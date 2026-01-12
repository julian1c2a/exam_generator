from modules.secuencial.models import SequentialExerciseData

class TimingDiagramRenderer:
    def render(self, data: SequentialExerciseData) -> str:
        # Usamos resizebox para asegurar que el cronograma se ajuste al ancho de la página.
        # y=0.35cm: Altura validada por el usuario.
        # arraystretch=0: Eliminar espaciado extra.
        
        latex = r"\begin{center}" + "\n"
        latex += r"\resizebox{\textwidth}{!}{%" + "\n"
        latex += r"\renewcommand{\arraystretch}{0}" + "\n"
        latex += r"\begin{tikztimingtable}[timing/slope=0, x=2.0cm, y=0.35cm]" + "\n"
        
        # Clock
        latex += fr"CLK\hspace{{1em}} & {data.clk_sequence} \\" + "\n"
        
        # Async signal (si existe)
        if data.has_async:
            latex += fr"{data.async_type}(asyn)\hspace{{1em}} & {data.async_sequence} \\" + "\n"
            
        # Input signal
        latex += fr"E\hspace{{2.5em}} & {data.input_sequence} \\" + "\n"
        
        # Output placeholders
        latex += fr"Q0 & [draw=none, fill=none] {data.output_placeholder} \\" + "\n"
        latex += fr"Q1 & [draw=none, fill=none] {data.output_placeholder} \\" + "\n"
        
        latex += r"\extracode \tablegrid \end{tikztimingtable}%" + "\n"
        latex += r"}" + "\n" # Cierre de resizebox
        latex += r"\end{center}" + "\n"
        return latex
