from modules.secuencial.models import SequentialExerciseData
from renderers.latex.utils.circuit import DigitalCircuitRenderer
from renderers.latex.utils.timing import TimingDiagramRenderer

class SecuencialLatexRenderer:
    def __init__(self):
        self.circuit_renderer = DigitalCircuitRenderer()
        self.timing_renderer = TimingDiagramRenderer()

    def render(self, data: SequentialExerciseData, index: int) -> str:
        latex = fr"\newpage \section*{{Ejercicio {index}: {data.title}}}" + "\n"
        
        edge_txt = "Subida" if data.edge_type == "Subida" else "Bajada"
        async_txt = f"Async \\textbf{{{data.async_type}(asyn)}} a nivel {data.async_level}" if data.has_async else "Sin Async"

        latex += r"\begin{tcolorbox}[title=Enunciado]" + "\n"
        latex += fr"Síncrono ({data.logic_type}) por {edge_txt}. FF {data.ff_type}. {async_txt}." + "\n"

        # Circuito
        latex += self.circuit_renderer.render_sequential_circuit(data)
        latex += r"\end{tcolorbox}" + "\n"

        # Cronograma
        latex += self.timing_renderer.render(data)
        
        latex += r"\vspace{0.5cm}" + "\n"
        latex += r"\noindent \textbf{Se pide:}" + "\n"
        latex += r"\begin{enumerate}[label=\alph*)]" + "\n"
        latex += r"\item Completar el cronograma (salidas Q0, Q1)." + "\n"
        latex += r"\item Determinar la secuencia de estados." + "\n"
        latex += r"\end{enumerate}" + "\n"
        
        return latex
