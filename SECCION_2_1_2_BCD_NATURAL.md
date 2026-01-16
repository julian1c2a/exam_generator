# Sección 2.1.2 - BCD Natural (Binary Coded Decimal - 8421)

**Representación Decimal mediante Dígitos Binarios**

---

## 📌 Concepto Fundamental

### Definición

**BCD Natural** (Binary Coded Decimal) es un sistema de **codificación de dígitos decimales** donde cada dígito decimal (0-9) se representa mediante su equivalente binario de **4 bits**, conservando el sistema de pesos **8-4-2-1**.

### Estructura

```
Número decimal: 5 7 3
                | | |
Codificación:   | | └─→ 3 = 0011
                | └─────→ 7 = 0111
                └────────→ 5 = 0101
                
Representación BCD Natural: 0101 0111 0011 (sin espacios: 010101110011)
```

### Características Clave

| Propiedad | Valor |
|-----------|-------|
| **Bits por dígito** | 4 |
| **Valores representables** | 0-9 (10 valores) |
| **Valores no usados** | 6 valores (1010-1111) |
| **Eficacia** | 10/16 = 62.5% |
| **Sistema de pesos** | SÍ (8-4-2-1) |
| **Autocomplementario** | NO |

---

## 🔢 Tabla de Correspondencia

| Decimal | BCD Natural | Decimal | BCD Natural |
|---------|------------|---------|------------|
| 0 | 0000 | 5 | 0101 |
| 1 | 0001 | 6 | 0110 |
| 2 | 0010 | 7 | 0111 |
| 3 | 0011 | 8 | 1000 |
| 4 | 0100 | 9 | 1001 |
| **Valores no usados** | **1010-1111** | | |

---

## 🎯 Operaciones Fundamentales

### 1. Conversión de Número Decimal a BCD Natural

**Proceso:**

1. Separar el número en sus dígitos individuales
2. Convertir cada dígito a su representación BCD de 4 bits
3. Concatenar los códigos

**Ejemplo: 427 → BCD Natural**

```
4 → 0100
2 → 0010
7 → 0111

Resultado: 0100 0010 0111
```

**Ejemplo: 9305 → BCD Natural**

```
9 → 1001
3 → 0011
0 → 0000
5 → 0101

Resultado: 1001 0011 0000 0101
```

### 2. Conversión de BCD Natural a Número Decimal

**Proceso:**

1. Dividir el código binario en grupos de 4 bits
2. Convertir cada grupo a su equivalente decimal
3. Concatenar los dígitos

**Ejemplo: 0110 1001 0010 → Decimal**

```
0110 → 6
1001 → 9
0010 → 2

Resultado: 692
```

**Ejemplo: 1000 0000 0011 → Decimal**

```
1000 → 8
0000 → 0
0011 → 3

Resultado: 803
```

### 3. Comparación Directa

En BCD Natural es **posible comparar directamente** los códigos binarios sin conversión:

```
Comparar: 257 vs 349

BCD Natural de 257: 0010 0101 0111
BCD Natural de 349: 0011 0100 1001

Comparación binaria:
0010... < 0011...  →  257 < 349 ✓
```

---

## 📦 Empaquetado y Eficacia

### Eficacia de Empaquetado

**BCD Natural desperdicia bits** porque solo usa 10 de 16 combinaciones posibles:

$$\text{Eficacia} = \frac{\text{valores representables}}{\text{combinaciones posibles}} = \frac{10}{16} = 62.5\%$$

### Comparativa: Números Naturales vs BCD Natural

| Cantidad | Números Naturales | BCD Natural | Diferencia |
|----------|------------------|------------|-----------|
| 1 dígito (0-9) | 4 bits | 4 bits | Igual |
| 2 dígitos (0-99) | 7 bits | 8 bits | +1 bit |
| 3 dígitos (0-999) | 10 bits | 12 bits | +2 bits |
| 4 dígitos (0-9999) | 14 bits | 16 bits | +2 bits |
| 5 dígitos (0-99999) | 17 bits | 20 bits | +3 bits |

