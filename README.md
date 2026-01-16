# Generador de Ex谩menes de Electr贸nica (V2)

Este proyecto es la evoluci贸n del generador de ex谩menes, dise帽ado para ser una plataforma extensible y modular ("Base de Datos de Ejercicios").

## 馃殌 Arquitectura

El sistema se basa en un dise帽o modular donde cada tipo de ejercicio es un plugin independiente.

### Estructura de Directorios

*   **`core/`**: N煤cleo del sistema.
    *   `generator_base.py`: Clase abstracta para todos los generadores.
    *   `exam_builder.py`: Construye el examen leyendo un "blueprint" (JSON).
    *   `catalog.py`: Registro central de todos los ejercicios disponibles.
*   **`modules/`**: Implementaci贸n de los ejercicios, organizados por tema.
    *   `numeracion/`: Conversiones, IEEE 754, C贸digos.
    *   `combinacional/`: Boole, Karnaugh, MUX, Decoders.
    *   `secuencial/`: Flip-Flops, Contadores, FSM, Cronogramas.
*   **`renderers/`**: Motores de generaci贸n de documentos.
    *   `latex/`: Generaci贸n de PDF profesional.
    *   `docx/`: Generaci贸n de Word editable.
*   **`config/`**: Archivos de configuraci贸n.
    *   `exam_blueprint.json`: Define qu茅 ejercicios entran en un examen espec铆fico.

## 馃洜 C贸mo a帽adir un nuevo ejercicio

1.  Crear una nueva clase en `modules/<tema>/generators.py` que herede de `ExerciseGenerator`.
2.  Implementar el m茅todo `generate()` para crear los datos aleatorios.
3.  Registrar la clase en `core/catalog.py`.
4.  A帽adir el renderizado correspondiente en `renderers/`.

## 馃摝 Instalaci贸n

```bash
pip install -r requirements.txt
```

## 馃摑 Uso

```bash
python main.py --config config/parcial_1.json
```

---

## ?? Documentaci髇 de N鷐eros Enteros Signados

Se ha implementado una documentaci髇 completa sobre **Secci髇 2.1.1.7: N鷐eros Enteros con Signo**, cobriendo 4 sistemas de representaci髇:

### 1. Magnitud y Signo (M&S)
- Documentaci髇: SECCION_2_1_1_7_MS.md
- C骴igo: core/enteros_signados.py
- Demo: python demo_ms_simple.py
- ? Completo y probado

### 2. Complemento a la Base Menos 1 (CB-1)
- Documentaci髇: SECCION_2_1_1_7_CB_MENOS_1.md
- C骴igo: core/enteros_signados.py
- Demo: python demo_cb1.py
- ? Completo y probado

### 3. Complemento a la Base (CB) - Two's Complement
- Documentaci髇: SECCION_2_1_1_7_CB.md
- C骴igo: core/enteros_signados.py
- Demo: python demo_cb.py
- EST罭DAR: Usado en todos los procesadores
- ? Completo y probado

### 4. Exceso a K (Biased Representation)
- Documentaci髇: SECCION_2_1_1_7_EXCESO_K.md
- C骴igo: core/exceso_k_representacion.py
- Demo: python demo_exceso_k.py
- EST罭DAR: Usado en IEEE 754 para exponentes
- ? Completo y probado

### Tablas Comparativas
Ejecutar: python generar_tabla_comparativa.py
Genera un an醠isis visual de todas las representaciones.
