# Generador de Exámenes de Electrónica (V2)

Este proyecto es la evolución del generador de exámenes, diseñado para ser una plataforma extensible y modular ("Base de Datos de Ejercicios").

## 🚀 Arquitectura

El sistema se basa en un diseño modular donde cada tipo de ejercicio es un plugin independiente.

### Estructura de Directorios

*   **`core/`**: Núcleo del sistema.
    *   `generator_base.py`: Clase abstracta para todos los generadores.
    *   `exam_builder.py`: Construye el examen leyendo un "blueprint" (JSON).
    *   `catalog.py`: Registro central de todos los ejercicios disponibles.
*   **`modules/`**: Implementación de los ejercicios, organizados por tema.
    *   `numeracion/`: Conversiones, IEEE 754, Códigos.
    *   `combinacional/`: Boole, Karnaugh, MUX, Decoders.
    *   `secuencial/`: Flip-Flops, Contadores, FSM, Cronogramas.
*   **`renderers/`**: Motores de generación de documentos.
    *   `latex/`: Generación de PDF profesional.
    *   `docx/`: Generación de Word editable.
*   **`config/`**: Archivos de configuración.
    *   `exam_blueprint.json`: Define qué ejercicios entran en un examen específico.

## 🛠 Cómo añadir un nuevo ejercicio

1.  Crear una nueva clase en `modules/<tema>/generators.py` que herede de `ExerciseGenerator`.
2.  Implementar el método `generate()` para crear los datos aleatorios.
3.  Registrar la clase en `core/catalog.py`.
4.  Añadir el renderizado correspondiente en `renderers/`.

## 📦 Instalación

```bash
pip install -r requirements.txt
```

## 📝 Uso

```bash
python main.py --config config/parcial_1.json
```
