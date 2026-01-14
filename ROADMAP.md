📊 Análisis del Estado Actual (Post-Auditoría V2.0)Este resumen técnico consolida el análisis de la arquitectura, los renderizadores y los errores detectados en la versión actual (master).1. Arquitectura y Flujo (MVC)El sistema sigue un patrón modular claro donde se separan los datos de su representación visual.Core (main_v2.py): Orquestador que lee config/test_exam.json, instancia los generadores y llama a LatexExamRenderer.Modelos (modules/): Clases de datos agnósticas (ej: SequentialExerciseData) que contienen la lógica matemática.Vistas (renderers/latex/): Transforman los modelos en código LaTeX puro usando plantillas y helpers.2. Análisis de RenderizadoresOrquestador (main_renderer.py):Carga paquetes robustos (circuitikz, tikz-timing, tcolorbox).Gestiona la cabecera institucional vía header.json.Enruta dinámicamente según el tipo de objeto (isinstance(data, Karnaugh...)).Numeración (numeracion_renderer.py):Distingue "Enunciado" vs "Solución" (texto rojo).⚠️ Dependencia Crítica: El método _render_grid espera carry_bits. Si el generador envía un string vacío (""), la fila azul de acarreo no se dibuja.Secuencial (secuencial_renderer.py):Utiliza LatexAssetManager para gestionar diagramas pesados y permitir corrección manual (resources/latex/).Genera IDs únicos (ej: ej1_seq_circuit) para evitar colisiones si hay múltiples ejercicios del mismo tipo.Utils (renderers/latex/utils/):circuit.py: Generación dinámica de circuitos JK/T/D con circuitikz.karnaugh.py: Implementa correctamente la secuencia Gray (00, 01, 11, 10).3. Errores y Deuda Técnica Detectada🚨 Bug Bloqueante (Secuencial): Se detectó la falta del argumento async_level="0" en SequentialGenerator. Estado: Corregido en la rama actual, pero debe verificarse en regresión.⚠️ Lógica Incompleta (Numeración): En generators.py (líneas ~89-91), la generación de operaciones aritméticas (Parte B) está incompleta.Faltan cálculos reales para overflow, underflow y carry_bits.Actualmente se pasa carry_bits="", lo que rompe la visualización de la solución en el PDF.Falta de "Solvers": El sistema genera problemas aleatorios pero no calcula sus soluciones (ecuaciones simplificadas, simulación de cronogramas), por lo que el PDF de "Solución" está incompleto.🚀 Hoja de Ruta de Implementación (V2 -> V2.1)Este documento detalla los pasos para solucionar la deuda técnica (solvers) y automatizar la producción (compilación).📦 Fase 0: DependenciasNecesitamos sympy para la simplificación de mapas de Karnaugh y álgebra booleana.pip install sympy
⚙️ Fase 1: Automatización de CompilaciónNecesitamos que Python llame a LaTeX automáticamente para generar los PDFs.Archivo: renderers/latex/utils/compiler.py (Crear nuevo)import subprocess
import os

def compile_tex_to_pdf(tex_file_path: str, output_dir: str = None) -> bool:
"""
Compila un archivo .tex a PDF usando lualatex y limpia archivos auxiliares.
"""
if not os.path.exists(tex_file_path):
print(f"❌ Archivo no encontrado: {tex_file_path}")
return False

    if output_dir is None:
        output_dir = os.path.dirname(tex_file_path)

    job_name = os.path.splitext(os.path.basename(tex_file_path))[0]
    
    # Comando lualatex (mejor para TikZ/Circuitikz)
    cmd = [
        'lualatex', 
        '-interaction=nonstopmode', 
        f'-output-directory={output_dir}',
        tex_file_path
    ]

    print(f"⚙️  Compilando {job_name}.tex ...")
    
    try:
        # Doble compilación para resolver referencias y calcular layout de TikZ
        subprocess.run(cmd, stdout=subprocess.DEVNULL, check=True)
        subprocess.run(cmd, stdout=subprocess.DEVNULL, check=True)
        
        # Limpieza de basura (.aux, .log, .out, etc.)
        for ext in ['.aux', '.log', '.out', '.synctex.gz']:
            junk = os.path.join(output_dir, job_name + ext)
            if os.path.exists(junk):
                os.remove(junk)
                
        print(f"✅ PDF Generado: {os.path.join(output_dir, job_name + '.pdf')}")
        return True
        
    except subprocess.CalledProcessError:
        print(f"❌ Error al compilar {job_name}. Revisa si tienes lualatex instalado y en el PATH.")
        return False
    except FileNotFoundError:
        print("❌ No se encontró el comando 'lualatex'. Instala TeXLive o MiKTeX.")
        return False
