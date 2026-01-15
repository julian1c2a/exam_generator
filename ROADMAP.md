# 🗺️ ROADMAP - Generador de Exámenes de Electrónica v2.1+

## 📊 RESUMEN EJECUTIVO

**Proyecto**: Generador automatizado de ejercicios y exámenes de **Fundamentos de Electrónica**  
**Objetivo**: Crear una plataforma modular que genere problemas con soluciones auto-calculadas en LaTeX/PDF e HTML  
**Estado Actual**: V2.0 - Arquitectura base funcional, solver incompleto  
**Responsable**: Equipo de Desarrollo  
**Última actualización**: 15 de enero de 2026  

---

## �️ ARQUITECTURA RECOMENDADA: SEPARACIÓN DE RESPONSABILIDADES

### 🚨 PROBLEMA ACTUAL EN RENDERERS

Observando `main_renderer.py` y `combinacional_renderer.py`, hay **acoplamiento excesivo**:

```
ACOPLAMIENTO ACTUAL (❌ Problemático)
┌─────────────────────────────────────┐
│   LatexExamRenderer                 │
│  (Enrutador + Orquestador)          │
├─────────────────────────────────────┤
│ - Carga header.json                 │
│ - Gestiona preamble/footer LaTeX    │
│ - Decide isinstance() para cada tipo│
│ - Instancia 3 renderers específicos │
│ - Maneja compilación              │
└──────────────┬──────────────────────┘
               │
     ┌─────────┼─────────┬──────────┐
     ▼         ▼         ▼          ▼
NumerRenderer CombRenderer SecRenderer ?
     │         │         │
     ├─→ DetalleEspecífico  ❌ ALTO ACOPLAMIENTO
     └─→ Lógica Compartida NO EXISTE
```

**Problemas Identificados**:

1. **SoC Débil**: Cada renderer mezcla estructura general con detalles específicos
2. **Código Duplicado**: Enunciado/Solución logic en cada renderer por separado
3. **Asset Manager Acoplado**: Inyectado en cada renderer, no es reutilizable
4. **Sin Estrategia de Composición**: ¿Qué si quiero HTML + LaTeX al mismo tiempo?
5. **Estilos No Centralizados**: Colores, fuentes, espacios definidos ad-hoc en cada renderer

### ✅ SOLUCIÓN PROPUESTA: Arquitectura en Capas

```
NUEVA ARQUITECTURA (✅ Desacoplada)

┌────────────────────────────────────────────────────────┐
│         CAPA 1: ORQUESTACIÓN                          │
│        LatexExamRenderer                              │
│  (Solo enrutamiento y coordinación)                   │
└──────────┬─────────────────────┬──────────────────────┘
           │                     │
    ┌──────▼──────┐      ┌───────▼────────┐
    │ CAPA 2: ESTRATEGIAS      │
    │ (Template/Factory)       │
    ├──────────────┤      │
    │ Numeracion   │◀─────┤ RenderStrategy
    │ Combinacional│◀─────┤ (Interface)
    │ Secuencial   │      │
    └──────┬───────┘      └────────────────┘
           │
    ┌──────▼──────────────────────────┐
    │  CAPA 3: COMPONENTES COMPARTIDOS │
    ├──────────────────────────────────┤
    │ • StyleManager (colores, fuentes)│
    │ • LayoutManager (espacios)       │
    │ • AssetManager (recursos)        │
    │ • ContentFactory (enunciado/sol) │
    └──────────────────────────────────┘
           △
           │
    ┌──────┴──────────────────┐
    │  CAPA 4: UTILIDADES     │
    ├──────────────────────────┤
    │ • TruthTableRenderer     │
    │ • KarnaughRenderer       │
    │ • CircuitRenderer        │
    │ • TimingDiagramRenderer  │
    └──────────────────────────┘
```

---

## �🎯 ANÁLISIS DEL ESTADO ACTUAL

### ✅ LO QUE FUNCIONA

