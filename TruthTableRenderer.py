from typing import List, Optional

class TruthTableRenderer:
    def render(self, headers: List[str], output_label: str, output_values: Optional[List[int]]) -> str:
        """
        Genera una tabla de verdad en LaTeX.
        :param headers: Lista de nombres de las variables de entrada (ej: ['A', 'B', 'C']).
        :param output_label: Nombre de la variable de salida (ej: 'F').
        :param output_values: Lista de valores de salida (0 o 1). Si es None, la columna de salida queda vacía.
        """
        n_vars = len(headers)
        n_rows = 2 ** n_vars
        
        # Definición de columnas: |c|c|...|c|
        cols_format = "|" + "c|" * (n_vars + 1)
        
        latex = fr"\begin{{table}}[H] \centering \renewcommand{{\arraystretch}}{{1.2}}" + "\n"
        latex += fr"\begin{{tabular}}{{{cols_format}}} \hline" + "\n"
        
        # Cabecera con color de fondo
        header_cells = [fr"\textbf{{{h}}}" for h in headers] + [fr"\textbf{{{output_label}}}"]
        latex += r"\rowcolor[gray]{0.9} " + " & ".join(header_cells) + r" \\ \hline" + "\n"
        
        # Filas
        for i in range(n_rows):
            # Generar combinación binaria para las entradas
            bin_str = format(i, f'0{n_vars}b')
            input_cells = list(bin_str)
            
            # Valor de salida
            if output_values and i < len(output_values):
                out_val = fr"\textbf{{{output_values[i]}}}"
            else:
                out_val = " " # Espacio vacío para completar
            
            row_cells = input_cells + [out_val]
            latex += " & ".join(row_cells) + r" \\ \hline" + "\n"
            
        latex += r"\end{tabular} \end{table}" + "\n"
        return latex