🧠 Fase 2: Implementar Solvers (Lógica)Los generadores deben calcular la solución exacta para rellenar los huecos detectados en el análisis.2.1 Módulo Combinacional (Karnaugh)Paso A: Actualizar ModeloEn modules/combinacional/models.py, clase KarnaughExerciseData:@dataclass
class KarnaughExerciseData(ExerciseData):

# ... campos existentes

# ... truth_table_outputs

solution_expr: str = "" # <--- CAMPO NUEVO para guardar la ecuación
Paso B: Actualizar GeneradorEn modules/combinacional/generators.py:from sympy.logic import SOPform
from sympy import symbols, latex

class KarnaughGenerator(ExerciseGenerator):
def generate(self, difficulty=1):

# ... (Mantener código actual de generación de outputs)

# outputs =

        # --- NUEVA LÓGICA DE RESOLUCIÓN ---
        # Identificar minterms (posiciones donde hay un 1)
        minterms = [i for i, val in enumerate(outputs) if val == 1]
        A, B, C, D = symbols('A B C D')
        
        # Calcular expresión simplificada usando SymPy
        expr = SOPform([A, B, C, D], minterms)
        sol_latex = latex(expr) # Convierte (A & ~B) a A \bar{B}
        
        return KarnaughExerciseData(
            # ... tus otros campos existentes ...
            truth_table_outputs=outputs,
            # ...
            solution_expr=f"${sol_latex}$" # Guardamos la solución formateada
        )
2.2 Módulo Secuencial (Simulador de Estados)Paso A: Actualizar ModeloEn modules/secuencial/models.py, clase SequentialExerciseData:@dataclass
class SequentialExerciseData(ExerciseData):

# ... campos existentes

solution_q0: str = "" # <--- CAMPO NUEVO: Secuencia calculada para Q0
solution_q1: str = "" # <--- CAMPO NUEVO: Secuencia calculada para Q1
Paso B: Actualizar GeneradorEn modules/secuencial/generators.py:class SequentialGenerator(ExerciseGenerator):

    def _simulate_ff(self, ff_type, input_seq, initial=0):
        """
        Simula un Flip-Flop ciclo a ciclo. 
        input_seq viene como 'LLHHLL...' (2 caracteres por ciclo según tu lógica actual)
        """
        q = initial
        out_wave = []
        
        # Procesar de 2 en 2 (porque tu input genera 2 caracteres por ciclo de reloj)
        for i in range(0, len(input_seq), 2):
            val_char = input_seq[i]
            val = 1 if val_char == 'H' else 0
            
            q_next = q
            if ff_type == 'T':
                if val == 1: q_next = 1 - q
            elif ff_type == 'JK': 
                # Asumiendo conexión J=K=Input (Modo Toggle controlado)
                if val == 1: q_next = 1 - q
            elif ff_type == 'D':
                q_next = val
                
            # Generar salida (mantener 2 chars por ciclo para sincronizar con tikz-timing)
            char = 'H' if q_next == 1 else 'L'
            out_wave.append(char * 2)
            q = q_next
            
        return "".join(out_wave)

    def generate(self, difficulty=1):
        # ... (Mantener tu código actual de generación de inputs) ...
        # input_sequence = ...
        
        # --- NUEVA LÓGICA DE SIMULACIÓN ---
        sol_q0 = self._simulate_ff(ff_type, input_sequence)
        
        return SequentialExerciseData(
            # ... tus otros campos existentes ...
            solution_q0=sol_q0,
            solution_q1=f"{width_units}{{}}" # Placeholder si no usamos Q1 aún
        )