| Componente | Estado | Observaciones |
|-----------|--------|---------------|
| **Arquitectura MVC** | ✅ Completa | Separación clara datos/vistas |
| **ExamBuilder** | ✅ Funcional | Lee JSON, instancia generadores |
| **LatexExamRenderer** | ✅ Robusto | Cabecera, enrutamiento dinámico |
| **Módulo Numeración** | ✅ 60% | Conversiones básicas funciona |
| **Módulo Combinacional** | ✅ 50% | Karnaugh visual, falta simplificación automática |
| **Módulo Secuencial** | ✅ 40% | Timing diagrams, falta simulación |
| **Renderers Utils** | ⚠️ Parcial | Karnaugh OK, circuitos/timing incompletos |

### 🚨 DEUDA TÉCNICA CRÍTICA

1. **NO hay Solvers**: Los generadores crean problemas pero NO calculan soluciones
   - Karnaugh: Genera tabla → Falta: simplificación automática con SymPy
   - Secuencial: Genera inputs → Falta: simulación de FF cronograma
   - Numeración: Genera operandos → Falta: cálculo real con acarreos

2. **Dependencias Faltantes**:
   - ❌ `sympy` (para álgebra booleana)
   - ❌ Compilador LaTeX → PDF automático
   - ❌ Gestión de assets LaTeX pesados

3. **Renderizado Incompleto**:
   - Enunciado: ✅ Se ve bien
   - Solución: ❌ Vacía o incorrecta (sin datos del solver)

---

## 🚀 FASES DE IMPLEMENTACIÓN INMEDIATA

### **FASE 1: SOLVERS Y CÁLCULOS** *(Semanas 1-2)* 🔴 CRÍTICO

#### 1.1 Instalar Dependencias

```bash
pip install sympy pytest numpy
```

#### 1.2 Módulo Numeración - Fix Acarreos

**Archivo**: `modules/numeracion/generators.py`

```python
def _calculate_addition(self, a: int, b: int, base: int = 2) -> tuple:
    """Calcula suma con acarreo explícito."""
    result = []
    carry = 0
    carry_list = []
    
    # Procesar bit a bit (o dígito a dígito en otra base)
    for i in range(max_bits):
        bit_a = (a >> i) & 1
        bit_b = (b >> i) & 1
        temp = bit_a + bit_b + carry
        result.append(temp % 2)
        carry = temp // 2
        carry_list.append(carry)
    
    return result, carry_list, carry  # (resultado, [acarreos por posición], acarreo final)
```

**Modelo actualizado**: `modules/numeracion/models.py`

```python
@dataclass
class NumerationExerciseData(ExerciseData):
    # ... existentes ...
    solution_result: str = ""        # "10110" en binario
    solution_carry_bits: str = ""    # "00110" (acarreos por posición)
    solution_overflow: bool = False  # Desbordamiento detectado
```

#### 1.3 Módulo Combinacional - Simplificación Booleana

**Archivo**: `modules/combinacional/generators.py`

```python
from sympy.logic import SOPform, POSform
from sympy import symbols, latex, simplify

class KarnaughGenerator(ExerciseGenerator):
    def generate(self, difficulty=1):
        # ... generar truth_table_outputs como antes ...
        
        # NUEVO: Calcular solución
        minterms = [i for i, bit in enumerate(outputs) if bit == 1]
        
        # Variables booleanas
        vars_list = ['A', 'B', 'C', 'D'][:num_variables]
        sym_vars = symbols(vars_list)
        
        # Forma simplificada
        expr = SOPform(sym_vars, minterms) if minterms else False
        solution_expr = latex(expr)  # Convierte a LaTeX: A \bar{B} + C
        
        return KarnaughExerciseData(
            # ... existentes ...
            solution_expr=f"${solution_expr}$",
            solution_simplified=True
        )
```

**Modelo actualizado**: `modules/combinacional/models.py`

```python
@dataclass
class KarnaughExerciseData(ExerciseData):
    # ... existentes ...
    solution_expr: str = ""           # "$A \\bar{B} + C$"
    solution_simplified: bool = False
```

#### 1.4 Módulo Secuencial - Simulador de Flip-Flops

**Archivo**: `modules/secuencial/generators.py`

