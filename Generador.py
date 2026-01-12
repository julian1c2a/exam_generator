import os
import random
from typing import List, Tuple, Any, Dict, Optional

# ==============================================================================
# CAPA DE CONFIGURACIÓN (AGNÓSTICA)
# ==============================================================================

class ExamSpecs:
    TITLE = "Fundamentos de Electrónica"
    SUBTITLE = "Parte I: Electrónica Digital"
    STUDENT_FIELD = "Nombre: ............................................................................ Fecha: ...................."

    # --- Ejercicio 1: Representación Numérica ---
    EX1_N_BITS = 8
    EX1_HEADERS = ['Id', 'Decimal', 'Binario Nat.', 'C2', 'Signo-Magnitud', 'BCD']
    EX1_ROW_LABELS = ['a', 'b', 'c', 'd']

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
# CAPA DE LÓGICA
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
\usepackage{tikz-timing}
\usepackage{amsmath}
\usepackage{array}
\usepackage{multirow}
\usepackage{colortbl}
\usepackage{enumitem}
\usepackage{float}
\usepackage{tcolorbox}

% Configuración de TikZ y tikz-timing
\usetikzlibrary{calc}

% Configuración de tcolorbox
\tcbset{
    colback=gray!5!white,
    colframe=gray!75!black,
    title=\textbf{ENUNCIADO},
    fonttitle=\bfseries,
    boxrule=0.5mm,
    arc=2mm
}

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

# --- FUNCIONES AUXILIARES DE LATEX ---

def gen_latex_tabla_verdad(vars_in: List[str], var_out: str, valores: Optional[List[int]]) -> str:
    num_vars = len(vars_in)
    num_rows = 2**num_vars
    col_def = "|" + "c|" * (num_vars + 1)

    latex = r"\begin{table}[H] \centering" + "\n"
    latex += r"\begin{tabular}{" + col_def + r"} \hline" + "\n"
    headers = [r"\textbf{" + v + r"}" for v in vars_in]
    header_row = " & ".join(headers) + r" & \textbf{" + var_out + r"} \\ \hline" + "\n"
    latex += r"\rowcolor[gray]{0.9} " + header_row

    for i in range(num_rows):
        bin_str = format(i, f'0{num_vars}b')
        input_cells = " & ".join(list(bin_str))
        if valores is not None:
            output_cell = r"\textbf{" + str(valores[i]) + r"}"
        else:
            output_cell = r" "
        latex += f"{input_cells} & {output_cell} \\\\ \\hline\n"

    latex += r"\end{tabular} \end{table}" + "\n"
    return latex

def gen_latex_mapa_karnaugh(label_izq="AB", label_sup="CD", label_out="F", show_trap=True, empty_headers=False) -> str:
    if empty_headers: show_trap = False
    if show_trap:
        grid_cols = 7; h_cols = 3; h_rows = 3
    else:
        grid_cols = 6; h_cols = 2; h_rows = 2

    col_def = "|" + "c|" * grid_cols
    latex = r"\begin{table}[H] \centering \renewcommand{\arraystretch}{2}" + "\n"
    latex += r"\begin{tabular}{" + col_def + r"} \hline" + "\n"

    latex += r"\multicolumn{" + str(h_cols) + r"}{|c|}{\multirow{" + str(h_rows) + r"}{*}{\Huge \textbf{" + label_out + r"}}} & \multicolumn{4}{c|}{\textbf{" + label_sup + r" =}} \\ \cline{" + str(h_cols+1) + r"-" + str(grid_cols) + r"}" + "\n"

    row_bins = ["00", "01", "10", "11"]
    row_grays = ["00", "01", "11", "10"]
    if empty_headers:
        blank = r"\hspace*{0.8cm}"
        row_bins = [blank] * 4; row_grays = [blank] * 4

    if show_trap:
        latex += r"\multicolumn{" + str(h_cols) + r"}{|c|}{} & 00 & 01 & 10 & 11 \\ \cline{" + str(h_cols+1) + r"-" + str(grid_cols) + r"}" + "\n"
        latex += r"\multicolumn{" + str(h_cols) + r"}{|c|}{} & 00 & 01 & 11 & 10 \\ \hline" + "\n"
    else:
        num_header = " & ".join(row_grays)
        latex += r"\multicolumn{" + str(h_cols) + r"}{|c|}{} & " + num_header + r" \\ \hline" + "\n"

    for i in range(4):
        label_cell = r"\multirow{4}{*}{\rotatebox{90}{\textbf{" + label_izq + r" =}}}" if i == 0 else ""
        if show_trap: num_cells = f"& {row_bins[i]} & {row_grays[i]}"
        else: num_cells = f"& {row_grays[i]}"

        start_cline = 2; end_cline = grid_cols
        line_cmd = r"\cline{" + str(start_cline) + r"-" + str(end_cline) + r"}" if i < 3 else r"\hline"
        latex += f"{label_cell} {num_cells} & & & & \\\\ {line_cmd}\n"

    latex += r"\end{tabular} \end{table}" + "\n"
    return latex

