import os
import random
from typing import List, Tuple, Any, Dict

# ==============================================================================
# CAPA DE CONFIGURACIÓN (AGNÓSTICA)
# ==============================================================================

class ExamSpecs:
    """
    Contenedor centralizado de especificaciones.
    Define los datos del examen independientemente del formato de salida.
    """

    TITLE = "Fundamentos de Electrónica"
    SUBTITLE = "Parte I: Electrónica Digital"
    STUDENT_FIELD = "Nombre: ............................................................................ Fecha: ...................."

    # --- Ejercicio 1: Representación Numérica ---
    EX1_N_BITS = 8
    EX1_HEADERS = ['Id', 'Decimal', 'Binario Nat.', 'C2', 'Signo-Magnitud', 'BCD']
    EX1_ROW_LABELS = ['a', 'b', 'c', 'd']

    # --- Ejercicio 2: Karnaugh ---
    # En LaTeX controlamos anchos con p{...} o celdas estándar

    # --- Ejercicio 3: Escenarios ---
    EX3_SCENARIOS = [
        {
            "titulo": "Sistema de Seguridad de Bóveda Bancaria",
            "vars": ["A: Sensor Reloj (1=Laboral)", "B: Llave Director (1=Si)", "C: Llave Gerente (1=Si)", "D: Código (1=OK)"],
            "salida": "Z: Apertura",
            "logicas": [
                "La puerta se abre SI estamos en horario laboral Y se ha introducido el código correcto. ADEMÁS, por seguridad, fuera de horario laboral (A=0) la puerta también se puede abrir, pero SOLO si están presentes AMBAS llaves (Director y Gerente).",
                "La puerta se abre siempre que el código de seguridad sea correcto, SALVO que estemos fuera de horario laboral y falte alguna de las llaves (Director o Gerente).",
                "Para abrir la puerta se requiere estrictamente el código de seguridad. ADEMÁS, si estamos en horario laboral basta con eso, pero si NO es horario laboral, se requiere adicionalmente la llave del Director."
            ]
        },
        {
            "titulo": "Control de Reactor Químico Industrial",
            "vars": ["P: Presión (1=Alta)", "T: Temp (1=Alta)", "N: Nivel (1=Alto)", "M: Manual (1=ON)"],
            "salida": "E: Válvula Escape",
            "logicas": [
                "La válvula de escape debe abrirse SIEMPRE que se active el interruptor manual. AUTOMÁTICAMENTE, también debe abrirse si la Presión es alta Y (la Temperatura es alta O el Nivel es crítico).",
                "La válvula se abre si hay Presión alta, PERO solo si el Nivel también es crítico. Sin embargo, si la Temperatura es alta, la válvula se abre independientemente.",
                "Por seguridad, la válvula se abre si al menos DOS de los tres sensores (Presión, Temperatura, Nivel) están en estado alto. El interruptor Manual abre la válvula directamente."
            ]
        },
        {
            "titulo": "Sistema de Riego Inteligente",
            "vars": ["H: Humedad (1=Seco)", "L: Luz (1=Día)", "D: Depósito (1=Lleno)", "T: Temp (1=Calor)"],
            "salida": "R: Riego",
            "logicas": [
                "Riega SI (Seco Y Depósito lleno). ADEMÁS, si hace Calor excesivo, riega forzosamente siempre que haya agua.",
                "Nunca riega sin agua. Si hay agua, riega si está Seco, PERO evita regar de Día (L=1) salvo que haga Calor excesivo.",
                "Riega si está Seco. BLOQUEO: No riega si es de Día Y el depósito no está lleno. El Calor activa riego de emergencia."
            ]
        }
    ]

    # --- Ejercicio 5: Cronogramas ---
    EX5_CRONO_CYCLES = 6

# ==============================================================================
# CAPA DE LÓGICA (Conversiones y Cálculos)
# ==============================================================================

def int_to_bin_str(val: int, bits: int) -> str:
    return format(val if val >= 0 else (1 << bits) + val, f'0{bits}b')

def int_to_bcd_str(val: int) -> str:
    if not (0 <= val <= 99): return "NR"
    tens = val // 10
    units = val % 10
    return f"{tens:04b} {units:04b}"

def int_to_sm_str(val: int, bits: int) -> str:
    if val >= 0:
        return format(val, f'0{bits}b')
    else:
        abs_val = abs(val)
        bin_abs = format(abs_val, f'0{bits - 1}b')
        return '1' + bin_abs

# ==============================================================================
# CAPA DE PRESENTACIÓN (Generación LaTeX)
# ==============================================================================