**Conclusión:** Números naturales en base 2 son más eficaces, pero BCD Natural:

- Facilita conversión a/desde decimal (especialmente en sistemas con entrada/salida decimal)
- Permite operaciones directas sin conversión base 10 → base 2
- Es ideal para sistemas que trabajan nativamente en decimal

---

## ➕➖ Suma en BCD Natural

### Suma Directa (con corrección)

La suma de dos números en BCD Natural **no siempre produce un resultado BCD válido** sin corrección.

**Problema: Desbordamiento de dígito**

Cuando el resultado de sumar dos dígitos BCD excede 9, es necesaria una **corrección**:

$$\text{Si suma} > 9 \text{: suma} = \text{suma} + 6 \text{ y propagar acarreo}$$

#### Ejemplo 1: Suma sin desbordamiento

```
  0101 (5)     
+ 0011 (3)     
-------
  1000 (8)  ✓ Resultado BCD válido
```

#### Ejemplo 2: Suma con desbordamiento (mismo dígito)

```
  0111 (7)
+ 0110 (6)
-------
  1101 (13 en binario, pero ≠ 3 en BCD)

Corrección: 1101 + 0110 = 10011
Interpretación: 1 (acarreo) y 0011 (3) → Resultado = 13 ✓
```

#### Ejemplo 3: Suma de números BCD de múltiples dígitos

```
Suma: 0101 0111 + 0011 0110 (57 + 36)

Dígitos:     5 7
           + 3 6
           -----

Paso 1 - Sumar dígitos en paralelo:
  0111 (7)     0101 (5)
+ 0110 (6)   + 0011 (3)
-------      -------
  1101 (>9)    1000 (8)

Paso 2 - Corregir dígito de 7+6=13:
  1101 + 0110 = 10011 → Genera acarreo

Paso 3 - Considerar acarreo en siguiente dígito:
  1000 (8) + 0001 (acarreo) = 1001 (9)

Resultado: 1001 0011 (93) ✓
```

---

## 📊 Rango y Capacidad

### Rango de Representación

Con $n$ dígitos BCD (donde cada dígito = 4 bits, total = $4n$ bits):

- **Rango:** [0, $10^n - 1$]
- **Ejemplo con 3 dígitos (12 bits):** [0, 999]
- **Ejemplo con 4 dígitos (16 bits):** [0, 9999]

### Tabla de Capacidad

| Bits | Dígitos | Rango | Números Naturales (mismo rango) |
|------|---------|-------|--------------------------------|
| 4 | 1 | 0-9 | 0-15 (4.17 dígitos) |
| 8 | 2 | 0-99 | 0-255 (2.4 dígitos) |
| 12 | 3 | 0-999 | 0-4095 (3.6 dígitos) |
| 16 | 4 | 0-9999 | 0-65535 (5 dígitos) |
| 20 | 5 | 0-99999 | 0-1048575 (6.3 dígitos) |

---

## 💡 Ventajas y Desventajas

### ✅ Ventajas

1. **Conversión inmediata a decimal:** Cada grupo de 4 bits es directamente legible
2. **Compatibilidad con sistemas decimales:** Entrada/salida sin conversión compleja
3. **Comparación directa:** Los números se pueden comparar bit a bit
4. **Intuitivo:** Fácil de entender y debuggear
5. **Sin ambigüedad:** No hay dos representaciones para el mismo número

### ❌ Desventajas

1. **Baja eficacia:** Solo 62.5% de combinaciones se usan
2. **Suma compleja:** Requiere corrección cuando el resultado excede 9
3. **Multiplicación compleja:** No es trivial multiplicar números BCD
4. **Menos compacto:** Usa ~20% más bits que números binarios naturales
5. **Costo de hardware:** Lógica adicional para correcciones aritméticas

---

## 🎓 Comparación con Otros Sistemas