2.3 Módulo Numeración (Corrección de Aritmética)Paso A: Implementar lógica de acarreoEn modules/numeracion/generators.py, arreglar la generación de operaciones:    # Pseudo-código para el fix:

# 1. Realizar suma/resta bit a bit

# 2. Guardar el acarreo de cada etapa en una lista

# 3. Convertir lista a string "00110..." para pasarlo a carry_bits

# 4. Calcular overflow real (Carry_in_sign != Carry_out_sign)

🎨 Fase 3: Renderizar SolucionesAhora que tenemos los datos, hay que pintarlos si is_solution=True.3.1 Actualizar renderers/latex/combinacional_renderer.pyModificar _render_karnaugh para mostrar la ecuación calculada:    def _render_karnaugh(self, data: KarnaughExerciseData, index: int) -> str:

# ... (código existente del enunciado y tabla)

        latex += r"\textbf{Espacio de Resolución:}" + "\n"
        
        # ... (código existente del mapa de Karnaugh) ...
        latex += self.asset_manager.get_component(...)
        
        # LÓGICA CONDICIONAL:
        if self.is_solution:
            latex += r"\vspace{0.5cm}" + "\n"
            latex += r"\begin{tcolorbox}[colback=green!10!white, title=Solución Calculada]" + "\n"
            latex += fr"\Large Resultado: {data.solution_expr}" + "\n"
            latex += r"\end{tcolorbox}" + "\n"
        else:
            latex += r"\vspace{3cm}" # Espacio en blanco para alumnos
            
        return latex
3.2 Actualizar renderers/latex/utils/timing.pyModificar render para usar las ondas simuladas en la solución:class TimingDiagramRenderer:
def render(self, data: SequentialExerciseData) -> str: # (Nota: Quitar is_solution de __init__ si no se usa, o pasarlo aquí)

# OJO: Necesitas saber si es solución. Puedes inyectar la info o deducirla si data.solution_q0 tiene datos

        # Si data.solution_q0 tiene algo y NO es el placeholder vacio, úsalo.
        # Pero mejor controlar esto desde fuera o pasar un flag.
        
        # Lógica sugerida:
        # Si data.solution_q0 es diferente de "" y queremos mostrar solución:
        q0_wave = data.solution_q0 if data.solution_q0 else data.output_placeholder
        q1_wave = data.solution_q1 if data.solution_q1 else data.output_placeholder
        
        # Para distinguir visualmente, si es solución ponerlo en rojo
        # style_q = "red" if data.solution_q0 else "black" (Simplificación)
        
        # ...
        rows.append(fr"{indent}{indent}Q0 & {q0_wave} \\") # Quitar [draw=none] si hay solución
        # ...
🚀 Fase 4: Integración FinalEditar main_v2.py para unir todo y generar los PDFs automáticamente.# Importar el compilador al inicio
from renderers.latex.utils.compiler import compile_tex_to_pdf

# ... dentro de la función main()

    # 2. Renderizado EXAMEN
    # ... (generación de Examen_V2.tex) ...
    # ... f.write(latex_code) ...
    
    print("📚 Generando PDF del Examen...")
    compile_tex_to_pdf(output_file)

    # 3. Renderizado SOLUCIÓN
    # ... (generación de Solucion_V2.tex) ...
    # ... f.write(latex_code_sol) ...
    
    print("📚 Generando PDF de la Solución...")
    compile_tex_to_pdf(output_file_sol)
