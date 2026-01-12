class KarnaughMapRenderer:
    def render_template(self, vars_left: str, vars_top: str, output_label: str) -> str:
        """
        Genera una plantilla de Mapa de Karnaugh vacía para 4 variables (2 izq, 2 sup).
        """
        # Asumimos mapa de 4 variables estándar (4x4)
        return fr"""
\begin{{center}}
\begin{{tikzpicture}}
    % Configuración base
    \draw (0,0) grid (4,4);
    \draw (0,4) -- (1,5);
    
    % Etiquetas de variables
    \node at (0.3, 4.6) {{{vars_left}}};
    \node at (0.8, 4.2) {{{vars_top}}};
    
    % Códigos Gray (Izquierda)
    \node[left] at (0, 3.5) {{00}};
    \node[left] at (0, 2.5) {{01}};
    \node[left] at (0, 1.5) {{11}};
    \node[left] at (0, 0.5) {{10}};
    
    % Códigos Gray (Superior)
    \node[above] at (0.5, 4) {{00}};
    \node[above] at (1.5, 4) {{01}};
    \node[above] at (2.5, 4) {{11}};
    \node[above] at (3.5, 4) {{10}};
    
    % Título opcional
    \node[above] at (2, 5) {{\textbf{{Mapa K para }} ${output_label}$}};
    
\end{{tikzpicture}}
\end{{center}}
"""
