from modules.secuencial.models import SequentialExerciseData

class TimingDiagramRenderer:
    def render(self, data: SequentialExerciseData) -> str:
        # Formateo limpio y legible del código LaTeX generado
        
        sep = r"\hspace{1ex}"
        
        # Construcción de filas
        rows = []
        rows.append(fr"            CLK{sep} & {data.clk_sequence} \\")
        
        if data.has_async:
            rows.append(fr"            {data.async_type}(asyn){sep} & {data.async_sequence} \\")
            
        rows.append(fr"            E{sep} & {data.input_sequence} \\")
        rows.append(fr"            Q0{sep} & [draw=none, fill=none] {data.output_placeholder} \\")
        rows.append(fr"            Q1{sep} & [draw=none, fill=none] {data.output_placeholder} \\")
        
        rows_str = "\n".join(rows)

        return fr"""
\begin{{center}}
    \resizebox{{\textwidth}}{{!}}{{%
        \renewcommand{{\arraystretch}}{{0}}
        \begin{{tikztimingtable}}[timing/slope=0, x=2.0cm, y=0.35cm]
{rows_str}
            \extracode
            \tablegrid
        \end{{tikztimingtable}}%
    }}
\end{{center}}
"""