```python
class SequentialGenerator(ExerciseGenerator):
    def _simulate_flipflop(self, ff_type: str, inputs: str, initial_q: int = 0) -> str:
        """
        Simula un FF ciclo a ciclo.
        Entrada: "HHLLHH..." (2 chars por ciclo de reloj)
        """
        q = initial_q
        output = []
        
        for i in range(0, len(inputs), 2):
            input_bit = 1 if inputs[i] == 'H' else 0
            
            # Lógica del FF
            if ff_type == 'T':      # Toggle si input=1
                q = (q + input_bit) % 2
            elif ff_type == 'D':    # Q toma el valor de input
                q = input_bit
            elif ff_type == 'JK':   # J=K=input (toggle if 1)
                if input_bit: q = 1 - q
            
            # Agregar onda: 2 chars (bajo + alto en tikz-timing)
            output.append('HH' if q else 'LL')
        
        return ''.join(output)
    
    def generate(self, difficulty=1):
        # ... generar input_sequence como antes ...
        
        # NUEVO: Simular soluciones
        solution_q0 = self._simulate_flipflop(self.ff_type, input_sequence)
        
        return SequentialExerciseData(
            # ... existentes ...
            solution_q0=solution_q0,
            solution_q1=""  # Placeholder si no usamos Q
        )
```

**Modelo actualizado**: `modules/secuencial/models.py`

```python
@dataclass
class SequentialExerciseData(ExerciseData):
    # ... existentes ...
    solution_q0: str = ""   # "HHLLHH..."
    solution_q1: str = ""   # Inversión de Q0 si aplica
    solution_sim_done: bool = False
```

---

### **FASE 2: COMPILADOR LATEX → PDF** *(Semana 1)* 🔴 CRÍTICO

**Archivo nuevo**: `renderers/latex/utils/compiler.py`

```python
import subprocess
import os

def compile_tex_to_pdf(tex_file_path: str, output_dir: str = None, attempts: int = 2) -> bool:
    """
    Compila .tex → .pdf usando lualatex (mejor para TikZ).
    """
    if not os.path.exists(tex_file_path):
        print(f"❌ Archivo no encontrado: {tex_file_path}")
        return False
    
    if output_dir is None:
        output_dir = os.path.dirname(tex_file_path)
    
    job_name = os.path.splitext(os.path.basename(tex_file_path))[0]
    
    cmd = ['lualatex', '-interaction=nonstopmode', f'-output-directory={output_dir}', tex_file_path]
    
    print(f"⚙️  Compilando {job_name}.tex...")
    
    try:
        # Doble compilación: primera pasa referencias, segunda las resuelve
        for attempt in range(attempts):
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode != 0:
                print(f"⚠️  Compilación {attempt+1}: warnings/errores detectados")
                print(result.stdout[-500:] if len(result.stdout) > 500 else result.stdout)
        
        # Limpiar basura
        for ext in ['.aux', '.log', '.out', '.synctex.gz']:
            junk_file = os.path.join(output_dir, job_name + ext)
            if os.path.exists(junk_file):
                os.remove(junk_file)
        
        pdf_path = os.path.join(output_dir, job_name + '.pdf')
        if os.path.exists(pdf_path):
            print(f"✅ PDF generado: {pdf_path}")
            return True
        else:
            print(f"❌ PDF no se creó. Revisa errores LaTeX arriba.")
            return False
            
    except FileNotFoundError:
        print("❌ 'lualatex' no encontrado. Instala TeXLive: sudo apt install texlive-latex-full")
        return False
```

---

### **FASE 3: RENDERIZAR SOLUCIONES** *(Semana 2)* 🟡 IMPORTANTE

#### 3.1 Actualizar Combinacional Renderer

**Archivo**: `renderers/latex/combinacional_renderer.py`

```python
def _render_karnaugh(self, data: KarnaughExerciseData, index: int) -> str:
    latex = # ... código existente enunciado/tabla ...
    
    # NUEVA SECCIÓN CONDICIONAL:
    if self.is_solution:
        latex += r"\vspace{0.3cm}" + "\n"
        latex += r"\begin{tcolorbox}[colback=green!15!white, colframe=green!50, title=\textbf{Solución Simplificada}]" + "\n"
        latex += fr"$$\boxed{{{data.solution_expr}}}$$" + "\n"
        latex += r"\end{tcolorbox}" + "\n"
    else:
        latex += r"\vspace{4cm}" + "\n"  # Espacio para que resuelva el alumno
    
    return latex
```