def get_latex_preamble() -> str:
    return r"""\documentclass[a4paper,11pt]{article}
\usepackage[utf8]{inputenc}
\usepackage[spanish]{babel}
\usepackage[top=2cm, bottom=2cm, left=2cm, right=2cm]{geometry}
\usepackage{tikz}
\usepackage{circuitikz}
\usepackage{amsmath}
\usepackage{array}
\usepackage{multirow}
\usepackage{colortbl}
\usepackage{enumitem}
\usepackage{float}

% Configuración de TikZ para cronogramas
\usetikzlibrary{calc}

\begin{document}

% --- ENCABEZADO ---
\begin{center}
    {\Huge \textbf{""" + ExamSpecs.TITLE + r"""}} \\
    \vspace{0.2cm}
    {\Large \textbf{""" + ExamSpecs.SUBTITLE + r"""}}
\end{center}
\vspace{0.5cm}
\noindent """ + ExamSpecs.STUDENT_FIELD + r"""
\vspace{0.5cm}
\hrule
\vspace{0.5cm}
"""

def gen_latex_ej1(valores_out: List[Tuple[str, int]]) -> str:
    latex = r"\section*{Ejercicio 1: Sistemas de Representación (" + str(ExamSpecs.EX1_N_BITS) + r" bits)}"
    latex += r"\noindent \textbf{a) Complete la tabla.} El registro es de " + str(ExamSpecs.EX1_N_BITS) + r" bits. Si no es representable, escriba 'NR'."

    latex += r"\begin{table}[H] \centering \renewcommand{\arraystretch}{1.5}"
    latex += r"\begin{tabular}{|c|c|c|c|c|c|} \hline"
    latex += r"\rowcolor[gray]{0.9} \textbf{Id} & \textbf{Decimal} & \textbf{Binario Nat.} & \textbf{C2} & \textbf{Signo-Mag.} & \textbf{BCD} \\ \hline"

    for label in ExamSpecs.EX1_ROW_LABELS:
        opciones_columna = [1, 1, 2, 3, 3, 4, 4, 5]
        col_idx = random.choice(opciones_columna)
        val = 0
        cells = [""] * 6
        cells[0] = f"{label})"

        es_signed_col = col_idx in [1, 3, 4]
        signo = -1 if (es_signed_col and random.random() < 0.7) else 1
        n_bits = ExamSpecs.EX1_N_BITS

        text_val = ""
        if col_idx == 1: magnitud = random.randint(0, 200); val = signo * magnitud; text_val = str(val)
        elif col_idx == 2: val = random.randint(0, 255); text_val = int_to_bin_str(val, n_bits)
        elif col_idx == 3: limit = 128 if signo == -1 else 127; magnitud = random.randint(0, limit); val = signo * magnitud; text_val = int_to_bin_str(val, n_bits)
        elif col_idx == 4: magnitud = random.randint(0, 127); val = signo * magnitud; text_val = int_to_sm_str(val, n_bits)
        elif col_idx == 5: val = random.randint(0, 99); text_val = int_to_bcd_str(val)

        cells[col_idx] = text_val
        valores_out.append((label, val))

        latex += " & ".join(cells) + r" \\ \hline"

    latex += r"\end{tabular} \end{table}"

    # Parte B
    if len(valores_out) >= 2:
        latex += r"\noindent \textbf{b) Realice las siguientes operaciones aritméticas} utilizando los valores de la tabla:"
        latex += r"\begin{itemize}"
        for i in range(1, 3):
            fila1 = random.choice(valores_out)
            fila2 = random.choice([x for x in valores_out if x != fila1])
            es_suma = random.choice([True, False])
            sistema = random.choice(['Binario Natural', 'Complemento a 2'])
            op_char = "+" if es_suma else "-"
            op_text = "Suma" if es_suma else "Resta"

            latex += r"\item \textbf{" + f"{i}) {op_text} en {sistema}:" + r"} Fila " + fila1[0] + f" {op_char} Fila " + fila2[0]
            latex += r"\\ \vspace{0.2cm} Resultado (Binario): \underline{\hspace{4cm}}"
            latex += r"\\ \textit{¿Overflow? $\square$ \hspace{0.5cm} ¿Underflow? $\square$ \hspace{0.5cm} ¿Correcto? $\square$}"
        latex += r"\end{itemize}"

    return latex