# --- GENERADORES DE EJERCICIOS ---

def gen_latex_ej1(valores_out: List[Tuple[str, int]]) -> str:
    latex = r"\section*{Ejercicio 1: Sistemas de Representación (" + str(ExamSpecs.EX1_N_BITS) + r" bits)}"
    latex += r"\begin{tcolorbox}[title=Enunciado]" + "\n"
    latex += r"\noindent \textbf{a)} Complete la tabla adjunta. El registro es de " + str(ExamSpecs.EX1_N_BITS) + r" bits. Si no es representable, escriba 'NR'." + "\n"
    latex += r"\end{tcolorbox}" + "\n"

    latex += r"\textbf{Respuesta:}" + "\n"
    latex += r"\begin{table}[H] \centering \renewcommand{\arraystretch}{1.5}" + "\n"
    latex += r"\begin{tabular}{|c|c|c|c|c|c|} \hline" + "\n"
    latex += r"\rowcolor[gray]{0.9} \textbf{Id} & \textbf{Decimal} & \textbf{Binario Nat.} & \textbf{C2} & \textbf{Signo-Mag.} & \textbf{BCD} \\ \hline" + "\n"

    for label in ExamSpecs.EX1_ROW_LABELS:
        opciones_columna = [1, 1, 2, 3, 3, 4, 4, 5]
        col_idx = random.choice(opciones_columna)
        val = 0; cells = [""] * 6; cells[0] = f"{label})"
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
        latex += " & ".join(cells) + r" \\ \hline" + "\n"
    latex += r"\end{tabular} \end{table}" + "\n"

    if len(valores_out) >= 2:
        latex += r"\begin{tcolorbox}[title=Enunciado (Parte b)]" + "\n"
        latex += r"\noindent \textbf{b)} Realice las siguientes operaciones aritméticas utilizando los valores de la tabla anterior." + "\n"
        latex += r"\end{tcolorbox}" + "\n"
        latex += r"\textbf{Respuesta:}" + "\n"
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
    for _ in range(random.randint(3, 6)):
        idx1 = random.randint(0, 15)
        idx2 = idx1 ^ (1 << random.randint(0, 3))
        outputs[idx1] = target_val
        outputs[idx2] = target_val

    latex += r"\begin{tcolorbox}[title=Enunciado]" + "\n"
    latex += r"\noindent Dada la función $F(A,B,C,D)$ definida por la siguiente tabla de verdad:" + "\n"
    latex += gen_latex_tabla_verdad(['A','B','C','D'], 'F', outputs)
    latex += r"\noindent Se pide:" + "\n"
    latex += r"\begin{enumerate}[label=\alph*)]" + "\n"
    latex += f"\\item Obtener la expresión canónica mediante {tipo_canonico}.\n"
    latex += r"\item Simplificar usando el mapa de Karnaugh (identificando numeración correcta)." + "\n"
    latex += f"\\item Implementar el circuito simplificado utilizando EXCLUSIVAMENTE puertas \\textbf{{{tipo_puerta}}}.\n"
    latex += r"\end{enumerate}" + "\n"
    latex += r"\end{tcolorbox}" + "\n"

    latex += r"\textbf{Espacio de Resolución:}" + "\n"
    latex += r"\vspace{0.2cm}"
    latex += r"\noindent \textit{Utilice el siguiente esquema (tache la numeración incorrecta):}"
    latex += gen_latex_mapa_karnaugh(label_izq="AB", label_sup="CD", label_out="F", show_trap=True, empty_headers=False)
    latex += r"\vspace{3cm} \hrule \vspace{0.2cm} \textit{Espacio para esquema lógico...}"
    return latex

