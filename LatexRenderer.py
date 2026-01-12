import json
import os
from typing import List, Optional
from exam_model import *
from TruthTableRenderer import TruthTableRenderer
from KarnaughMapRenderer import KarnaughMapRenderer
from DigitalCircuitRenderer import DigitalCircuitRenderer
from TimingDiagramRenderer import TimingDiagramRenderer

class LatexRenderer:
    def __init__(self):
        self.truth_table_renderer = TruthTableRenderer()
        self.kmap_renderer = KarnaughMapRenderer()
        self.circuit_renderer = DigitalCircuitRenderer()
        self.timing_renderer = TimingDiagramRenderer()
        
        # Cargar configuraciones
        self.header_config = self._load_json('header_config.json')
        self.scoring_config = self._load_json('scoring_config.json')

    def _load_json(self, filename: str) -> dict:
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def _get_score_text(self, key: str) -> str:
        if self.scoring_config.get("show_score_in_title", False):
            points = self.scoring_config.get(key, 0)
            return fr" \hfill \textbf{{[{points} ptos]}}"
        return ""

    def get_preamble(self) -> str:
        h = self.header_config
        
        # Construcción del encabezado dinámico
        header_latex = r"\begin{center}" + "\n"
        if h.get("university"):
            header_latex += fr"{{\Large \textbf{{{h['university']}}}}} \\" + "\n"
        if h.get("department"):
            header_latex += fr"{{\large {h['department']}}} \\" + "\n"
        header_latex += r"\vspace{0.2cm}" + "\n"
        if h.get("subject"):
            header_latex += fr"{{\Huge \textbf{{{h['subject']}}}}} \\" + "\n"
        if h.get("exam_title"):
            header_latex += fr"{{\Large \textbf{{{h['exam_title']}}}}} \\" + "\n"
        if h.get("term"):
            header_latex += fr"\textit{{{h['term']}}} \\" + "\n"
        if h.get("professors"):
            header_latex += fr"\vspace{{0.1cm}} {{\small {h['professors']}}}" + "\n"
        header_latex += r"\end{center}"

        return fr"""\documentclass[a4paper,11pt]{{article}}
\usepackage[utf8]{{inputenc}}
\usepackage[spanish]{{babel}}
\usepackage[top=2cm, bottom=2cm, left=2cm, right=2cm]{{geometry}}
\usepackage{{tikz}}
\usepackage{{circuitikz}}
\usepackage{{tikz-timing}}
\usepackage{{amsmath}}
\usepackage{{amssymb}}
\usepackage{{array}}
\usepackage{{multirow}}
\usepackage{{colortbl}}
\usepackage{{enumitem}}
\usepackage{{float}}
\usepackage{{tcolorbox}}
\usepackage{{graphicx}} % Para logos si fuera necesario
\usetikzlibrary{{calc}}
\tcbset{{colback=gray!5!white, colframe=gray!75!black, title=\textbf{{ENUNCIADO}}, fonttitle=\bfseries, boxrule=0.5mm, arc=2mm}}

\begin{{document}}

{header_latex}

\vspace{{0.5cm}}
\noindent \textbf{{Apellido y Nombre:}} ............................................................................ \hfill \textbf{{Grupo:}} ....................
\vspace{{0.5cm}} \hrule \vspace{{0.5cm}}
"""

    def render_ej1(self, data: Exercise1Data) -> str:
        score = self._get_score_text("ej1")
        latex = fr"\section*{{Ejercicio 1: Sistemas de Representación ({data.n_bits} bits){score}}}" + "\n"
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
        score = self._get_score_text("ej2")
        latex = fr"\newpage \section*{{Ejercicio 2: Diseño y Simplificación Lógica{score}}}" + "\n"
        latex += r"\begin{tcolorbox}[title=Enunciado]" + "\n"
        latex += r"\noindent Dada la función definida por:" + "\n"

        # Delegar a TruthTableRenderer
        latex += self.truth_table_renderer.render(['A','B','C','D'], 'F', data.truth_table_outputs)

        latex += r"\noindent Se pide:" + "\n"
        latex += r"\begin{enumerate}[label=\alph*)]" + "\n"
        latex += fr"\item Obtener la expresión canónica ({data.canon_type})." + "\n"
        latex += r"\item Simplificar por Karnaugh." + "\n"
        latex += fr"\item Implementar con puertas \textbf{{{data.gate_type}}}." + "\n"
        latex += r"\end{enumerate} \end{tcolorbox}" + "\n"

        latex += r"\textbf{Espacio de Resolución:}" + "\n"
        # Delegar a KarnaughMapRenderer
        latex += self.kmap_renderer.render_template("AB", "CD", "F")
        latex += r"\vspace{3cm} \hrule" + "\n"
        return latex

    def render_ej3(self, data: Exercise3Data) -> str:
        score = self._get_score_text("ej3")
        latex = fr"\newpage \section*{{Ejercicio 3: Problema de Diseño Lógico{score}}}" + "\n"
        latex += r"\begin{tcolorbox}[title=Enunciado]" + "\n"
        latex += fr"\textbf{{Contexto: {data.title}}}" + "\n"
        latex += r"\begin{itemize}" + "\n"
        for v in data.variables: latex += fr"\item {v}" + "\n"
        latex += fr"\item Salida: {data.output_name}" + "\n"
        latex += r"\end{itemize}" + "\n"
        latex += fr"\textit{{Lógica: {data.logic_description}}}" + "\n"
        latex += r"\end{tcolorbox}" + "\n"

        latex += r"\textbf{1. Tabla de Verdad:}" + "\n"
        latex += self.truth_table_renderer.render(data.var_names_clean, data.out_name_clean, None)
        
        latex += r"\newpage \textbf{2. Mapa de Karnaugh:}" + "\n"
        l_izq = "".join(data.var_names_clean[:2])
        l_sup = "".join(data.var_names_clean[2:])
        latex += self.kmap_renderer.render_template(l_izq, l_sup, data.out_name_clean)
        return latex

    def render_ej4(self, data: Exercise4Data) -> str:
        score = self._get_score_text("ej4")
        latex = fr"\newpage \section*{{Ejercicio 4: Bloques MSI{score}}}" + "\n"
        latex += r"\begin{tcolorbox}[title=Enunciado]" + "\n"
        latex += fr"Dado el componente: \textbf{{{data.block_type}}}" + "\n"
        
        # Delegar a DigitalCircuitRenderer
        if data.block_type == 'MUX':
            latex += self.circuit_renderer.render_mux()
        elif data.block_type == 'COMPARADOR':
            latex += self.circuit_renderer.render_comparator(data.params)
        elif data.block_type == 'SUMADOR':
            latex += self.circuit_renderer.render_adder(data.params)

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
        score = self._get_score_text("ej5")
        latex = fr"\newpage \section*{{Ejercicio 5: Secuenciales{score}}}" + "\n"
        edge_txt = "Subida" if data.edge_type == "Subida" else "Bajada"
        async_txt = f"Async \\textbf{{{data.async_type}(asyn)}} a nivel {data.async_level}" if data.has_async else "Sin Async"

        latex += r"\begin{tcolorbox}[title=Enunciado]" + "\n"
        latex += fr"Síncrono ({data.logic_type}) por {edge_txt}. FF {data.ff_type}. {async_txt}." + "\n"

        # Delegar Circuito
        latex += self.circuit_renderer.render_sequential_circuit(data)
        latex += r"\end{tcolorbox}" + "\n"

        # Delegar Cronograma
        latex += self.timing_renderer.render(data)
        return latex

    def get_footer(self) -> str:
        return r"\end{document}"