def gen_latex_ej2() -> str:
    latex = r"\section*{Ejercicio 2: Diseño y Simplificación Lógica}"

    es_minterms = random.choice([True, False])
    tipo_canonico = "Minitérminos (Suma de Productos)" if es_minterms else "Maxitérminos (Producto de Sumas)"
    tipo_puerta = "NAND" if es_minterms else "NOR"
    target_val = 1 if es_minterms else 0
    default_val = 0 if es_minterms else 1
    outputs = [default_val] * 16

    # Generar adyacencias
    for _ in range(random.randint(3, 6)):
        idx1 = random.randint(0, 15)
        idx2 = idx1 ^ (1 << random.randint(0, 3))
        outputs[idx1] = target_val
        outputs[idx2] = target_val

    latex += r"\noindent Dada la función $F(A,B,C,D)$ definida por la siguiente tabla de verdad:"
    latex += r"\vspace{0.3cm}"

    # TABLA DE VERDAD (Estrecha)
    latex += r"\begin{table}[H] \centering"
    latex += r"\begin{tabular}{|c|c|c|c|c|} \hline"
    latex += r"\rowcolor[gray]{0.9} \textbf{A} & \textbf{B} & \textbf{C} & \textbf{D} & \textbf{F} \\ \hline"
    for i in range(16):
        b = f"{i:04b}"
        latex += f"{b[0]} & {b[1]} & {b[2]} & {b[3]} & \\textbf{{{outputs[i]}}} \\\\ \\hline"
    latex += r"\end{tabular} \end{table}"

    latex += r"\noindent Utilice el siguiente esquema para simplificar. \textbf{Nota: La numeración incluye opciones correctas (Gray) e incorrectas (Binario Nat.), táchese la que no proceda.}"
    latex += r"\vspace{0.5cm}"

    # MAPA DE KARNAUGH (Tabla compleja)
    # Estructura 7x7
    # Filas: [Header CD] [Num Bad] [Num Good] [Row 00] [Row 01] [Row 11] [Row 10]
    # Cols:  [Header AB] [Num Bad] [Num Good] [Col 00] [Col 01] [Col 11] [Col 10]

    latex += r"\begin{table}[H] \centering \renewcommand{\arraystretch}{2}"
    latex += r"\begin{tabular}{|c|c|c|c|c|c|c|} \hline"

    # Fila 1: F (merged 3x3) | CD Label (merged 1x4)
    latex += r"\multicolumn{3}{|c|}{\multirow{3}{*}{\Huge \textbf{F}}} & \multicolumn{4}{c|}{\textbf{CD =}} \\ \cline{4-7}"

    # Fila 2: Num Bad (Cols)
    latex += r"\multicolumn{3}{|c|}{} & 00 & 01 & 10 & 11 \\ \cline{4-7}"

    # Fila 3: Num Good (Cols)
    latex += r"\multicolumn{3}{|c|}{} & 00 & 01 & 11 & 10 \\ \hline"

    # Filas de la cuadrícula
    row_bins = ["00", "01", "10", "11"]
    row_grays = ["00", "01", "11", "10"]

    for i in range(4):
        # Columna 1: AB Label (merged 4x1) -> Solo en la primera iteración
        col1 = r"\multirow{4}{*}{\rotatebox{90}{\textbf{AB =}}}" if i == 0 else ""
        latex += f"{col1} & {row_bins[i]} & {row_grays[i]} & & & & \\\\ \\hline"

    latex += r"\end{tabular} \end{table}"

    latex += r"\begin{enumerate}[label=\alph*)]"
    latex += f"\item Obtener la expresión canónica mediante {tipo_canonico}."
    latex += r"\item Simplificar usando el mapa (identificando numeración correcta)."
    latex += f"\item Implementar el circuito simplificado utilizando EXCLUSIVAMENTE puertas \\textbf{{{tipo_puerta}}}."
    latex += r"\end{enumerate}"

    return latex

def gen_latex_ej3() -> str:
    latex = r"\section*{Ejercicio 3: Problema de Diseño Lógico}"
    escenario = random.choice(ExamSpecs.EX3_SCENARIOS)
    logica = random.choice(escenario["logicas"])

    latex += f"\\noindent \\textbf{{Contexto: {escenario['titulo']}}} \\\\"
    latex += r"\begin{itemize}"
    for var in escenario["vars"]:
        latex += f"\\item {var}"
    latex += f"\\item Salida: {escenario['salida']}"
    latex += r"\end{itemize}"

    latex += f"\\noindent \\textit{{\\textbf{{Lógica de funcionamiento:}} {logica}}}"
    latex += r"\vspace{0.3cm} \\ \noindent \textbf{Se pide:} (Justifique todos los pasos)"
    latex += r"\begin{enumerate} \item Tabla de Verdad. \item Mapa de Karnaugh y simplificación. \item Esquema lógico final. \end{enumerate}"
    return latex

