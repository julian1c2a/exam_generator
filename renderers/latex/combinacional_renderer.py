from modules.combinacional.models import KarnaughExerciseData, LogicProblemExerciseData, MSIExerciseData
from renderers.latex.utils.truth_table import TruthTableRenderer
from renderers.latex.utils.karnaugh import KarnaughMapRenderer
from renderers.latex.utils.circuit import DigitalCircuitRenderer

class CombinacionalLatexRenderer:
    def __init__(self):
        self.tt_renderer = TruthTableRenderer()
        self.kmap_renderer = KarnaughMapRenderer()
        self.circuit_renderer = DigitalCircuitRenderer()

    def render(self, data: object, index: int) -> str:
        if isinstance(data, KarnaughExerciseData):
            return self._render_karnaugh(data, index)
        elif isinstance(data, LogicProblemExerciseData):
            return self._render_problem(data, index)
        elif isinstance(data, MSIExerciseData):
            return self._render_msi(data, index)
        return ""

    def _render_karnaugh(self, data: KarnaughExerciseData, index: int) -> str:
        latex = fr"\newpage \section*{{Ejercicio {index}: {data.title}}}" + "\n"
        latex += r"\begin{tcolorbox}[title=Enunciado]" + "\n"
        latex += fr"\noindent {data.description}" + "\n"

        latex += self.tt_renderer.render(data.vars_name, data.out_name, data.truth_table_outputs)

        latex += r"\noindent Se pide:" + "\n"
        latex += r"\begin{enumerate}[label=\alph*)]" + "\n"
        latex += fr"\item Obtener la expresión canónica ({data.canon_type})." + "\n"
        latex += r"\item Simplificar por Karnaugh." + "\n"
        latex += fr"\item Implementar con puertas \textbf{{{data.gate_type}}}." + "\n"
        latex += r"\end{enumerate} \end{tcolorbox}" + "\n"

        latex += r"\textbf{Espacio de Resolución:}" + "\n"
        vars_left = "".join(data.vars_name[:2])
        vars_top = "".join(data.vars_name[2:])
        latex += self.kmap_renderer.render_template(vars_left, vars_top, data.out_name)
        latex += r"\vspace{3cm}" + "\n"
        return latex

    def _render_problem(self, data: LogicProblemExerciseData, index: int) -> str:
        latex = fr"\newpage \section*{{Ejercicio {index}: {data.title}}}" + "\n"
        latex += r"\begin{tcolorbox}[title=Enunciado]" + "\n"
        latex += fr"\textbf{{Contexto: {data.context_title}}}" + "\n"
        latex += r"\begin{itemize}" + "\n"
        for v in data.variables_desc: latex += fr"\item {v}" + "\n"
        latex += fr"\item Salida: {data.output_desc}" + "\n"
        latex += r"\end{itemize}" + "\n"
        latex += fr"\textit{{Lógica: {data.logic_description}}}" + "\n"
        latex += r"\end{tcolorbox}" + "\n"

        latex += r"\textbf{1. Tabla de Verdad:}" + "\n"
        latex += self.tt_renderer.render(data.vars_clean, data.out_clean, None)
        
        latex += r"\newpage \textbf{2. Mapa de Karnaugh:}" + "\n"
        l_izq = "".join(data.vars_clean[:2])
        l_sup = "".join(data.vars_clean[2:])
        latex += self.kmap_renderer.render_template(l_izq, l_sup, data.out_clean)
        
        latex += r"\vspace{1cm}" + "\n"
        latex += r"\noindent \textbf{3. Esquema Lógico:}" + "\n"
        latex += r"\vspace{4cm}" + "\n"
        return latex

    def _render_msi(self, data: MSIExerciseData, index: int) -> str:
        latex = fr"\newpage \section*{{Ejercicio {index}: {data.title}}}" + "\n"
        latex += r"\begin{tcolorbox}[title=Enunciado]" + "\n"
        latex += fr"{data.description}" + "\n"
        
        if data.block_type == 'MUX':
            latex += self.circuit_renderer.render_mux()
        elif data.block_type == 'COMPARADOR':
            latex += self.circuit_renderer.render_comparator(data.params)
        elif data.block_type == 'SUMADOR':
            latex += self.circuit_renderer.render_adder(data.params)

        if data.block_type == 'MUX':
            latex += fr"Entradas I0-I15: {data.params['inputs']} \\ Determine Y para:" + "\n"
            latex += r"\begin{enumerate}" + "\n"
            for case in data.params['cases']:
                latex += fr"\item Enable={case['ena']}, Dir={case['addr']:04b}" + "\n"
            latex += r"\end{enumerate}" + "\n"
        elif data.block_type == 'COMPARADOR':
            latex += r"\noindent Determine las salidas ($>, =, <$) para las entradas indicadas." + "\n"
        elif data.block_type == 'SUMADOR':
            latex += r"\noindent Determine la salida S y el acarreo de salida Cout." + "\n"

        latex += r"\end{tcolorbox} \vspace{5cm}" + "\n"
        return latex
