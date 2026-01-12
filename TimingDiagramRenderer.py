from ExamDataModel import Exercise5Data

class TimingDiagramRenderer:
    def render(self, data: Exercise5Data) -> str:
        latex = r"\begin{center} \begin{tikztimingtable}[timing/slope=0, x=2.0cm, y=0.8cm]" + "\n"
        
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
        
        latex += r"\extracode \tablegrid \end{tikztimingtable} \end{center}" + "\n"
        return latex
