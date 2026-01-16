# 📚 Generador de Ejercicios de Electrónica Digital

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![LaTeX](https://img.shields.io/badge/LaTeX-PDF-red?logo=latex&logoColor=white)](https://www.latex-project.org/)
[![Status](https://img.shields.io/badge/Status-Actively%20Developed-green)](https://github.com)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

Una **plataforma modular y extensible** para generar ejercicios de electrónica digital con documentación técnica completa. Cubre sistemas de numeración, códigos binarios, lógica combinacional y secuencial.

---

## 🎯 Características Principales

- ✅ **Documentación Exhaustiva**: 2550+ líneas de teoría técnica
- ✅ **45+ Ejemplos Prácticos**: Ejercicios resueltos paso a paso
- ✅ **Validación Matemática**: Todas las propiedades probadas
- ✅ **Generación Automática**: PDF profesionales y documentos editables
- ✅ **Modular y Extensible**: Diseño basado en plugins

---

## 📖 Documentación Disponible

### 🔢 Sección 2.1.1: Números Sin Signo

Representación de números positivos en distintas bases.

| Sistema | Documentación | Demo | Descripción |
|---------|---------------|------|-------------|
| **Base B** | [2.1.1.1](docs/SECCION_2_1_1_1_BASE_B.md) | `demo_base_b.py` | Representación generalizada |
| **Conversiones** | [2.1.1.2](docs/SECCION_2_1_1_2_CONVERSIONES.md) | `demo_conversiones.py` | Entre bases (B₁ ↔ B₂) |
| **Eficiencia** | [2.1.1.3](docs/SECCION_2_1_1_3_EFICIENCIA.md) | Análisis | Bits necesarios por dígito |
| **Rango y Capacidad** | [2.1.1.4](docs/SECCION_2_1_1_4_RANGO.md) | `demo_rango.py` | Valores máximos representables |
| **Fraccionarios** | [2.1.1.5](docs/SECCION_2_1_1_5_FRACCIONARIOS.md) | `demo_fracciones.py` | Números con parte decimal |
| **Operaciones** | [2.1.1.6](docs/SECCION_2_1_1_6_OPERACIONES.md) | `demo_operaciones.py` | Suma, resta, multiplicación |

**Comando rápido:**

```bash
python demo_base_b.py
python demo_conversiones.py
```

---

### 🔐 Sección 2.1.1.7: Números Enteros con Signo

Cuatro sistemas estándar para representar números positivos y negativos.

| Sistema | Documentación | Demo | Rango | Uso |
|---------|---------------|------|-------|-----|
| **Magnitud y Signo** | [MS](docs/SECCION_2_1_1_7_MS.md) | `demo_ms_simple.py` | ±(2ⁿ⁻¹-1) | Histórico |
| **Complemento a (B-1)** | [CB-1](docs/SECCION_2_1_1_7_CB_MENOS_1.md) | `demo_cb1.py` | ±(2ⁿ⁻¹-1) | Histórico |
| **Complemento a Base** | [CB (Two's))](docs/SECCION_2_1_1_7_CB.md) | `demo_cb.py` | ±2ⁿ⁻¹ | ⭐ Estándar actual |
| **Exceso a K** | [Exc-K](docs/SECCION_2_1_1_7_EXCESO_K.md) | `demo_exceso_k.py` | [0, 2ⁿ) | IEEE 754 exponentes |

**Tabla comparativa:**

```bash
python generar_tabla_comparativa.py
```

---

### 📦 Sección 2.1.2: Códigos BCD (Binary Coded Decimal)

| Código | Documentación | Validación | Bits | Directo | Status |
|--------|---------------|-----------|------|---------|--------|
| **BCD Natural (8421)** | [Doc](docs/SECCION_2_1_2_BCD_NATURAL.md) | ✅ | 4 | ✅ Sí | ✅ Completo |
| **BCD Exceso-3** | [Doc](docs/SECCION_2_1_2_EXCESO_3.md) | ✅ | 4 | ✅ Sí* | ✅ Completo |
| **BCD Aiken (2421)** | [Doc](docs/SECCION_2_1_2_AIKEN.md) | ✅ | 4 | ✅ Sí* | ✅ Completo |

**Nota:** *Comparación directa válida con ajustes (ver documentación)

**Ejecución:**

```bash
python demo_bcd_validacion.py
```

---

### 🔄 Sección 2.1.3-2.1.4: Códigos Especializados

| Código | Documentación | Bits | Regla | Demo |
|--------|---------------|------|-------|------|
| **Johnson** | [Doc](docs/SECCION_2_1_3_JOHNSON.md) | 5 | Max 1 transición | `demo_johnson.py` |
| **Biquinario** | [Doc](docs/SECCION_2_1_4_BIQUINARIO.md) | 7 | Exactamente 2 bits | `demo_biquinario.py` |

**Validación integrada:**

```bash
python demo_validacion_johnson_biquinario.py
```

**Funciones de validación:**

```python
from core.sistemas_numeracion_basicos import is_johnson_valid, is_biquinario_valid

is_johnson_valid(0b00111)      # → True
is_biquinario_valid(0b1010010) # → True
```

Ver: [FUNCIONES_VALIDACION_JOHNSON_BIQUINARIO.md](docs/FUNCIONES_VALIDACION_JOHNSON_BIQUINARIO.md)

---

### ➗ Sección 2.1.5: Punto Fijo (Fixed-Point)

Representación Q(E, F): **E bits enteros, F bits fraccionarios**

| Aspecto | Documentación | Descripción |
|--------|---------------|-------------|
| **Formato Q** | [Doc](docs/SECCION_2_1_5_PUNTO_FIJO.md) | Q(8,8), Q(16,16), etc. |
| **Conversión de Bases** | [Doc](docs/SECCION_2_1_5_PUNTO_FIJO.md#conversión) | Regla: B'ᶠ' ≥ Bᶠ |
| **Análisis de Errores** | [Doc](docs/SECCION_2_1_5_PUNTO_FIJO.md#errores) | Error absoluto, relativo |
| **Operaciones** | [Doc](docs/SECCION_2_1_5_PUNTO_FIJO.md#operaciones) | Suma, resta, multiplicación |

**Ejemplo: Conversión Base Doble**

```
Q(4,4) base 2 → Q(2,4) base 10
Regla: 10⁴ = 10000 ≥ 2⁴ = 16 ✓
```

---

### 🔬 Sección 2.1.6: Punto Flotante (Floating-Point)

Formato generalizado: **V = M × B^E**

| Aspecto | Documentación | Descripción |
|--------|---------------|-------------|
| **Formato** | [Doc](docs/SECCION_2_1_6_PUNTO_FLOTANTE.md) | Variable M y E |
| **IEEE 754** | [Doc](docs/SECCION_2_1_6_PUNTO_FLOTANTE.md#ieee-754) | Simple (32), Double (64), Extended (80) |
| **Números Especiales** | [Doc](docs/SECCION_2_1_6_PUNTO_FLOTANTE.md#especiales) | ±0, ±∞, NaN, denormalizados |
| **Normalización** | [Doc](docs/SECCION_2_1_6_PUNTO_FLOTANTE.md#normalización) | **Crítico post-operación** |

**Comparativa Punto Fijo vs Flotante:**

```bash
Ver: COMPARATIVA_PUNTO_FIJO_VS_FLOTANTE.md
- Tabla de decisión (7 criterios)
- Análisis de errores
- Casos de uso (procesamiento de imágenes, integración numérica)
```

**Índice y Guía de Aprendizaje:**

```bash
Ver: INDICE_SECCIONES_2_1_5_2_1_6.md
- Orden de lectura recomendado
- Temas especiales resaltados
- 10+ preguntas de autoevaluación
```

---

## 📊 Estadísticas de la Documentación

| Métrica | Valor |
|---------|-------|
| **Líneas de documentación** | 2550+ |
| **Archivos de documentación** | 15+ |
| **Ejemplos prácticos** | 45+ |
| **Fórmulas matemáticas** | 50+ |
| **Tablas comparativas** | 20+ |
| **Scripts de demostración** | 18+ |

---

## 🏗️ Estructura del Proyecto

```
GeneratorFEExercises/
├── docs/                          # 📄 Documentación técnica
│   ├── SECCION_2_1_1_*.md        # Números sin signo (6 archivos)
│   ├── SECCION_2_1_1_7_*.md      # Números con signo (4 archivos)
│   ├── SECCION_2_1_2_*.md        # Códigos BCD (3 archivos)
│   ├── SECCION_2_1_3_JOHNSON.md
│   ├── SECCION_2_1_4_BIQUINARIO.md
│   ├── SECCION_2_1_5_PUNTO_FIJO.md
│   ├── SECCION_2_1_6_PUNTO_FLOTANTE.md
│   ├── COMPARATIVA_PUNTO_FIJO_VS_FLOTANTE.md
│   └── INDICE_SECCIONES_2_1_5_2_1_6.md
├── demo_*.py                      # 🎬 Scripts de demostración
├── core/                          # 🔧 Código central
│   ├── sistemas_numeracion_basicos.py
│   ├── enteros_signados.py
│   ├── exceso_k_representacion.py
│   ├── generator_base.py
│   └── catalog.py
├── modules/                       # 📦 Ejercicios por tema
│   ├── numeracion/
│   ├── combinacional/
│   └── secuencial/
├── renderers/                     # 🎨 Generadores de PDF/DOCX
│   ├── latex/
│   └── docx/
└── config/                        # ⚙️ Configuración

```

---

## 🚀 Instalación y Uso Rápido

### Instalación

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/GeneratorFEExercises.git
cd GeneratorFEExercises

# Instalar dependencias
pip install -r requirements.txt
```

### Ejecución de Demostraciones

```bash
# Números sin signo
python demo_base_b.py
python demo_conversiones.py

# Números con signo
python demo_ms_simple.py
python demo_cb.py
python demo_exceso_k.py
python generar_tabla_comparativa.py

# Códigos especiales
python demo_bcd_validacion.py
python demo_validacion_johnson_biquinario.py
```

---

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Pasos:

1. **Fork** el repositorio
2. Crea una rama: `git checkout -b feature/tu-feature`
3. Realiza cambios y commitea: `git commit -m "feat: descripción clara"`
4. **Push**: `git push origin feature/tu-feature`
5. Abre un **Pull Request**

### Áreas de Contribución

- 📝 Adicionar más ejemplos prácticos
- 🐛 Reportar bugs encontrados
- 📚 Expandir secciones de documentación
- 🔬 Crear demostraciones interactivas
- 🧪 Agregar pruebas unitarias

---

## 📋 Roadmap

- [ ] Implementar calculadora de conversión de bases (UI web)
- [ ] Crear simulador interactivo IEEE 754
- [ ] Agregar pruebas unitarias automatizadas
- [ ] Integración con GitHub Codespaces
- [ ] Documentación en inglés

---

## 📄 Licencia

Este proyecto está bajo licencia **MIT**. Ver [LICENSE](LICENSE) para más detalles.

---

## 📧 Contacto y Soporte

- 📝 **Issues**: [Reportar problemas](https://github.com/tu-usuario/GeneratorFEExercises/issues)
- 💬 **Discussions**: [Preguntas y sugerencias](https://github.com/tu-usuario/GeneratorFEExercises/discussions)

---

**Última actualización:** 2024 | **Versión:** 2.0