#### 3.2 Actualizar Secuencial Renderer

**Archivo**: `renderers/latex/secuencial_renderer.py`

Modificar la sección de timing para usar `solution_q0`:

```python
# En el método _render_timing_diagram:
q0_wave = data.solution_q0 if self.is_solution else data.output_placeholder
q1_wave = data.solution_q1 if self.is_solution else data.output_placeholder

# Si es solución, cambiar estilo (opcional: color rojo para q0)
q0_style = "[color=red]" if self.is_solution and data.solution_q0 else ""
```

#### 3.3 Actualizar Numeración Renderer

**Archivo**: `renderers/latex/numeracion_renderer.py`

```python
# En _render_grid, usar solution_carry_bits si es_solución:
if self.is_solution and data.solution_carry_bits:
    carry_bits_str = " ".join(data.solution_carry_bits)
else:
    carry_bits_str = " ".join(["\\phantom{0}"] * len(...)  # Vacío

# Para el resultado final:
if self.is_solution:
    result_latex = fr"\textcolor{{red}}{{{data.solution_result}}}"
else:
    result_latex = "\\phantom{0000}"
```

---

### **FASE 4: INTEGRACIÓN FINAL** *(Fin Semana 2)* 🟢 FINAL

**Archivo**: `main_v2.py` (actualizar)

```python
import os
import argparse
from core.exam_builder import ExamBuilder
from renderers.latex.main_renderer import LatexExamRenderer
from renderers.latex.utils.compiler import compile_tex_to_pdf  # NUEVO

def main():
    default_config = os.path.join("config", "test_exam.json")
    
    print("🚀 Generador de Exámenes V2.1 (con Solvers)")
    
    # 1. CONSTRUCCIÓN
    try:
        builder = ExamBuilder(default_config)
        exercises = builder.build()  # Ahora los generadores calculan soluciones ✨
    except Exception as e:
        print(f"❌ Error: {e}")
        return
    
    output_dir = os.path.join("build", "latex")
    os.makedirs(output_dir, exist_ok=True)
    
    # 2. RENDERIZAR ENUNCIADO
    print("📄 Renderizando enunciado...")
    try:
        renderer_exam = LatexExamRenderer(is_solution=False)
        latex_code = renderer_exam.render(exercises)
        
        exam_file = os.path.join(output_dir, "Examen_V2.tex")
        with open(exam_file, "w", encoding="utf-8") as f:
            f.write(latex_code)
        print(f"✅ {exam_file}")
        
        # Compilar a PDF
        print("📚 Compilando PDF enunciado...")
        compile_tex_to_pdf(exam_file)
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
    
    # 3. RENDERIZAR SOLUCIÓN
    print("\n📋 Renderizando solución...")
    try:
        renderer_sol = LatexExamRenderer(is_solution=True)
        latex_code_sol = renderer_sol.render(exercises)
        
        sol_file = os.path.join(output_dir, "Solucion_V2.tex")
        with open(sol_file, "w", encoding="utf-8") as f:
            f.write(latex_code_sol)
        print(f"✅ {sol_file}")
        
        # Compilar a PDF
        print("📚 Compilando PDF solución...")
        compile_tex_to_pdf(sol_file)
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
    
    print("\n✨ ¡Examen y soluciones generados exitosamente!")

if __name__ == "__main__":
    main()
```

---

## 📅 ROADMAP EXTENDIDO (POST V2.1)

### **FASE 5: EXPANSIÓN DE MÓDULOS** *(Semanas 3-6)*

