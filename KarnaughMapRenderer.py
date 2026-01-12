from typing import List, Optional

class KarnaughMapRenderer:
    def render_template(self, vars_left: str, vars_top: str, output_label: str, values: Optional[List[int]] = None) -> str:
        """
        Genera un Mapa de Karnaugh didáctico con doble numeración (Natural y Gray) para que el alumno elija.
        Replica el estilo de tabla 7x7 del examen original.
        """
        
        # Mapeo de índices para 4 variables (Gray Code)
        # Filas (AB): 00(0), 01(1), 11(3), 10(2)
        # Cols (CD): 00(0), 01(1), 11(3), 10(2)
        
        # Matriz de índices de la tabla de verdad
        map_indices = [
            [0,  1,  3,  2],   # AB=00
            [4,  5,  7,  6],   # AB=01
            [12, 13, 15, 14],  # AB=11
            [8,  9,  11, 10]   # AB=10
        ]
        
        # Preparar contenido de las celdas
        rows_content = []
        
        # Etiquetas de filas: Binario Natural vs Gray
        # El alumno debe usar la columna Gray (00, 01, 11, 10)
        row_labels_natural = ["00", "01", "10", "11"]
        row_labels_gray    = ["00", "01", "11", "10"]
        
        for i in range(4): # 4 filas de datos
            row_cells = []
            for j in range(4): # 4 columnas de datos
                idx = map_indices[i][j]
                val = ""
                if values and idx < len(values):
                    val = fr"\textbf{{{values[idx]}}}"
                row_cells.append(val)
            
            # Construir la fila:
            # Col 1 (Natural) & Col 2 (Gray) & Val1 & Val2 & Val3 & Val4
            row_str = fr" & {row_labels_natural[i]} & {row_labels_gray[i]} & " + " & ".join(row_cells) + r" \\ \cline{2-7}"
            rows_content.append(row_str)

        # Construcción de la tabla compleja
        latex = r"\begin{center}" + "\n"
        latex += r"\begin{table}[H] \centering \renewcommand{\arraystretch}{2}" + "\n"
        latex += r"\begin{tabular}{|c|c|c|c|c|c|c|} \hline" + "\n"
        
        # Cabecera compleja
        # Fila 1: Variable Salida (F) y Variable Superior (CD)
        latex += fr"\multicolumn{{3}}{{|c|}}{{\multirow{{3}}*{{\Huge \textbf{{{output_label}}}}}}} & \multicolumn{{4}}{{c|}}{{\textbf{{{vars_top} =}}}} \\ \cline{{4-7}}" + "\n"
        
        # Fila 2: Numeración Natural (Incorrecta para K-Map, trampa)
        latex += r"\multicolumn{3}{|c|}{} & 00 & 01 & 10 & 11 \\ \cline{4-7}" + "\n"
        
        # Fila 3: Numeración Gray (Correcta)
        latex += r"\multicolumn{3}{|c|}{} & 00 & 01 & 11 & 10 \\ \hline" + "\n"
        
        # Filas de datos con etiqueta lateral rotada
        # La primera fila lleva el multirow de la etiqueta lateral
        first_row = rows_content[0]
        # Reemplazamos el primer "&" por la etiqueta rotada
        latex += fr"\multirow{{4}}*{{\rotatebox{{90}}{{\textbf{{{vars_left} =}}}}}}" + first_row + "\n"
        
        # Resto de filas
        for row in rows_content[1:]:
            latex += row + "\n"
            
        latex += r"\hline" + "\n"
        latex += r"\end{tabular} \end{table}" + "\n"
        latex += r"\end{center}" + "\n"
        
        return latex
