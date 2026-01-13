from modules.secuencial.models import SequentialExerciseData

class TimingDiagramRenderer:
    def render(self, data: SequentialExerciseData) -> str:
        
        # Construcción de filas
        rows = []
        rows.append(fr"\t\tCLK & {data.clk_sequence} \\")
        
        if data.has_async:
            rows.append(fr"\t\t{data.async_type}(asyn) & {data.async_sequence} \\")
            
        rows.append(fr"\t\tE & {data.input_sequence} \\")
        rows.append(fr"\t\tQ0 & [draw=none, fill=none] {data.output_placeholder} \\")
        rows.append(fr"\t\tQ1 & [draw=none, fill=none] {data.output_placeholder} \\")
        
        rows_str = "\n".join(rows)

        return fr"""\begin{{flushleft}}
	% arraystretch=0 elimina el padding proporcional.
	\renewcommand{{\arraystretch}}{{0}}
	% extrarowheight negativo elimina altura fija extra.
	\setlength{{\extrarowheight}}{{0pt}}
	
	\begin{{tikztimingtable}}[
		timing/slope=0,
		timing/xunit=0.60cm,
		timing/yunit=0.35cm,
		timing/coldist=2pt
	]
{rows_str}
		\extracode \tablegrid
	\end{{tikztimingtable}}
\end{{flushleft}}
"""