| Módulo | Ejercicios Requeridos | Prioridad | Est. |
|--------|----------------------|-----------|------|
| **Boole Avanzado** | Puertas lógicas, síntesis NAND/NOR | 🔴 | 1w |
| **Sistemas Comb.** | MUX, Decodificadores, Sumadores | 🔴 | 2w |
| **Máquinas Estados** | FSM Moore/Mealy, Diagramas | 🟡 | 2w |
| **Memorias Digitales** | ROM, RAM, Flash (teórico) | 🟡 | 1w |
| **Análoga Básica** | Ohm, Thevenin, AC simple | 🟢 | 2w |

### **FASE 6: INTERFAZ WEB** *(Semanas 7-10)* 🔮

- Backend REST API (FastAPI)
- Frontend interactivo (React)
- Base de datos de ejercicios (PostgreSQL)
- Sistema de evaluación automática
- Generación de reportes

### **FASE 7: PRODUCCIÓN** *(Semana 11+)*

- Deployment en servidor
- Integración LMS (Moodle, Canvas)
- App móvil (opcional)
- Documentación pedagógica completa

---

### **IMPLEMENTACIÓN DETALLADA DE NUEVA ARQUITECTURA RENDERERS**

#### Paso 1: Crear Manager de Estilos Centralizado

**Archivo nuevo**: `renderers/latex/utils/style_manager.py`

```python
from dataclasses import dataclass
from enum import Enum

class ColorScheme(Enum):
    LIGHT = {
        'background': 'white',
        'problem': 'blue!5',
        'solution': 'green!10',
        'error': 'red!10',
        'title_fg': 'black',
        'title_bg': 'blue!20',
    }
    DARK = {
        'background': 'gray!5',
        'problem': 'blue!15',
        'solution': 'green!20',
        'error': 'red!20',
    }

@dataclass
class LatexStyle:
    """Estilo centralizado para LaTeX."""
    # Márgenes y espacios
    section_spacing: str = "0.3cm"
    problem_spacing: str = "0.5cm"
    solution_spacing: str = "0.8cm"
    work_space: str = "4cm"
    
    # Colores
    colors: dict = None
    
    # Tipografía
    title_font: str = r"\Large\bfseries"
    problem_font: str = r"\normalsize"
    solution_font: str = r"\normalsize\color{red}"
    
    def __post_init__(self):
        if self.colors is None:
            self.colors = ColorScheme.LIGHT.value

@dataclass
class BoxStyle:
    """Estilo para cajas (tcolorbox)."""
    colback: str = "blue!5"
    colframe: str = "blue!50"
    title: str = "Enunciado"
    border_width: str = "2pt"
```

#### Paso 2: Crear ContentFactory

**Archivo nuevo**: `renderers/latex/utils/content_factory.py`

```python
from typing import Union
from core.generator_base import ExerciseData

class ContentFactory:
    """Genera contenido (enunciado/solución) sin mezclar lógica de renderizado."""
    
    @staticmethod
    def get_problem_header(exercise_data: ExerciseData, index: int, is_solution: bool = False) -> str:
        """Encabezado estándar para todos los problemas."""
        title = exercise_data.title
        prefix = "✓ SOLUCIÓN:" if is_solution else f"Problema {index}:"
        return fr"\section*{{{prefix} {title}}}"
    
    @staticmethod
    def get_statement_box(description: str, is_solution: bool = False) -> tuple:
        """Genera caja con enunciado. Retorna (header, content, footer)."""
        
        if is_solution:
            return (
                r"\begin{tcolorbox}[colback=green!10!white, colframe=green!50, title=\textbf{SOLUCIÓN}]",
                description,
                r"\end{tcolorbox}"
            )
        else:
            return (
                r"\begin{tcolorbox}[colback=blue!5!white, colframe=blue!50, title=Enunciado]",
                description,
                r"\end{tcolorbox}"
            )
    
    @staticmethod
    def get_work_space(height: str = "4cm", is_solution: bool = False) -> str:
        """Genera espacio en blanco o solución."""
        if is_solution:
            return ""  # Sin espacio si es solución
        return fr"\vspace{{{height}}}"
```

#### Paso 3: Crear Interface/Strategy para Renderers

**Archivo nuevo**: `renderers/latex/base_renderer.py`

