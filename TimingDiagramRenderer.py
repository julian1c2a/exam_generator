from ExamDataModel import Exercise5Data

class TimingDiagramRenderer:
    def render(self, data: Exercise5Data) -> str:
        # Usamos resizebox para asegurar que el cronograma se ajuste al ancho de la página.
        # arraystretch=0 para eliminar el espaciado vertical de la tabla, dejando solo la altura de la señal.
        
        latex = r"\begin{center}" + "\n"
        latex += r"\resizebox{\textwidth}{!}{%" + "\n"
        latex += r"\renewcommand{\arraystretch}{0}" + "\n" # Cero espacio extra entre filas
        latex += r"\begin{tikztimingtable}[timing/slope=0, x=2.0cm, y=1.0cm]" + "\n" # y=1.0 para buena altura
        
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