def gen_latex_ej4() -> str:
    latex = r"\section*{Ejercicio 4: Análisis de Bloques MSI}"
    tipo = random.choice(['MUX', 'COMPARADOR', 'SUMADOR'])
    latex += f"\\noindent Dado el siguiente componente: \\textbf{{{tipo}}}"
    latex += r"\vspace{0.5cm}"

    latex += r"\begin{center} \begin{tikzpicture}"

    if tipo == 'MUX':
        # Dibujo Mux 16:1
        latex += r"\draw[thick] (0,0) -- (0,8) -- (4,6) -- (4,2) -- (0,0) -- cycle;"
        latex += r"\node at (2,4) {\textbf{MUX 16:1}};"
        # Entradas Izq
        latex += r"\foreach \y in {0.5,1,...,7.5} \draw (-0.5,\y) -- (0,\y);"
        latex += r"\node[left] at (-0.5, 7.5) {I0}; \node[left] at (-0.5, 0.5) {I15};"
        # Selectores
        latex += r"\foreach \x in {1,1.6,2.2,2.8} \draw (\x, -0.5) -- (\x, {(\x-2)*0.5 + 1});" # Rough calc
        latex += r"\node[below] at (2,-0.5) {S3..S0};"
        # Enable
        latex += r"\draw (3.5, -0.5) -- (3.5, 2.8); \node[below] at (3.5,-0.5) {$\overline{E}$}; \node[circle,draw,inner sep=1pt] at (3.5, 2.9) {};"
        # Salidas
        latex += r"\draw (4,4) -- (5,4) node[right]{Y};"
        latex += r"\draw (4,3) -- (4.5,3); \node[circle,draw,inner sep=1pt] at (4.6,3) {}; \draw (4.7,3) -- (5,3) node[right]{$\overline{Y}$};"

        inputs = [random.randint(0,1) for _ in range(16)]
        latex += r"\end{tikzpicture} \end{center}"

        latex += f"\\noindent Entradas de datos (I0 a I15): {inputs} \\\\"
        latex += r"Determine las salidas $Y$ y $\overline{Y}$ para:"
        latex += r"\begin{enumerate}"
        for _ in range(3):
            addr = random.randint(0,15)
            ena = random.choice([0,1])
            latex += f"\\item Enable={ena}, Dirección={addr:04b}"
        latex += r"\end{enumerate}"

    elif tipo == 'COMPARADOR':
        val_a = random.randint(0, 15); val_b = random.randint(0, 15)
        latex += r"\draw[thick] (0,0) rectangle (4,4);"
        latex += r"\node at (2,3) {\textbf{COMPARADOR}};"
        latex += r"\node at (2,2) {\textbf{4 BITS}};"
        # Inputs A y B
        latex += r"\draw (-1, 3) -- (0,3) node[midway, above]{A(4)};"
        latex += r"\draw (-1, 1) -- (0,1) node[midway, above]{B(4)};"
        # Cascadas
        cascada = [random.randint(0,1) for _ in range(3)]
        latex += r"\draw (1, -1) -- (1,0) node[below, yshift=-1cm]{I($>$)=%d};" % cascada[0]
        latex += r"\draw (2, -1) -- (2,0) node[below, yshift=-1cm]{I($=$)=%d};" % cascada[1]
        latex += r"\draw (3, -1) -- (3,0) node[below, yshift=-1cm]{I($<$)=%d};" % cascada[2]
        # Salidas
        latex += r"\draw (4,3) -- (5,3) node[right]{$>$};"
        latex += r"\draw (4,2) -- (5,2) node[right]{$=$};"
        latex += r"\draw (4,1) -- (5,1) node[right]{$<$};"
        latex += r"\end{tikzpicture} \end{center}"

        latex += f"\\noindent Datos: A = {val_a} ({val_a:04b}), B = {val_b} ({val_b:04b}). Determine las 3 salidas."

    elif tipo == 'SUMADOR':
        val_a = random.randint(0, 15); val_b = random.randint(0, 15); cin = random.randint(0,1)
        latex += r"\draw[thick] (0,0) rectangle (4,4);"
        latex += r"\node at (2,2) {\textbf{SUMADOR 4 BITS}};"
        latex += r"\draw (-1,3) -- (0,3) node[midway, above]{A};"
        latex += r"\draw (-1,1) -- (0,1) node[midway, above]{B};"
        latex += r"\draw (2,4) -- (2,5) node[above]{Cin=%d};" % cin
        latex += r"\draw (4,2.5) -- (5,2.5) node[right]{S(4)};"
        latex += r"\draw (4,1.5) -- (5,1.5) node[right]{Cout};"
        latex += r"\end{tikzpicture} \end{center}"

        latex += f"\\noindent Realice la suma A ({val_a}) + B ({val_b}) + Cin. Indique S, Cout y si hay Overflow."

    return latex