```python
from abc import ABC, abstractmethod
from typing import List
from core.generator_base import ExerciseData
from renderers.latex.utils.style_manager import LatexStyle
from renderers.latex.utils.asset_manager import LatexAssetManager

class BaseLatexRenderer(ABC):
    """Clase abstracta para todos los renderers específicos."""
    
    def __init__(self, is_solution: bool = False, style: LatexStyle = None):
        self.is_solution = is_solution
        self.style = style or LatexStyle()
        self.asset_manager = LatexAssetManager()
    
    @abstractmethod
    def render(self, data: ExerciseData, index: int) -> str:
        """Renderiza un ejercicio completo."""
        pass
    
    @abstractmethod
    def get_supported_types(self) -> List[type]:
        """Retorna tipos de ExerciseData que este renderer soporta."""
        pass
    
    def _add_header(self, content: str, title: str, index: int) -> str:
        """Método compartido para agregar encabezado."""
        return fr"\newpage \section*{{Ejercicio {index}: {title}}}" + "\n" + content
    
    def _add_solution_box(self, content: str) -> str:
        """Método compartido para agregar caja de solución."""
        if self.is_solution:
            return (
                r"\begin{tcolorbox}[colback=green!15!white, colframe=green!50!black, "
                r"title=\textbf{Solución Calculada}, boxrule=2pt]" + "\n"
                + content + "\n"
                + r"\end{tcolorbox}" + "\n"
            )
        return content
```

#### Paso 4: Refactorizar Renderers Específicos

**Archivo**: `renderers/latex/combinacional_renderer.py` (REFACTORIZADO)

```python
from renderers.latex.base_renderer import BaseLatexRenderer
from modules.combinacional.models import KarnaughExerciseData, LogicProblemExerciseData, MSIExerciseData
from renderers.latex.utils.truth_table import TruthTableRenderer
from renderers.latex.utils.karnaugh import KarnaughMapRenderer

class CombinacionalLatexRenderer(BaseLatexRenderer):
    """Renderer para ejercicios combinacionales (Boole, Karnaugh, MSI)."""
    
    def __init__(self, is_solution: bool = False, style=None):
        super().__init__(is_solution, style)
        self.tt_renderer = TruthTableRenderer()
        self.kmap_renderer = KarnaughMapRenderer()
    
    def get_supported_types(self):
        return [KarnaughExerciseData, LogicProblemExerciseData, MSIExerciseData]
    
    def render(self, data: object, index: int) -> str:
        if isinstance(data, KarnaughExerciseData):
            return self._render_karnaugh(data, index)
        elif isinstance(data, LogicProblemExerciseData):
            return self._render_problem(data, index)
        elif isinstance(data, MSIExerciseData):
            return self._render_msi(data, index)
        return ""
    
    def _render_karnaugh(self, data: KarnaughExerciseData, index: int) -> str:
        """Renderiza ejercicio de Karnaugh con separación clara de responsabilidades."""
        
        # 1. ENCABEZADO (responsabilidad compartida)
        latex = self._add_header(data.description, data.title, index)
        
        # 2. ENUNCIADO (content factory)
        header, desc, footer = self._get_statement_box(data.description)
        latex += header + "\n" + desc + "\n" + footer + "\n"
        
        # 3. TABLA DE VERDAD (delegado a especialista)
        latex += self.tt_renderer.render(data.vars_name, data.out_name, data.truth_table_outputs)
        
        # 4. ESPACIO DE TRABAJO O SOLUCIÓN
        if self.is_solution:
            # Si es solución: mostrar resultado
            latex += self._add_solution_box(
                fr"$$\boxed{{{data.solution_expr}}}$$"
            )
        else:
            # Si es enunciado: espacio en blanco
            latex += fr"\vspace{{{self.style.work_space}}}" + "\n"
        
        return latex
    
    def _get_statement_box(self, description: str) -> tuple:
        """Factory de cajas de enunciado."""
        if self.is_solution:
            return (
                r"\begin{tcolorbox}[colback=green!10, title=Enunciado Original]",
                description,
                r"\end{tcolorbox}"
            )
        return (
            r"\begin{tcolorbox}[colback=blue!5, title=Enunciado]",
            description,
            r"\end{tcolorbox}"
        )
```

