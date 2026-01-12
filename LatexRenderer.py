from typing import List, Optional
from exam_model import *

class LatexRenderer:
    def get_preamble(self) -> str:
        return r"""\documentclass[a4paper,11pt]{article}
\usepackage[utf8]{inputenc}
\usepackage[spanish]{babel}
\usepackage[top=2cm, bottom=2cm, left=2cm, right=2cm]{geometry}
\usepackage{tikz}
\usepackage{circuitikz}
\usepackage{tikz-timing}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{array}
\usepackage{multirow}
\usepackage{colortbl}
\usepackage{enumitem}
\usepackage{float}
\usepackage{tcolorbox}
\usetikzlibrary{calc}
\tcbset{colback=gray!5!white, colframe=gray!75!black, title=\textbf{ENUNCIADO}, fonttitle=\bfseries, boxrule=0.5mm, arc=2mm}
\begin{document}
\begin{center}
    {\Huge \textbf{Fundamentos de Electrónica}} \\ \vspace{0.2cm}
    {\Large \textbf{Parte I: Electrónica Digital}}
\end{center}
\vspace{0.5cm}
\noindent Nombre: ............................................................................ Fecha: ....................
\vspace{0.5cm} \hrule \vspace{0.5cm}
"""

    def render_ej1(self, data: Exercise1Data) -> str:
        latex = fr"\section*{{Ejercicio 1: Sistemas de Representación ({data.n_bits} bits)}}" + "\n"
        latex += r"\begin{tcolorbox}[title=Enunciado]" + "\n"
        latex += fr"\noindent \textbf{{a)}} Complete la tabla. Registro de {data.n_bits} bits. Si no es representable, escriba 'NR'." + "\n"
        latex += r"\end{tcolorbox}" + "\n\n"

        # Tabla
        latex += r"\textbf{Respuesta:}" + "\n"
        latex += r"\begin{table}[H] \centering \renewcommand{\arraystretch}{1.5}" + "\n"
        latex += r"\begin{tabular}{|c|c|c|c|c|c|} \hline" + "\n"
        latex += r"\rowcolor[gray]{0.9} \textbf{Id} & \textbf{Decimal} & \textbf{Binario Nat.} & \textbf{C2} & \textbf{Signo-Mag.} & \textbf{BCD} \\ \hline" + "\n"

        for row in data.rows:
            cells = [""] * 6
            cells[0] = f"{row.label})"
            cells[row.target_col_idx] = row.target_val_str
            latex += " & ".join(cells) + r" \\ \hline" + "\n"
        latex += r"\end{tabular} \end{table}" + "\n"

        # Parte B
        if data.operations:
            latex += r"\begin{tcolorbox}[title=Enunciado (Parte b)]" + "\n"
            latex += r"\noindent \textbf{b)} Realice las siguientes operaciones aritméticas." + "\n"
            latex += r"\end{tcolorbox}" + "\n"
            latex += r"\begin{itemize}" + "\n"
            for i, op in enumerate(data.operations, 1):
                latex += fr"\item \textbf{{{i}) {op.op_type} en {op.system}:}} Fila {op.operand1} {op.operator_symbol} Fila {op.operand2}" + "\n"
                latex += r"\\ \vspace{0.2cm} Resultado: \underline{\hspace{4cm}} \\ \textit{¿Overflow? $\square$ ¿Correcto? $\square$}" + "\n"
            latex += r"\end{itemize}" + "\n"

        return latex

    def render_ej2(self, data: Exercise2Data) -> str:
        latex = r"\newpage \section*{Ejercicio 2: Diseño y Simplificación Lógica}" + "\n"
        latex += r"\begin{tcolorbox}[title=Enunciado]" + "\n"
        latex += r"\noindent Dada la función definida por:" + "\n"

        # Helper interno para tabla verdad
        latex += self._render_truth_table(['A','B','C','D'], 'F', data.truth_table_outputs)

        latex += r"\noindent Se pide:" + "\n"
        latex += r"\begin{enumerate}[label=\alph*)]" + "\n"
        latex += fr"\item Obtener la expresión canónica ({data.canon_type})." + "\n"
        latex += r"\item Simplificar por Karnaugh." + "\n"
        latex += fr"\item Implementar con puertas \textbf{{{data.gate_type}}}." + "\n"
        latex += r"\end{enumerate} \end{tcolorbox}" + "\n"

        latex += r"\textbf{Espacio de Resolución:}" + "\n"
        latex += self._render_kmap_template("AB", "CD", "F", show_trap=True)
        latex += r"\vspace{3cm} \hrule" + "\n"
        return latex

    def render_ej3(self, data: Exercise3Data) -> str:
        latex = r"\newpage \section*{Ejercicio 3: Problema de Diseño Lógico}" + "\n"
        latex += r"\begin{tcolorbox}[title=Enunciado]" + "\n"
        latex += fr"\textbf{{Contexto: {data.title}}}" + "\n"
        latex += r"\begin{itemize}" + "\n"
        for v in data.variables: latex += fr"\item {v}" + "\n"
        latex += fr"\item Salida: {data.output_name}" + "\n"
        latex += r"\end{itemize}" + "\n"
        latex += fr"\textit{{Lógica: {data.logic_description}}}" + "\n"
        latex += r"\end{tcolorbox}" + "\n"

        latex += r"\textbf{1. Tabla de Verdad:}" + "\n"
        latex += self._render_truth_table(data.var_names_clean, data.out_name_clean, None)
        latex += r"\newpage \textbf{2. Mapa de Karnaugh:}" + "\n"

        l_izq = "".join(data.var_names_clean[:2])
        l_sup = "".join(data.var_names_clean[2:])
        latex += self._render_kmap_template(l_izq, l_sup, data.out_name_clean, show_trap=False, empty_headers=True)
        return latex

    def render_ej4(self, data: Exercise4Data) -> str:
        latex = r"\newpage \section*{Ejercicio 4: Bloques MSI}" + "\n"
        latex += r"\begin{tcolorbox}[title=Enunciado]" + "\n"
        latex += fr"Dado el componente: \textbf{{{data.block_type}}}" + "\n"
        latex += r"\begin{center} \begin{tikzpicture}" + "\n"

        # Lógica de dibujo separada por tipo
        if data.block_type == 'MUX':
            latex += self._draw_mux()
        elif data.block_type == 'COMPARADOR':
            latex += self._draw_comparator(data.params)
        elif data.block_type == 'SUMADOR':
            latex += self._draw_adder(data.params)

        latex += r"\end{tikzpicture} \end{center}" + "\n"

        # Preguntas específicas
        if data.block_type == 'MUX':
            latex += fr"Entradas I0-I15: {data.params['inputs']} \\ Determine Y para:" + "\n"
            latex += r"\begin{enumerate}" + "\n"
            for case in data.params['cases']:
                latex += fr"\item Enable={case['ena']}, Dir={case['addr']:04b}" + "\n"
            latex += r"\end{enumerate}" + "\n"

        latex += r"\end{tcolorbox} \vspace{5cm}" + "\n"
        return latex

    def render_ej5(self, data: Exercise5Data) -> str:
        latex = r"\newpage \section*{Ejercicio 5: Secuenciales}" + "\n"
        edge_txt = "Subida" if data.edge_type == "Subida" else "Bajada"
        async_txt = f"Async \\textbf{{{data.async_type}(asyn)}} a nivel {data.async_level}" if data.has_async else "Sin Async"

        latex += r"\begin{tcolorbox}[title=Enunciado]" + "\n"
        latex += fr"Síncrono ({data.logic_type}) por {edge_txt}. FF {data.ff_type}. {async_txt}." + "\n"

        # Circuito
        latex += r"\begin{center} \begin{circuitikz}[scale=1.2, transform shape] \draw" + "\n"
        latex += self._draw_sequential_circuit(data)
        latex += r"; \end{circuitikz} \end{center}" + "\n"
        latex += r"\end{tcolorbox}" + "\n"

        # Cronograma
        latex += r"\begin{center} \begin{tikztimingtable}[timing/slope=0, x=2.0cm, y=0.8cm]" + "\n"
        latex += fr"CLK\hspace{{1em}} & {data.clk_sequence} \\" + "\n"
        if data.has_async:
            latex += fr"{data.async_type}(asyn)\hspace{{1em}} & {data.async_sequence} \\" + "\n"
        latex += fr"E\hspace{{2.5em}} & {data.input_sequence} \\" + "\n"
        latex += fr"Q0 & [draw=none, fill=none] {data.output_placeholder} \\" + "\n"
        latex += fr"Q1 & [draw=none, fill=none] {data.output_placeholder} \\" + "\n"
        latex += r"\extracode \tablegrid \end{tikztimingtable} \end{center}" + "\n"
        return latex

    def get_footer(self) -> str:
        return r"\end{document}"

    # --- Helpers de Dibujo (Privados) ---
    def _draw_mux(self):
        return r"""\draw[thick] (0,0) -- (0,8) -- (4,6) -- (4,2) -- (0,0) -- cycle;
                   \node at (2,4) {\textbf{MUX 16:1}};
                   \foreach \y in {0.5,1,...,7.5} \draw (-0.5,\y) -- (0,\y);
                   \draw (3.5, -0.5) -- (3.5, 2.8); \node[below] at (3.5,-0.5) {$\overline{E}$};
                   \draw (4,4) -- (5,4) node[right]{Y};"""

    def _draw_comparator(self, params):
        code = r"""\draw[thick] (0,0) rectangle (4,4);
                   \node at (2,3.5) {\textbf{COMPARADOR}}; \node at (2,0.5) {\textbf{4 BITS}};
                   \draw[ultra thick] (-1.2, 3) -- (0,3); \node[left] at (-1.2, 3) {A}; \node[above] at (-0.6, 3.1) {\scriptsize 4}; \draw[thick] (-0.7, 2.8) -- (-0.5, 3.2);
                   \draw[ultra thick] (-1.2, 1) -- (0,1); \node[left] at (-1.2, 1) {B}; \node[above] at (-0.6, 1.1) {\scriptsize 4}; \draw[thick] (-0.7, 0.8) -- (-0.5, 1.2);
                   \draw (4,3) -- (5,3) node[right]{$>$}; \draw (4,2) -- (5,2) node[right]{$=$}; \draw (4,1) -- (5,1) node[right]{$<$};"""
        # Entradas cascada
        vals = params['cascada']
        code += fr"\draw (-1, 2.4) -- (0, 2.4); \node[left] at (-1, 2.4) {{\small $I_{{gr}}={vals[0]}$}};"
        code += fr"\draw (-1, 2.0) -- (0, 2.0); \node[left] at (-1, 2.0) {{\small $I_{{eq}}={vals[1]}$}};"
        code += fr"\draw (-1, 1.6) -- (0, 1.6); \node[left] at (-1, 1.6) {{\small $I_{{le}}={vals[2]}$}};"
        return code

    def _draw_adder(self, params):
        return fr"""\draw[thick] (0,0) rectangle (4,4);
                    \node at (2,2) {{\textbf{{SUMADOR 4 BITS}}}};
                    \draw (-1,3) -- (0,3) node[midway, above]{{A}}; \draw (-1,1) -- (0,1) node[midway, above]{{B}};
                    \draw (2,4) -- (2,5) node[above]{{Cin={params['Cin']}}};
                    \draw (4,2.5) -- (5,2.5) node[right]{{S}}; \draw (4,1.5) -- (5,1.5) node[right]{{Cout}};"""

    def _draw_sequential_circuit(self, data: Exercise5Data) -> str:
        # Aquí va la lógica de Circuitikz que ya perfeccionamos (ff1, ff2, clocks, logic, async)
        # Por brevedad en esta respuesta, inserto el núcleo lógico:
        ff = data.ff_type
        clk_dot = ", dot on clock" if data.edge_type == "Bajada" else ""

        code = fr"(0,0) node[flipflop {ff}{clk_dot}, external pins width=0](FF1){{Q0}} (5,0) node[flipflop {ff}{clk_dot}, external pins width=0](FF2){{Q1}}"
        code += r"; \draw (FF1.pin 2) -- ++(-1.5,0) -- ++(0,-2.5) coordinate(clk_bus); \draw (FF2.pin 2) -- ++(-1.5,0) -- ++(0,-2.5) -- (clk_bus); \draw (clk_bus) -- ++(-1.0,0) node[left]{CLK};"

        if data.logic_type == 'SHIFT':
            code += r"\draw (FF1.pin 1) -- ++(-1,0) node[left]{E}; \draw (FF1.pin 6) -- (FF2.pin 1); \draw (FF1.pin 6) -- ++(0.5,0) -- ++(0,1.5) node[above]{Q0}; \draw (FF2.pin 6) -- ++(0.5,0) -- ++(0,1.5) node[above]{Q1};"
        else: # COUNTER
            if ff == 'JK':
                code += r"\draw (FF1.pin 1) -- ++(-0.5,0) coordinate(j1) -- ++(-0.5,0) node[left]{E}; \draw (FF1.pin 3) -- ++(-0.5,0) -- (j1); \draw (FF1.pin 6) -- ++(0.5,0) coordinate(q0) -- (FF2.pin 1); \draw (q0) -- ++(0,-0.5) -- ++(1.5,0) -- (FF2.pin 3);"
            elif ff == 'T':
                code += r"\draw (FF1.pin 1) -- ++(-1,0) node[left]{E}; \draw (FF1.pin 6) -- (FF2.pin 1);"
            code += r"\draw (FF1.pin 6) -- ++(0,1.5) node[above]{Q0}; \draw (FF2.pin 6) -- ++(0,1.5) node[above]{Q1};"

        if data.has_async:
            pin = "up" if data.async_type in ['Set', 'Preset'] else "down"
            y_dir = "0.5" if pin == "up" else "-0.5"
            code += fr"\draw (FF1.{pin}) -- ++(0,{y_dir}) coordinate(a); \draw (FF2.{pin}) -- ++(0,{y_dir}) -- (a); \draw (a) -- ++(0,{y_dir}) node[above]{{{data.async_type}}};"

        return code

    def _render_truth_table(self, headers, out, vals):
        n = len(headers)
        cols = "|" + "c|" * (n + 1)
        tex = fr"\begin{{table}}[H] \centering \begin{{tabular}}{{{cols}}} \hline" + "\n"
        tex += r"\rowcolor[gray]{0.9} " + " & ".join([fr"\textbf{{{h}}}" for h in headers]) + fr" & \textbf{{{out}}} \\ \hline" + "\n"
        for i in range(2**n):
            b = format(i, f'0{n}b')
            row_vals = " & ".join(list(b))
            out_val = fr"\textbf{{{vals[i]}}}" if vals else " "
            tex += fr"{row_vals} & {out_val} \\ \hline" + "\n"
        tex += r"\end{tabular} \end{table}" + "\n"
        return tex

    def _render_kmap_template(self, label_izq, label_sup, label_out, show_trap=True, empty_headers=False):
        # (Aquí iría la lógica completa de la función gen_latex_mapa_karnaugh que ya tenemos optimizada)
        # Por brevedad, asumo que usas la versión final de la conversación anterior.
        return r"% KMAP TEMPLATE PLACEHOLDER"