| Aspecto | Naturales Binarios | BCD Natural | Exceso-3 | Aiken |
|--------|------------------|------------|----------|--------|
| Eficacia | 100% | 62.5% | 62.5% | 62.5% |
| Pesos | 1,2,4,8 | 8,4,2,1 | - | 2,4,2,1 |
| Autocomplementario | NO | NO | **SÍ** | **SÍ** |
| Suma simple | **SÍ** | NO | NO | NO |
| Comparación directa | **SÍ** | **SÍ** | SÍ | **SÍ** |
| Uso industrial | NÚMEROS | ENTRADA/SALIDA | HISTÓRICO | HISTÓRICO |

---

## 📍 Casos Especiales

### 1. El cero en BCD

```
0 en BCD Natural: 0000
(Sin ambigüedad, un único cero)
```

### 2. Números con dígitos cero

```
507 en BCD: 0101 0000 0111
         (5)  (0)  (7)
```

### 3. Números muy grandes

```
1234567890 en BCD requiere 40 bits:
0001 0010 0011 0100 0101 0110 0111 1000 1001 0000
  1    2    3    4    5    6    7    8    9    0
```

---

## 🔗 Relaciones con Otros Sistemas

### BCD Natural vs Números Naturales Binarios

```
Número: 42

Binarios naturales:  101010  (6 bits)
BCD Natural:        0100 0010  (8 bits)

Binarios: 42 decimal = 32 + 8 + 2 = 2^5 + 2^3 + 2^1 = 101010
BCD: Cada dígito (4, 2) se codifica independientemente
```

### BCD Natural como Base para Otros Códigos

- **Exceso-3:** Suma 3 a cada dígito BCD y codifica el resultado
- **Aiken:** Usa pesos 2-4-2-1 para crear autocomplementariedad

---

## 🎯 Aplicaciones Prácticas

### Sistemas que Utilizan BCD Natural

1. **Calculadoras antiguas:** Almacenamiento interno de números decimales
2. **Contadores digitales:** Displays de 7 segmentos
3. **Sistemas de punto de venta (POS):** Valores monetarios
4. **Ábaco digital:** Representación directa de decimales
5. **Interfaces USB/Serial:** Codificación de datos decimales

### Ejemplos de Uso

**Ejemplo 1: Código postal representado en BCD**

```
Código: 28001 (Madrid)

2    8    0    0    1
0010 1000 0000 0000 0001

Ventaja: Fácil separar dígitos, cada uno es autoexplicativo
```

**Ejemplo 2: Fecha en BCD**

```
Fecha: 16-01-2026

16: 0001 0110
01: 0000 0001
2026: 0010 0000 0010 0110

Legible en hexadecimal: 16, 01, 20, 26
```

---

## 📝 Resumen

| Característica | Valor |
|---|---|
| **Nombre** | BCD Natural (8421) |
| **Propósito** | Codificar dígitos decimales en binario |
| **Bits por dígito** | 4 |
| **Rango por dígito** | 0-9 |
| **Eficacia** | 62.5% (10/16) |
| **Tiene pesos** | SÍ (8,4,2,1) |
| **Autocomplementario** | NO |
| **Suma** | Requiere corrección |
| **Comparación** | Directa |
| **Uso industrial** | Entrada/salida decimal |

---

## 🔄 Siguientes Sistemas

Una vez dominado **BCD Natural**, exploraremos sus variantes especializadas:

1. **[BCD Exceso-3](SECCION_2_1_2_BCD_EXC3.md)** - Sistema autocomplementario sin pesos
2. **[BCD Aiken (2-4-2-1)](SECCION_2_1_2_BCD_AIKEN.md)** - Sistema autocomplementario con pesos
3. Comparativa de los tres sistemas BCD

---

**Conceptos Previos Necesarios:**

- Sistemas de numeración en diferentes bases
- Conversión entre bases
- Representación binaria de números

**Conceptos Relacionados:**

- Códigos cíclicos (Gray)
- Códigos de corrección de errores (Hamming)
- IEEE 754 (usa M&S para mantisa)
