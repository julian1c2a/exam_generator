# Guía de Depuración de Imágenes LaTeX

Este proyecto utiliza un sistema de **Gestión de Recursos (Asset Manager)** que permite separar la generación automática de diagramas (TikZ, Circuitikz) de su corrección manual.

## 🔄 Flujo de Trabajo

Cuando ejecutas `main_v2.py`, el sistema sigue estos pasos para cada diagrama (Mapas de Karnaugh, Circuitos, Cronogramas):

1.  **Busca un recurso fijo**: Verifica si existe un archivo `.tex` corregido manualmente en `resources/latex/`.
2.  **Si existe**: Lo utiliza directamente (`\input{../../resources/latex/archivo.tex}`).
3.  **Si NO existe**:
    *   Genera el código LaTeX dinámicamente desde Python.
    *   Guarda ese código en un archivo "borrador" en `build/latex/components/`.
    *   Utiliza ese borrador en el examen (`\input{components/archivo.tex}`).

## 🛠 Cómo Corregir una Imagen Mal Generada

Si un diagrama (por ejemplo, el cronograma del Ejercicio 5) no se ve bien:

1.  **Identifica el archivo generado**:
    *   Ve a la carpeta `build/latex/components/`.
    *   Busca el archivo correspondiente (ej: `ej5_seq_timing.tex`). El nombre suele ser descriptivo (`ej{numero}_{tipo}.tex`).

2.  **Copia a Recursos**:
    *   Copia ese archivo `.tex` a la carpeta `resources/latex/`.

3.  **Edita Manualmente**:
    *   Abre el archivo en `resources/latex/ej5_seq_timing.tex` con tu editor de texto o IDE LaTeX favorito.
    *   Modifica el código TikZ/LaTeX hasta que se vea como quieres.
    *   *Tip:* Puedes crear un pequeño archivo `test.tex` temporal que incluya ese componente para compilarlo y verlo rápido sin generar todo el examen.

4.  **Regenera el Examen**:
    *   Ejecuta `python main_v2.py` de nuevo.
    *   El sistema detectará tu archivo en `resources/latex/` y lo usará en lugar de generar uno nuevo.
    *   Verás en el log o en el archivo `.tex` final un comentario como: `% [RECURSO FIJO DETECTADO: ej5_seq_timing.tex]`.

## 📂 Estructura de Archivos

*   `build/latex/Examen_V2.tex`: Archivo principal del examen.
*   `build/latex/components/`: **Borradores**. Se sobrescriben cada vez que ejecutas el script (si no hay recurso fijo). **NO EDITAR AQUÍ**.
*   `resources/latex/`: **Definitivos**. Archivos corregidos manualmente. Git debe rastrear esta carpeta.

## 💡 Ejemplo Práctico

**Problema:** El cable del reloj en el Flip-Flop JK atraviesa el componente.

1.  Ejecuto el script. Veo el error en el PDF.
2.  Voy a `build/latex/components/ej5_seq_circuit.tex`.
3.  Lo copio a `resources/latex/ej5_seq_circuit.tex`.
4.  Edito `resources/latex/ej5_seq_circuit.tex`:
    *   Cambio `\draw (FF1.pin 2) -- ...` por `\draw (FF1.clk) -- ...`.
5.  Ejecuto el script.
6.  El PDF final ahora usa mi versión corregida.