#### Paso 5: Refactorizar LatexExamRenderer (Orquestador)

**Archivo**: `renderers/latex/main_renderer.py` (REFACTORIZADO)

```python
import json
import os
from typing import List, Dict, Type
from core.generator_base import ExerciseData
from renderers.latex.base_renderer import BaseLatexRenderer
from renderers.latex.combinacional_renderer import CombinacionalLatexRenderer
from renderers.latex.secuencial_renderer import SecuencialLatexRenderer
from renderers.latex.numeracion_renderer import NumeracionLatexRenderer
from renderers.latex.utils.style_manager import LatexStyle

class LatexExamRenderer:
    """
    Orquestador principal: 
    - Solo enrutamiento de tipos
    - Delegación clara a estrategias
    - Composición de resultado final
    """
    
    def __init__(self, is_solution: bool = False, style: LatexStyle = None):
        self.is_solution = is_solution
        self.style = style or LatexStyle()
        self.header_config = self._load_json(os.path.join("config", "header.json"))
        
        # Registrar estrategias (Strategy Pattern)
        self.strategies: Dict[Type, BaseLatexRenderer] = {
            # Cada renderer se registra para sus tipos soportados
        }
        self._register_strategies()
    
    def _register_strategies(self):
        """Registra todos los renderers disponibles."""
        renderers = [
            NumeracionLatexRenderer(self.is_solution, self.style),
            CombinacionalLatexRenderer(self.is_solution, self.style),
            SecuencialLatexRenderer(self.is_solution, self.style),
        ]
        
        for renderer in renderers:
            for supported_type in renderer.get_supported_types():
                self.strategies[supported_type] = renderer
    
    def _load_json(self, filename: str) -> dict:
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    
    def render(self, exercises: List[ExerciseData]) -> str:
        """Render completo: preamble + ejercicios + footer."""
        latex = self._get_preamble()
        
        for i, ex_data in enumerate(exercises, 1):
            renderer = self._get_renderer(ex_data)
            if renderer:
                latex += renderer.render(ex_data, i)
            else:
                latex += f"\\section*{{Ejercicio {i}: ERROR}}\n"
                latex += f"No hay renderer para {type(ex_data).__name__}\n"
        
        latex += self._get_footer()
        return latex
    
    def _get_renderer(self, data: ExerciseData) -> BaseLatexRenderer:
        """Busca renderer apropiado (Strategy Pattern)."""
        return self.strategies.get(type(data))
    
    def _get_preamble(self) -> str:
        """Preamble LaTeX (Responsabilidad clara)."""
        h = self.header_config
        title = f"{h.get('exam_title', '')} - {h.get('exam_type', '')}"
        if self.is_solution:
            title += r" \textcolor{red}{(SOLUCIÓN)}"
        
        return fr"""\documentclass[a4paper,11pt]{{article}}
\usepackage[utf8]{{inputenc}}
\usepackage[spanish]{{babel}}
\usepackage{{tikz,circuitikz,tikz-timing,amsmath,amssymb,tcolorbox}}
\title{{{title}}}
\author{{{h.get('professors', '')}}}
\date{{{h.get('date', '')}}}
\begin{{document}}
\maketitle
"""
    
    def _get_footer(self) -> str:
        return r"\end{document}"
```

#### Paso 6: Crear Composable Builder para Renderers

**Archivo nuevo**: `renderers/latex/renderer_factory.py`

```python
from renderers.latex.main_renderer import LatexExamRenderer
from renderers.latex.utils.style_manager import LatexStyle, ColorScheme

class LatexRendererFactory:
    """Factory para crear renderers con diferentes configuraciones."""
    
    @staticmethod
    def create_exam_renderer(is_solution: bool = False, 
                             color_scheme: str = 'LIGHT') -> LatexExamRenderer:
        """Crea un renderer de examen con estilo específico."""
        
        style = LatexStyle()
        style.colors = ColorScheme[color_scheme].value
        
        return LatexExamRenderer(is_solution=is_solution, style=style)
    
    @staticmethod
    def create_custom_renderer(is_solution: bool = False,
                               work_space: str = "4cm",
                               solution_color: str = "green!10") -> LatexExamRenderer:
        """Crea renderer con espacios y colores personalizados."""
        
        style = LatexStyle(work_space=work_space)
        style.colors['solution'] = solution_color
        
        return LatexExamRenderer(is_solution=is_solution, style=style)
```

