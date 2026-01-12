# Generador de Exámenes de Fundamentos de Electrónica

Este proyecto es una herramienta automatizada para generar exámenes de electrónica digital aleatorios, produciendo salidas tanto en formato **LaTeX (PDF)** de alta calidad tipográfica como en **Word (.docx)** editable.

## 🏗 Arquitectura del Proyecto

El sistema sigue una arquitectura modular basada en **Modelo-Vista-Controlador (MVC)** simplificado:

1.  **Modelo (`ExamDataModel.py`)**:
    *   Define las estructuras de datos (DTOs) utilizando `dataclasses`.
    *   No contiene lógica, solo la definición de qué datos constituyen un ejercicio.

2.  **Controlador (`ExamGenerator.py`)**:
    *   Contiene toda la **lógica de negocio** y algoritmos de aleatorización.
    *   Es la **única fuente de verdad**: genera los datos una sola vez y los entrega a las vistas.
    *   Carga escenarios de problemas desde `scenarios.json`.

3.  **Vistas (Renderizadores)**:
    *   **`LatexRenderer.py`**: Orquesta la generación del archivo `.tex`. Delega tareas complejas a sub-renderizadores:
        *   `TruthTableRenderer.py`: Tablas de verdad dinámicas.
        *   `KarnaughMapRenderer.py`: Mapas de Karnaugh (estilo tabla didáctica con doble numeración).
        *   `DigitalCircuitRenderer.py`: Circuitos digitales (MUX, Sumadores, Flip-Flops) usando `circuitikz`.
        *   `TimingDiagramRenderer.py`: Cronogramas compactos usando `tikz-timing`.
    *   **`DocxRenderer.py`**: Genera la versión en Word utilizando `python-docx`.

4.  **Orquestador (`Main.py`)**:
    *   Punto de entrada del script.
    *   Instancia el generador, obtiene los datos y llama a ambos renderizadores para asegurar que el PDF y el DOCX sean idénticos en contenido.

## ⚙️ Configuración

El comportamiento del generador se personaliza a través de archivos JSON externos, sin necesidad de tocar el código:

*   **`header_config.json`**: Datos institucionales (Universidad, Asignatura, Profesores, Fecha, Logo).
*   **`scoring_config.json`**: Puntuación asignada a cada ejercicio.
*   **`scenarios.json`**: Banco de enunciados para los problemas de diseño lógico (Ejercicio 3).

## 📝 Reglas de Estilo y Formato

### LaTeX
*   **Paquetes**: Se utiliza `circuitikz` para circuitos, `tikz-timing` para cronogramas, `fancyhdr` para encabezados profesionales y `diagbox` para tablas.
*   **Tablas**: Las tablas de conversión numérica usan columnas de ancho fijo (`C{2.8cm}`) para mantener la uniformidad.
*   **Cronogramas**: Se generan compactos (`y=0.35cm`, `arraystretch=0`) y se ajustan automáticamente al ancho de la página (`resizebox`).
*   **Circuitos**:
    *   **MUX**: Trapecio con entradas de selección (S0-S3) en la base inferior.
    *   **Sumador**: Entradas y salidas representadas como buses de 4 bits. Cin ubicado abajo a la izquierda.
    *   **Flip-Flops**: Dibujo manual del círculo de negación en el reloj para máxima compatibilidad.

### Word
*   Se intenta replicar la estructura del LaTeX lo más fielmente posible utilizando tablas para la maquetación.

## 🚀 Uso

1.  Asegúrate de tener las dependencias instaladas (`python-docx`).
2.  Coloca tu logo en la raíz del proyecto (configura el nombre en `header_config.json`).
3.  Ejecuta el script principal:
    ```bash
    python Main.py
    ```
4.  Se generarán `Examen_Final.tex` y `Examen_Final.docx`.

## 🛡 Manejo de Errores
*   Si el archivo de salida (`.docx`) está abierto y bloqueado por Word, el script lo detecta y guarda automáticamente una copia con un nombre aleatorio (ej: `Examen_Copia_123.docx`) para no interrumpir el flujo de trabajo.
