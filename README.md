# Generador de Ejercicios de Electrónica (V2)

Este proyecto es la evolución del generador de exámenes, diseñado para ser una plataforma extensible y modular ("Base de Datos de Ejercicios").

## Arquitectura

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

## Cómo añadir un nuevo ejercicio

1.  Crear una nueva clase en `modules/<tema>/generators.py` que herede de `ExerciseGenerator`.
2.  Implementar el método `generate()` para crear los datos aleatorios.
3.  Registrar la clase en `core/catalog.py`.
4.  Añadir el renderizado correspondiente en `renderers/`.

## Instalación

```bash
pip install -r requirements.txt
```

## Uso

```bash
python main.py --config config/parcial_1.json
```

---

## ?? Documentación de Números Enteros Signados

Se ha implementado una documentación completa sobre **Sección 2.1.1.7: Números Enteros con Signo**, cobriendo 4 sistemas de representación:

### 1. Magnitud y Signo (M&S)
- Documentación: SECCION_2_1_1_7_MS.md
- Código: core/enteros_signados.py
- Demo: python demo_ms_simple.py
- ? Completo y probado

### 2. Complemento a la Base Menos 1 (CB-1)
- Documentación: SECCION_2_1_1_7_CB_MENOS_1.md
- Código: core/enteros_signados.py
- Demo: python demo_cb1.py
- ? Completo y probado

### 3. Complemento a la Base (CB) - Two's Complement
- Documentación: SECCION_2_1_1_7_CB.md
- Código: core/enteros_signados.py
- Demo: python demo_cb.py
- ESTÁNDAR: Usado en todos los procesadores
- ? Completo y probado

### 4. Exceso a K (Biased Representation)
- Documentación: SECCION_2_1_1_7_EXCESO_K.md
- Código: core/exceso_k_representacion.py
- Demo: python demo_exceso_k.py
- ESTÁNDAR: Usado en IEEE 754 para exponentes
- ? Completo y probado

### Tablas Comparativas
Ejecutar: python generar_tabla_comparativa.py
Genera un análisis visual de todas las representaciones.