---

### **VENTAJAS DE ESTA ARQUITECTURA**

| Aspecto | Antes ❌ | Después ✅ |
|--------|---------|----------|
| **Responsabilidades** | Mezcladas | Claras y separadas |
| **Reutilización** | Baja | Alta (StyleManager, ContentFactory) |
| **Testing** | Difícil | Fácil (units independientes) |
| **Mantenimiento** | Propenso a bugs | Cambios localizados |
| **Extensibilidad** | Nueva clase = editar main | Factory + Strategy |
| **Duplicación** | Código repetido | DRY |
| **Composabilidad** | Fija | Flexible |

---

## ✅ CHECKLIST AMPLIADO (Semanas 1-2)

### SEMANA 1: Solvers + Compilador

**Solvers (Matemática)**:

- [ ] Instalar `sympy`
- [ ] Crear `modules/numeracion/generators.py` con lógica de acarreos
- [ ] Crear `modules/combinacional/generators.py` con simplificación Booleana
- [ ] Crear `modules/secuencial/generators.py` con simulador de FF
- [ ] Tests unitarios para cada solver

**Compilador**:

- [ ] Crear `renderers/latex/utils/compiler.py`
- [ ] Tests de compilación LaTeX

**Total**: ~35 horas

---

### SEMANA 2: Refactorización Renderers + Integración

**Arquitectura de Renderers** (Separación de Responsabilidades):

- [ ] Crear `renderers/latex/utils/style_manager.py`
- [ ] Crear `renderers/latex/utils/content_factory.py`
- [ ] Crear `renderers/latex/base_renderer.py`
- [ ] Crear `renderers/latex/renderer_factory.py`
- [ ] Refactorizar `combinacional_renderer.py`
- [ ] Refactorizar `secuencial_renderer.py`
- [ ] Refactorizar `numeracion_renderer.py`
- [ ] Refactorizar `main_renderer.py` (orquestador)
- [ ] Tests de integración (end-to-end)

**Integración Final**:

- [ ] Actualizar `main_v2.py` con compilador automático
- [ ] Ejecutar pipeline completo
- [ ] Generar PDFs Examen + Solución sin errores

**Total**: ~40 horas

**MÉTRICA DE ÉXITO**:

```
✅ Examen_V2.pdf (enunciado completo con diagramas)
✅ Solucion_V2.pdf (soluciones calculadas automáticamente)
✅ 0 errores LaTeX
✅ Código con 80%+ cobertura de tests
```

---

## 🔗 REFERENCIAS Y RECURSOS

### Documentación

- [SymPy Logic](https://docs.sympy.org/latest/modules/logic/index.html)
- [Instalar `sympy`
- [ ] Crear `renderers/latex/utils/compiler.py`
- [ ] Actualizar `modules/numeracion/generators.py` con lógica de acarreos
- [ ] Actualizar `modules/numeracion/models.py` (campos solution_*)
- [ ] Actualizar `modules/combinacional/generators.py` con simplificación
- [ ] Actualizar `modules/combinacional/models.py`
- [ ] Actualizar `modules/secuencial/generators.py` con simulador
- [ ] Actualizar `modules/secuencial/models.py`
- [ ] Crear tests para solvers
- [ ] Ejecutar `python main_v2.py` y generar Examen_V2.pdf + Solucion_V2.pdf sin errores
- [TikZ Manual](https://tikz.dev/)
- [CircuiTikZ](https://ctan.org/pkg/circuitikz)

### Ejemplos

- Karnaugh con SymPy: `sympy.logic.inference.SOPform`
- Timing diagrams: `tikz-timing` package
- Circuit elements: `circuitikz` library

---

**Próximo checkpoint**: Fin de semana del 19 de enero
**Meta**: Solvers 100% funcionales, PDFs generados automáticamente
