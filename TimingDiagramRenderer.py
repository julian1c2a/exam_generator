from ExamDataModel import Exercise5Data

class TimingDiagramRenderer:
    def render(self, data: Exercise5Data) -> str:
        # Usamos resizebox para asegurar que el cronograma se ajuste al ancho de la página
        # independientemente de la cantidad de ciclos.
        
        # Ajustes de estilo:
        # y=1.5cm: Aumenta la altura de las señales
        # timing/slope=0: Flancos verticales perfectos
        # Eliminado 'row dist' que causaba error.
        # Usamos \\[-1ex] para reducir el espacio entre filas manualmente.
        
        latex = r"\begin{center}" + "\n"
        latex += r"\resizebox{\textwidth}{!}{%" + "\n"
        latex += r"\begin{tikztimingtable}[timing/slope=0, x=2.0cm, y=1.5cm]" + "\n"
        
        # Clock
        latex += fr"CLK\hspace{{1em}} & {data.clk_sequence} \\[-1ex]" + "\n"
        
        # Async signal (si existe)
        if data.has_async:
            latex += fr"{data.async_type}(asyn)\hspace{{1em}} & {data.async_sequence} \\[-1ex]" + "\n"
            
        # Input signal
        latex += fr"E\hspace{{2.5em}} & {data.input_sequence} \\[-1ex]" + "\n"
        
        # Output placeholders
        latex += fr"Q0 & [draw=none, fill=none] {data.output_placeholder} \\[-1ex]" + "\n"
        latex += fr"Q1 & [draw=none, fill=none] {data.output_placeholder} \\" + "\n"
        
        latex += r"\extracode \tablegrid \end{tikztimingtable}%" + "\n"
        latex += r"}" + "\n" # Cierre de resizebox
        latex += r"\end{center}" + "\n"
        return latex