def gen_latex_ej5() -> str:
    latex = r"\section*{Ejercicio 5: Sistemas Secuenciales}"

    ff = random.choice(['JK', 'D', 'T'])
    edge = random.choice(['rising', 'falling']) # TikZ timing naming convention
    edge_txt = "Subida" if edge == 'rising' else "Bajada"
    has_async = random.choice([True, False])

    async_txt = "Sin Async"
    if has_async:
        atipo = random.choice(['PRE', 'CLR'])
        alvl = random.choice(['1', '0'])
        async_txt = f"Entrada asíncrona {atipo} activa a nivel {alvl}"

    latex += f"\\noindent Sistema secuencial síncrono por flanco de \\textbf{{{edge_txt}}}. Biestables tipo \\textbf{{{ff}}}. {async_txt}."
    latex += r"\vspace{0.5cm}"

    # DIBUJO DEL ESQUEMA LÓGICO (Básico con Circuitikz)
    latex += r"\begin{center} \begin{circuitikz} \draw"

    # Dibujamos dos FF genéricos
    # FlipFlop 1
    latex += r"(0,0) node[flipflop "+ff+r", dot on clock, external pins width=0](FF1){Q0}" if edge=='falling' else r"(0,0) node[flipflop "+ff+r", external pins width=0](FF1){Q0}"
    # FlipFlop 2
    latex += r"(5,0) node[flipflop "+ff+r", dot on clock, external pins width=0](FF2){Q1}" if edge=='falling' else r"(5,0) node[flipflop "+ff+r", external pins width=0](FF2){Q1}"

    latex += r"; \end{circuitikz} \end{center}"

    latex += r"\noindent \textbf{Se pide:} a) Ecuaciones de entrada. b) Completar el cronograma."
    latex += r"\vspace{0.5cm}"

    # DIBUJO DEL CRONOGRAMA (Manual con TikZ puro para control total)
    latex += r"\begin{center} \begin{tikzpicture}[x=1cm, y=0.5cm]"

    cycles = ExamSpecs.EX5_CRONO_CYCLES

    # Reloj
    latex += r"\draw (0,4) node[left]{CLK};"
    latex += r"\draw[thick] (0,4)"
    for _ in range(cycles):
        latex += r" -- ++(0.5,0) -- ++(0,1) -- ++(0.5,0) -- ++(0,-1)"
    latex += r";"

    # Entrada E (Aleatoria)
    latex += r"\draw (0,2) node[left]{E};"
    latex += r"\draw[thick] (0,2)"
    curr_e = 0
    for _ in range(cycles * 2):
        new_e = random.randint(0,1)
        if new_e != curr_e:
            latex += r" -- ++(0," + str(new_e - curr_e) + r")"
            curr_e = new_e
        latex += r" -- ++(0.5,0)"
    latex += r";"

    # Líneas vacías para Q0 y Q1
    latex += r"\draw (0,0) node[left]{Q0}; \draw[dotted] (0,0) -- (6,0);"
    latex += r"\draw (0,-1.5) node[left]{Q1}; \draw[dotted] (0,-1.5) -- (6,-1.5);"

    # Async signal si existe
    if has_async:
        latex += r"\draw (0,5.5) node[left]{ASYNC};"
        # Pulso inicial
        latex += r"\draw[thick] (0,5.5) -- (0.2, 5.5) -- (0.2, 6.5) -- (1.5, 6.5) -- (1.5, 5.5) -- (6, 5.5);"

    latex += r"\end{tikzpicture} \end{center}"

    return latex

# ==============================================================================
# MAIN
# ==============================================================================

def main():
    valores_ej1 = [] # Para pasar datos entre 1a y 1b

    latex_code = get_latex_preamble()
    latex_code += gen_latex_ej1(valores_ej1)
    latex_code += gen_latex_ej2()
    latex_code += r"\newpage"
    latex_code += gen_latex_ej3()
    latex_code += gen_latex_ej4()
    latex_code += r"\newpage"
    latex_code += gen_latex_ej5()

    latex_code += r"\end{document}"

    filename = "Examen_Electronica_Digital.tex"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(latex_code)

    print(f"✅ ¡ÉXITO! Archivo generado: {os.path.abspath(filename)}")

if __name__ == "__main__":
    main()