def gen_latex_ej3() -> str:
    latex = r"\section*{Ejercicio 3: Problema de Diseño Lógico}"
    escenario = random.choice(ExamSpecs.EX3_SCENARIOS)
    logica = random.choice(escenario["logicas"])
    vars_clean = [v.split(':')[0].strip() for v in escenario["vars"]]
    out_clean = escenario["salida"].split(':')[0].strip()

    latex += r"\begin{tcolorbox}[title=Enunciado]" + "\n"
    latex += f"\\noindent \\textbf{{Contexto: {escenario['titulo']}}} \\\\" + "\n"
    latex += r"\begin{itemize}"
    for var in escenario["vars"]: latex += f"\\item {var}"
    latex += f"\\item Salida: {escenario['salida']}"
    latex += r"\end{itemize}" + "\n"
    latex += f"\\noindent \\textit{{\\textbf{{Lógica de funcionamiento:}} {logica}}}" + "\n"
    latex += r"\vspace{0.3cm} \\ \noindent \textbf{Se pide:} (Justifique todos los pasos)" + "\n"
    latex += r"\begin{enumerate} \item Tabla de Verdad. \item Mapa de Karnaugh y simplificación. \item Esquema lógico final. \end{enumerate}" + "\n"
    latex += r"\end{tcolorbox}" + "\n"

    latex += r"\textbf{Espacio de Resolución:}" + "\n"
    latex += r"\vspace{0.2cm}"
    latex += r"\noindent \textbf{1. Complete la Tabla de Verdad:}"
    latex += gen_latex_tabla_verdad(vars_clean, out_clean, valores=None)
    latex += r"\newpage"
    latex += r"\noindent \textbf{2. Rellene la numeración y simplifique en el Mapa de Karnaugh:}"
    l_izq = "".join(vars_clean[:2]); l_sup = "".join(vars_clean[2:])
    latex += gen_latex_mapa_karnaugh(label_izq=l_izq, label_sup=l_sup, label_out=out_clean, show_trap=False, empty_headers=True)
    latex += r"\vspace{1cm}"
    latex += r"\noindent \textbf{3. Esquema Lógico:}"
    latex += r"\vspace{4cm}"
    return latex

