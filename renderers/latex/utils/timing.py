from modules.secuencial.models import SequentialExerciseData

class TimingDiagramRenderer:
    def render(self, data: SequentialExerciseData) -> str:
        # Formateo para coincidir con el estilo manual de candidate.tex
        
        sep = r"\hspace{1ex}"
        
        # Construcción de filas
        rows = []
        
        # Línea 8: Añade la señal de RELOJ (CLK) con su secuencia generada (ej: 24{C})
        rows.append(fr"\t\t\tCLK{sep} & {data.clk_sequence} \\")
        
        if data.has_async:
            # Línea 10: Si hay señal asíncrona (Set/Reset), la añade (ej: 2L 22H)
            rows.append(fr"\t\t\t{data.async_type}(asyn){sep} & {data.async_sequence} \\")
            
        # Línea 12: Añade la señal de entrada (E) con su secuencia aleatoria (ej: HLLH...)
        rows.append(fr"\t\t\tE{sep} & {data.input_sequence} \\")
        
        # Línea 13: Añade el placeholder para la salida Q0 (espacio vacío para que el alumno dibuje)
        rows.append(fr"\t\t\tQ0{sep} & [draw=none, fill=none] {data.output_placeholder} \\")
        
        # Línea 14: Añade el placeholder para la salida Q1
        rows.append(fr"\t\t\tQ1{sep} & [draw=none, fill=none] {data.output_placeholder} \\")
        
        rows_str = "\n".join(rows)

        return fr"""\begin{{center}}
	\resizebox{{\textwidth}}{{!}}{{%
		\renewcommand{{\arraystretch}}{{0}}
		\begin{{tikztimingtable}}[timing/slope=0, x=2.0cm, y=0.35cm]
{rows_str}
			\extracode \tablegrid
		\end{{tikztimingtable}}%
	}}
\end{{center}}
"""
