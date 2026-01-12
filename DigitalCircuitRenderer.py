from ExamDataModel import Exercise5Data

class DigitalCircuitRenderer:
    def render_mux(self) -> str:
        return r"""
\begin{center} \begin{tikzpicture}
    \draw[thick] (0,0) -- (0,8) -- (4,6) -- (4,2) -- (0,0) -- cycle;
    \node at (2,4) {\textbf{MUX 16:1}};
    \foreach \y in {0.5,1,...,7.5} \draw (-0.5,\y) -- (0,\y);
    \draw (3.5, -0.5) -- (3.5, 2.8); \node[below] at (3.5,-0.5) {$\overline{E}$};
    \draw (4,4) -- (5,4) node[right]{Y};
    \node[left] at (-0.5, 7.5) {I0};
    \node[left] at (-0.5, 0.5) {I15};
\end{tikzpicture} \end{center}
"""

    def render_comparator(self, params: dict) -> str:
        vals = params['cascada']
        return fr"""
\begin{{center}} \begin{{tikzpicture}}
    \draw[thick] (0,0) rectangle (4,4);
    \node at (2,3.5) {{\textbf{{COMPARADOR}}}}; \node at (2,0.5) {{\textbf{{4 BITS}}}};
    
    % Entradas A y B
    \draw[ultra thick] (-1.2, 3) -- (0,3); \node[left] at (-1.2, 3) {{A}}; 
    \node[above] at (-0.6, 3.1) {{\scriptsize 4}}; \draw[thick] (-0.7, 2.8) -- (-0.5, 3.2);
    
    \draw[ultra thick] (-1.2, 1) -- (0,1); \node[left] at (-1.2, 1) {{B}}; 
    \node[above] at (-0.6, 1.1) {{\scriptsize 4}}; \draw[thick] (-0.7, 0.8) -- (-0.5, 1.2);
    
    % Salidas
    \draw (4,3) -- (5,3) node[right]{{$>$}}; 
    \draw (4,2) -- (5,2) node[right]{{$=$}}; 
    \draw (4,1) -- (5,1) node[right]{{$<$}};
    
    % Entradas de cascada
    \draw (-1, 2.4) -- (0, 2.4); \node[left] at (-1, 2.4) {{\small $I_{{gr}}={vals[0]}$}};
    \draw (-1, 2.0) -- (0, 2.0); \node[left] at (-1, 2.0) {{\small $I_{{eq}}={vals[1]}$}};
    \draw (-1, 1.6) -- (0, 1.6); \node[left] at (-1, 1.6) {{\small $I_{{le}}={vals[2]}$}};
\end{{tikzpicture}} \end{{center}}
"""

    def render_adder(self, params: dict) -> str:
        return fr"""
\begin{{center}} \begin{{tikzpicture}}
    \draw[thick] (0,0) rectangle (4,4);
    \node at (2,2) {{\textbf{{SUMADOR 4 BITS}}}};
    \draw (-1,3) -- (0,3) node[midway, above]{{A}}; 
    \draw (-1,1) -- (0,1) node[midway, above]{{B}};
    \draw (2,4) -- (2,5) node[above]{{Cin={params['Cin']}}};
    \draw (4,2.5) -- (5,2.5) node[right]{{S}}; 
    \draw (4,1.5) -- (5,1.5) node[right]{{Cout}};
\end{{tikzpicture}} \end{{center}}
"""

    def render_sequential_circuit(self, data: Exercise5Data) -> str:
        ff = data.ff_type
        clk_dot = ", dot on clock" if data.edge_type == "Bajada" else ""
        
        code = r"\begin{center} \begin{circuitikz}[scale=1.2, transform shape] \draw" + "\n"
        
        # Flip Flops
        code += fr"(0,0) node[flipflop {ff}{clk_dot}, external pins width=0](FF1){{Q0}} "
        code += fr"(5,0) node[flipflop {ff}{clk_dot}, external pins width=0](FF2){{Q1}};" + "\n"
        
        # Clock Bus
        code += r"\draw (FF1.pin 2) -- ++(-1.5,0) -- ++(0,-2.5) coordinate(clk_bus);" + "\n"
        code += r"\draw (FF2.pin 2) -- ++(-1.5,0) -- ++(0,-2.5) -- (clk_bus);" + "\n"
        code += r"\draw (clk_bus) -- ++(-1.0,0) node[left]{CLK};" + "\n"

        # Lógica específica (Shift vs Counter)
        if data.logic_type == 'SHIFT':
            code += r"\draw (FF1.pin 1) -- ++(-1,0) node[left]{E};" + "\n"
            code += r"\draw (FF1.pin 6) -- (FF2.pin 1);" + "\n"
        else: # COUNTER
            if ff == 'JK':
                code += r"\draw (FF1.pin 1) -- ++(-0.5,0) coordinate(j1) -- ++(-0.5,0) node[left]{E};" + "\n"
                code += r"\draw (FF1.pin 3) -- ++(-0.5,0) -- (j1);" + "\n"
                code += r"\draw (FF1.pin 6) -- ++(0.5,0) coordinate(q0) -- (FF2.pin 1);" + "\n"
                code += r"\draw (q0) -- ++(0,-0.5) -- ++(1.5,0) -- (FF2.pin 3);" + "\n"
            elif ff == 'T':
                code += r"\draw (FF1.pin 1) -- ++(-1,0) node[left]{E};" + "\n"
                code += r"\draw (FF1.pin 6) -- (FF2.pin 1);" + "\n"
        
        # Salidas Q
        code += r"\draw (FF1.pin 6) -- ++(0,1.5) node[above]{Q0};" + "\n"
        code += r"\draw (FF2.pin 6) -- ++(0,1.5) node[above]{Q1};" + "\n"

        # Asíncrono
        if data.has_async:
            pin = "up" if data.async_type in ['Set', 'Preset'] else "down"
            y_dir = "0.5" if pin == "up" else "-0.5"
            code += fr"\draw (FF1.{pin}) -- ++(0,{y_dir}) coordinate(a);" + "\n"
            code += fr"\draw (FF2.{pin}) -- ++(0,{y_dir}) -- (a);" + "\n"
            code += fr"\draw (a) -- ++(0,{y_dir}) node[above]{{{data.async_type}}};" + "\n"

        code += r"\end{circuitikz} \end{center}"
        return code