def gen_latex_ej4() -> str:
    latex = r"\section*{Ejercicio 4: Análisis de Bloques MSI}"
    tipo = random.choice(['MUX', 'COMPARADOR', 'SUMADOR'])

    latex += r"\begin{tcolorbox}[title=Enunciado]" + "\n"
    latex += f"\\noindent Dado el siguiente componente: \\textbf{{{tipo}}}"
    latex += r"\vspace{0.2cm}"

    latex += r"\begin{center} \begin{tikzpicture}"
    if tipo == 'MUX':
        latex += r"\draw[thick] (0,0) -- (0,8) -- (4,6) -- (4,2) -- (0,0) -- cycle;"
        latex += r"\node at (2,4) {\textbf{MUX 16:1}};"
        latex += r"\foreach \y in {0.5,1,...,7.5} \draw (-0.5,\y) -- (0,\y);"
        latex += r"\node[left] at (-0.5, 7.5) {I0}; \node[left] at (-0.5, 0.5) {I15};"
        latex += r"\foreach \x in {1,1.6,2.2,2.8} \draw (\x, -0.5) -- (\x, {(\x-2)*0.5 + 1});"
        latex += r"\node[below] at (2,-0.5) {S3..S0};"
        latex += r"\draw (3.5, -0.5) -- (3.5, 2.8); \node[below] at (3.5,-0.5) {$\overline{E}$}; \node[circle,draw,inner sep=1pt] at (3.5, 2.9) {};"
        latex += r"\draw (4,4) -- (5,4) node[right]{Y};"
        latex += r"\draw (4,3) -- (4.5,3); \node[circle,draw,inner sep=1pt] at (4.6,3) {}; \draw (4.7,3) -- (5,3) node[right]{$\overline{Y}$};"
    elif tipo == 'COMPARADOR':
        val_a = random.randint(0, 15); val_b = random.randint(0, 15)
        latex += r"\draw[thick] (0,0) rectangle (4,4);"
        # TEXTO REORGANIZADO
        latex += r"\node at (2,3.5) {\textbf{COMPARADOR}};"
        latex += r"\node at (2,0.5) {\textbf{4 BITS}};"

        # BUSES A Y B (GRUESOS Y DESPLAZADOS)
        latex += r"\draw[ultra thick] (-1.2, 3) -- (0,3);"
        latex += r"\node[left] at (-1.2, 3) {A};"
        latex += r"\draw[thick] (-0.7, 2.8) -- (-0.5, 3.2);" # Slash
        latex += r"\node[above] at (-0.6, 3.1) {\scriptsize 4};" # Num 4

        latex += r"\draw[ultra thick] (-1.2, 1) -- (0,1);"
        latex += r"\node[left] at (-1.2, 1) {B};"
        latex += r"\draw[thick] (-0.7, 0.8) -- (-0.5, 1.2);" # Slash
        latex += r"\node[above] at (-0.6, 1.1) {\scriptsize 4};" # Num 4

        # ENTRADAS CASCADA (LADO IZQUIERDO, INTERMEDIAS)
        cascada = [random.randint(0,1) for _ in range(3)]
        latex += r"\draw (-1, 2.4) -- (0, 2.4);"
        latex += r"\node[left] at (-1, 2.4) {\small $I_{>}=%d$};" % cascada[0]
        latex += r"\draw (-1, 2.0) -- (0, 2.0);"
        latex += r"\node[left] at (-1, 2.0) {\small $I_{=}=%d$};" % cascada[1]
        latex += r"\draw (-1, 1.6) -- (0, 1.6);"
        latex += r"\node[left] at (-1, 1.6) {\small $I_{<}=%d$};" % cascada[2]

        latex += r"\draw (4,3) -- (5,3) node[right]{$>$};"
        latex += r"\draw (4,2) -- (5,2) node[right]{$=$};"
        latex += r"\draw (4,1) -- (5,1) node[right]{$<$};"
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

    if tipo == 'MUX':
        inputs = [random.randint(0,1) for _ in range(16)]
        latex += f"\\noindent Entradas de datos (I0 a I15): {inputs} \\\\"
        latex += r"Determine las salidas $Y$ y $\overline{Y}$ para:"
        latex += r"\begin{enumerate}"
        for _ in range(3):
            addr = random.randint(0,15); ena = random.choice([0,1])
            latex += f"\\item Enable={ena}, Dirección={addr:04b}"
        latex += r"\end{enumerate}"
    elif tipo == 'COMPARADOR':
        val_a = random.randint(0, 15); val_b = random.randint(0, 15)
        latex += f"\\noindent Datos: A = {val_a} ({val_a:04b}), B = {val_b} ({val_b:04b}). Determine las 3 salidas."
    elif tipo == 'SUMADOR':
        val_a = random.randint(0, 15); val_b = random.randint(0, 15)
        latex += f"\\noindent Realice la suma A ({val_a}) + B ({val_b}) + Cin. Indique S, Cout y si hay Overflow."

    latex += r"\end{tcolorbox}" + "\n"
    latex += r"\textbf{Espacio de Resolución:}" + "\n"
    latex += r"\vspace{5cm}"
    return latex

def gen_latex_ej5() -> str:
    latex = r"\section*{Ejercicio 5: Sistemas Secuenciales}"

    ff = random.choice(['JK', 'D', 'T'])
    edge = random.choice(['rising', 'falling'])
    edge_txt = "Subida" if edge == 'rising' else "Bajada"
    has_async = random.choice([True, False])

    logic_type = 'SHIFT' if ff == 'D' else 'COUNTER'

    async_txt = "Sin Async"
    if has_async:
        atipo = random.choice(['PRE', 'CLR'])
        alvl = random.choice(['1', '0'])
        async_txt = f"Entrada asíncrona {atipo} activa a nivel {alvl}"

    latex += r"\begin{tcolorbox}[title=Enunciado]" + "\n"
    latex += f"\\noindent Sistema secuencial síncrono ({logic_type}) por flanco de \\textbf{{{edge_txt}}}. Biestables tipo \\textbf{{{ff}}}. {async_txt}."
    latex += r"\vspace{0.5cm}"

    latex += r"\begin{center} \begin{circuitikz}[scale=1.2, transform shape] \draw"

    # FF1 y FF2 con coordenadas
    latex += r"(0,0) node[flipflop "+ff+r", external pins width=0](FF1){Q0}"
    latex += r"(5,0) node[flipflop "+ff+r", external pins width=0](FF2){Q1}"

    # CLK COMÚN
    latex += r"; \draw (FF1.pin 2) -- ++(-0.5,0) -- ++(0,-1.5) coordinate(clk_bus);"
    latex += r"\draw (FF2.pin 2) -- ++(-0.5,0) -- ++(0,-1.5) -- (clk_bus);"
    latex += r"\draw (clk_bus) -- ++(-1,0) node[left]{CLK};"

    # LÓGICA
    if logic_type == 'SHIFT':
        latex += r"\draw (FF1.pin 1) -- ++(-1,0) node[left]{E};"
        latex += r"\draw (FF1.pin 6) -- (FF2.pin 1);"
        latex += r"\draw (FF1.pin 6) -- ++(0.5,0) -- ++(0,1) node[above]{Q0};"
        latex += r"\draw (FF2.pin 6) -- ++(0.5,0) -- ++(0,1) node[above]{Q1};"

    elif logic_type == 'COUNTER':
        if ff == 'JK':
            latex += r"\draw (FF1.pin 1) -- ++(-0.5,0) coordinate(j1) -- ++(-0.5,0) node[left]{E};"
            latex += r"\draw (FF1.pin 3) -- ++(-0.5,0) -- (j1);"
            latex += r"\draw (FF1.pin 6) -- ++(0.5,0) coordinate(q0_out) -- (FF2.pin 1);"
            latex += r"\draw (q0_out) -- ++(0,-0.5) -- ++(1.5,0) -- (FF2.pin 3);"
        elif ff == 'T':
            latex += r"\draw (FF1.pin 1) -- ++(-1,0) node[left]{E};"
            latex += r"\draw (FF1.pin 6) -- (FF2.pin 1);"
        latex += r"\draw (FF1.pin 6) -- ++(0,1) node[above]{Q0};"
        latex += r"\draw (FF2.pin 6) -- ++(0,1) node[above]{Q1};"

    if has_async:
        pin_name = "up" if atipo == 'PRE' else "down"
        latex += r"\draw (FF1." + pin_name + r") -- ++(0," + ("0.5" if atipo=='PRE' else "-0.5") + r") coordinate(async1);"
        latex += r"\draw (FF2." + pin_name + r") -- ++(0," + ("0.5" if atipo=='PRE' else "-0.5") + r") -- (async1);"
        latex += r"\draw (async1) -- ++(0," + ("0.5" if atipo=='PRE' else "-0.5") + r") node[" + ("above" if atipo=='PRE' else "below") + r"]{ASYNC};"

    latex += r"; \end{circuitikz} \end{center}"

    latex += r"\noindent \textbf{Se pide:} a) Ecuaciones de entrada. b) Completar el cronograma."
    latex += r"\end{tcolorbox}" + "\n"

    latex += r"\textbf{Espacio de Resolución:}" + "\n"
    latex += r"\vspace{2cm}"

    latex += r"\begin{center}"
    # SCALE 1.8CM
    latex += r"\begin{tikztimingtable}[timing/slope=0, x=1.8cm, y=0.5cm]"

    cycles = ExamSpecs.EX5_CRONO_CYCLES
    width = cycles * 2

    # CLK
    clk_str = f"{cycles}{{C}}"
    latex += r"CLK & " + clk_str + r" \\"

    # ASYNC
    if has_async:
        active_high = ('1' in async_txt)
        if active_high:
            async_sig = "2H " + str(width-2) + "L"
        else:
            async_sig = "2L " + str(width-2) + "H"
        latex += r"ASYNC & " + async_sig + r" \\"

    # ENTRADA E
    input_str = ""
    for _ in range(width):
        input_str += "H" if random.randint(0,1) else "L"
    latex += r"E & " + input_str + r" \\"

    # SALIDAS VACÍAS
    # Usamos 'Z' (High Impedance) con draw=none para asegurar el espacio sin dibujar
    out_str = f"{width}{{Z}}"

    latex += r"Q0 & [draw=none] " + out_str + r" \\"
    latex += r"Q1 & [draw=none] " + out_str + r" \\"

    latex += r"\extracode"
    latex += r"\tablegrid"
    latex += r"\end{tikztimingtable}"
    latex += r"\end{center}"

    return latex

# ==============================================================================
# MAIN
# ==============================================================================

def main():
    valores_ej1 = []
    latex_code = get_latex_preamble()
    latex_code += gen_latex_ej1(valores_ej1)
    latex_code += r"\newpage"
    latex_code += gen_latex_ej2()
    latex_code += r"\newpage"
    latex_code += gen_latex_ej3()
    latex_code += r"\newpage"
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