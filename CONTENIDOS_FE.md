# 📚 Temario de Fundamentos de Electrónica

---

## 1️⃣ Introducción a la Electrónica

### 1.1 Conceptos Básicos

- Magnitudes fundamentales
- Ley de Ohm
- Potencia eléctrica

### 1.2 Componentes Electrónicos

- Resistencias
- Condensadores
- Bobinas
- Semiconductores

---

## 2️⃣ Electrónica Digital

### 2.1 Sistemas de Representación de la Información

#### 2.1.1 Sistemas de Numeración

##### 2.1.1.1 Sistemas Posicionales y No Posicionales

###### Definiciones

Un **sistema de numeración** es un conjunto de reglas y símbolos utilizados para representar cantidades numéricas.

- **Sistemas No Posicionales**: El valor de cada símbolo es INDEPENDIENTE de su posición.
- **Sistemas Posicionales**: El valor de cada símbolo depende de su POSICIÓN en la representación.

###### Ejemplo 1: Números Romanos (Sistema No Posicional)

El sistema romano utiliza símbolos con valores fijos:

| Símbolo | I | V | X | L | C | D | M |
|---------|---|---|----|----|----|----|------|
| Valor   | 1 | 5 | 10 | 50 | 100 | 500 | 1000 |

**Característica clave**: El símbolo "V" representa SIEMPRE 5, independientemente de dónde aparezca en la representación.

**Ejemplos**:

- 4 = IV (no 4, sino "uno antes de cinco" = 5 - 1)
- 27 = XXVII = 10 + 10 + 5 + 1 + 1
- 1994 = MCMXCIV = 1000 + (1000-100) + (100-10) + (5-1) = 1000 + 900 + 90 + 4

**Desventaja**: Los números grandes son difíciles de escribir y las operaciones aritméticas son muy complicadas.

**Función Python disponible**:

```python
decimal_a_romano(numero: int) -> str
romano_a_decimal(romano_str: str) -> int
explicar_romano(numero: int) -> Dict
```

Ver [core/sistemas_numeracion_basicos.py](core/sistemas_numeracion_basicos.py)

###### Ejemplo 2: Base 5 (Sistema Posicional con Potencias)

Sistema posicional donde los pesos de cada posición son potencias de 5:

| Posición | 4 | 3 | 2 | 1 | 0 |
|----------|---|---|---|---|---|
| Peso     | 5^4 = 625 | 5^3 = 125 | 5^2 = 25 | 5^1 = 5 | 5^0 = 1 |
| Símbolo  | 3 | 0 | 4 | 3 | 4 |

**Número en base 5**: 30434₅

**Cálculo**: 3×625 + 0×125 + 4×25 + 3×5 + 4×1 = 1875 + 0 + 100 + 15 + 4 = **1994₁₀**

**Característica clave**: El dígito "3" tiene DIFERENTES valores según su posición:

- En posición 4: representa 3 × 625 = 1875
- En posición 1: representa 3 × 5 = 15

**Funciones Python disponibles**:

```python
decimal_a_base_5(numero: int) -> str
base_5_a_decimal(base_5_str: str) -> int
explicar_base_5(numero: int) -> Dict
```

Ver [core/sistemas_numeracion_basicos.py](core/sistemas_numeracion_basicos.py)

###### Ejemplo 3: Sistema de Notación Temporal (Sistema Posicional con Bases Variables)

El sistema de representación de tiempo es un caso especial: **POSICIONAL pero con BASES VARIABLES**:

- Horas: base 24 (máximo 23)
- Minutos: base 60 (máximo 59)
- Segundos: base 60 (máximo 59)

**Ejemplo**: 3661 segundos

| Posición | Horas | Minutos | Segundos |
|----------|-------|---------|----------|
| Valor    | 1     | 1       | 1        |
| Peso     | 3600  | 60      | 1        |
| Cálculo  | 1×3600 | 1×60 | 1×1 |

**Fórmula**: 1×3600 + 1×60 + 1 = **3661 segundos** = **01:01:01**

Este sistema refleja nuestra realidad histórica y es muy eficiente para operaciones prácticas, pero no utiliza una base única.

**Origen histórico**: Los babilonios utilizaban un sistema sexagesimal (base 60) en astronomía y medición del tiempo, que hoy se preserva en nuestra notación de tiempo y ángulos.

**Funciones Python disponibles**:

```python
decimal_a_tiempo(segundos_totales: int) -> str
tiempo_a_decimal(tiempo_str: str) -> int
explicar_tiempo(segundos_totales: int) -> Dict
```

Ver [core/sistemas_numeracion_basicos.py](core/sistemas_numeracion_basicos.py)

---

##### 2.1.1.2 Unicidad de la Representación

###### Teorema Fundamental

En cualquier sistema de numeración posicional, **cada número natural tiene una representación ÚNICA** (sin ceros a la izquierda) en una base dada.

###### Prueba Informal

Para un número natural $n$ y una base $B$:

$$n = d_k \cdot B^k + d_{k-1} \cdot B^{k-1} + \ldots + d_1 \cdot B^1 + d_0 \cdot B^0$$

donde $0 \le d_i < B$ para cada $i$.

- Los dígitos $d_i$ se obtienen UNÍVOCAMENTE mediante divisiones sucesivas:
  - $d_0 = n \bmod B$
  - $d_1 = (n \div B) \bmod B$
  - $d_i = (\lfloor n / B^i \rfloor) \bmod B$

- La secuencia de operaciones de división es **única y determinista**.

###### Ejemplos Verificables

| Número | Decimal | Binario | Base 5 | Octal | Verificación |
|--------|---------|---------|--------|-------|--------------|
| 4      | 4       | 100     | 4      | 4     | ✓ Única en cada base |
| 27     | 27      | 11011   | 102    | 33    | ✓ Única en cada base |
| 99     | 99      | 1100011 | 344    | 143   | ✓ Única en cada base |
| 1994   | 1994    | 11111001010 | 30434 | 3712 | ✓ Única en cada base |

**Conclusión**: No existe ambigüedad. Cada número tiene exactamente una representación en cada base.

**Funciones Python disponibles**:

```python
demostrar_unicidad() -> Dict
comparar_sistemas(numero: int) -> Dict
```

Ver [core/sistemas_numeracion_basicos.py](core/sistemas_numeracion_basicos.py)

---

##### 2.1.1.3 Conversión entre Sistemas de Numeración

###### Conversión de Base 10 a Base B

**Algoritmo de Divisiones Sucesivas**:

1. Dividir $n$ entre $B$. El resto es el dígito de posición 0.
2. Dividir el cociente entre $B$. El resto es el dígito de posición 1.
3. Repetir hasta que el cociente sea 0.
4. Leer los restos de abajo a arriba.

**Ejemplo**: Convertir 1994 a base 5

```
1994 ÷ 5 = 398 resto 4  → d_0 = 4
398 ÷ 5 = 79 resto 3   → d_1 = 3
79 ÷ 5 = 15 resto 4    → d_2 = 4
15 ÷ 5 = 3 resto 0     → d_3 = 0
3 ÷ 5 = 0 resto 3      → d_4 = 3

Resultado: 30434₅ (leyendo de abajo a arriba)
```

###### Conversión de Base B a Base 10

**Método del Polinomio** (evaluación explícita):

$$\text{Número}_B = d_n \cdot B^n + d_{n-1} \cdot B^{n-1} + \ldots + d_1 \cdot B^1 + d_0 \cdot B^0$$

**Ejemplo**: Convertir 30434₅ a decimal

$$30434_5 = 3 \cdot 5^4 + 0 \cdot 5^3 + 4 \cdot 5^2 + 3 \cdot 5^1 + 4 \cdot 5^0$$
$$= 3 \cdot 625 + 0 \cdot 125 + 4 \cdot 25 + 3 \cdot 5 + 4 \cdot 1$$
$$= 1875 + 0 + 100 + 15 + 4 = 1994_{10}$$

**Método de Horner** (más eficiente, sin exponenciaciones):

$$\text{Resultado} = ((\cdots((d_n \cdot B + d_{n-1}) \cdot B + d_{n-2}) \cdot B + \cdots + d_1) \cdot B + d_0)$$

**Ejemplo**: Convertir 30434₅ usando Horner

```
Paso 1: 3
Paso 2: 3 × 5 + 0 = 15
Paso 3: 15 × 5 + 4 = 79
Paso 4: 79 × 5 + 3 = 398
Paso 5: 398 × 5 + 4 = 1994
```

**Ventaja**: Horner evita calcular potencias, requiere solo $n$ multiplicaciones en lugar de $2n$.

###### Conversión entre Bases Relacionadas

Si $B_1 = b^m$ y $B_2 = b^n$ (por ejemplo, 4 = 2² y 16 = 2⁴), la conversión es más simple:

1. Convertir $B_1 \to b$ (agrupando $m$ dígitos)
2. Convertir $b \to B_2$ (agrupando $n$ dígitos)

**Ejemplo**: Convertir 1111₂ a base 16

```
Agrupamos de 4 en 4 (porque 16 = 2⁴):
  1111₂ = F₁₆
  
Verificación: 1×2³ + 1×2² + 1×2¹ + 1×2⁰ = 8 + 4 + 2 + 1 = 15 = F₁₆
```

---

##### 2.1.1.4 Calculadora: Números Romanos ↔ Decimal

Para practicar los conceptos, aquí una herramienta interactiva:

**Características**:

- Conversión decimal → romanos
- Conversión romanos → decimal
- Validación de representaciones
- Explicación paso a paso
- Verificación de unicidad

**Modulo Python**: [`core/sistemas_numeracion_basicos.py`](core/sistemas_numeracion_basicos.py)

**Funciones principales**:

```python
# Conversión decimal a romano
decimal_a_romano(1994)  → "MCMXCIV"

# Conversión romano a decimal
romano_a_decimal("MCMXCIV")  → 1994

# Explicación paso a paso
explicar_romano(1994)  → diccionario con desglose

# Conversión a base 5
decimal_a_base_5(1994)  → "30434"

# Conversión desde base 5
base_5_a_decimal("30434")  → 1994
```

**Script demostrativo**: [`demo_sistemas_numeracion_basicos.py`](demo_sistemas_numeracion_basicos.py)

Ejecutar para ver 5 demostraciones completas:

```bash
python demo_sistemas_numeracion_basicos.py
```

**Ejemplos de salida**:

| Decimal | Romano | Base 5 |
|---------|--------|--------|
| 4       | IV     | 4      |
| 27      | XXVII  | 102    |
| 99      | XCIX   | 344    |
| 1994    | MCMXCIV| 30434  |

**Nota importante**: Todos estos son sistemas POSICIONALES o NO POSICIONALES, pero cada uno tiene su propia estructura única y aplicaciones. El sistema posicional es el predominante en computación porque permite operaciones aritméticas eficientes.

**Funciones Python disponibles** (conversiones genéricas entre bases B y B'):

```python
decimal_a_base_B(numero: int, base: int) -> str
base_B_a_decimal(numero_str: str, base: int) -> int
base_B_a_base_B_prima(numero_str: str, base_origen: int, base_destino: int) -> str
```

Ver [core/sistemas_numeracion_basicos.py](core/sistemas_numeracion_basicos.py)

---

##### 2.1.1.5 Sistemas Binarios, Octales y Hexadecimales

**Sistemas de numeración binaria (2.1.1.5.1)**:

- Conversión entre binario ($B = 2$) y decimal ($B = 10$)

**Sistemas de numeración octal y hexadecimal (2.1.1.5.2)**:

- Conversión entre octal ($B = 8 = 2^3$), hexadecimal ($B = 16 = 2^4$) y decimal ($B = 10$)

**Conversión entre binario, octal y hexadecimal (2.1.1.5.3)**:

- Métodos de agrupación de dígitos

**Sistema de conversión entre representación de bases relacionadas (2.1.1.5.4)**:

- Conversión entre base $B$ y base $B'$ donde $B = b^n$ y $B' = b^{n'}$

**Función Python optimizada para bases relacionadas**:

```python
base_B_a_base_B_prima_potencias(numero_str: str, base_comun: int, 
                                exponente_origen: int, 
                                exponente_destino: int) -> str
```

Ejemplos:

- `base_B_a_base_B_prima_potencias("11111111", 2, 1, 4)` → Binario a Hexadecimal (2¹ a 2⁴)
- `base_B_a_base_B_prima_potencias("ff", 2, 4, 1)` → Hexadecimal a Binario (2⁴ a 2¹)
- `base_B_a_base_B_prima_potencias("1111", 2, 1, 3)` → Binario a Octal (2¹ a 2³)

Ver [core/sistemas_numeracion_basicos.py](core/sistemas_numeracion_basicos.py)

---

##### 2.1.1.6 Representación en Longitud Fija

**Representación de números naturales (2.1.1.6.1)**:

Representación de números naturales en un registro de longitud fija de $n$ dígitos.

###### Capacidad de Representación (2.1.1.6.1.1)

Llamamos **capacidad de representación** para una longitud dada $n$ y una base $B$ al número $B^n$, que indica cuántos números diferentes se pueden representar en esa configuración.

**Definición formal**:

La capacidad de representación es una función:

$$\text{capacidad}(B, n) = B^n$$

Donde:

- $B$ es la base del sistema de numeración
- $n$ es la longitud (número de dígitos)
- El resultado es el número total de representaciones distintas posibles

**Ejemplos**:

| Base | Longitud | Capacidad | Rango |
|------|----------|-----------|-------|
| 2    | 3        | 2³ = 8    | 0-7 |
| 2    | 8        | 2⁸ = 256  | 0-255 |
| 10   | 3        | 10³ = 1000 | 0-999 |
| 16   | 2        | 16² = 256  | 0-255 (FF) |

**Función de Longitud de Representación**:

Además, definimos la **longitud de representación** como la función que devuelve el mínimo número de dígitos necesarios para representar un número $x$ en una base $B$:

$$\text{longitud}(x, B) = \lfloor \log_B(x) \rfloor + 1$$

Esta es essencialmente el **logaritmo entero** del número en base $B$.

**Funciones Python disponibles** (2.1.1.6.1.1 y 2.1.1.6.1.2):

```python
capacidad_representacion(base: int, longitud: int) -> int
rango_representacion(base: int, longitud: int) -> Tuple[int, int]
longitud_representacion(numero: int, base: int) -> int
analisis_representacion(numero: int, base: int, longitud: int = None) -> Dict
```

Ver [core/sistemas_numeracion_basicos.py](core/sistemas_numeracion_basicos.py)

**Ejemplos**:

- Número 27 en base 10: $\log_{10}(27) \approx 1.43 \Rightarrow \lfloor 1.43 \rfloor + 1 = 2$ dígitos ✓
- Número 255 en base 2: $\log_2(255) \approx 7.99 \Rightarrow \lfloor 7.99 \rfloor + 1 = 8$ dígitos ✓
- Número 1994 en base 5: $\log_5(1994) \approx 4.72 \Rightarrow \lfloor 4.72 \rfloor + 1 = 5$ dígitos (verifica: 30434₅) ✓

###### Rango de Valores Representables (2.1.1.6.1.2)

El **rango de representación** para un registro de longitud $l$ en base $B$ es el intervalo $[0, B^l - 1]$ (cerrado).

**Justificación**:

- **Mínimo**: Con todos los dígitos igual a 0, obtenemos $0 \cdot B^{l-1} + \ldots + 0 \cdot B + 0 = 0$

- **Máximo**: Con todos los dígitos igual a $(B-1)$, obtenemos:
  $$(B-1) \cdot B^{l-1} + (B-1) \cdot B^{l-2} + \ldots + (B-1) \cdot B + (B-1)$$
  $$= (B-1)(B^{l-1} + B^{l-2} + \ldots + B + 1)$$
  $$= (B-1) \cdot \frac{B^l - 1}{B - 1} = B^l - 1$$

**Ejemplos**:

| Base | Longitud | Rango | Capacidad |
|------|----------|-------|-----------|
| 2    | 3        | [0, 7]      | 8 |
| 2    | 8        | [0, 255]    | 256 |
| 10   | 2        | [0, 99]     | 100 |
| 16   | 2        | [0, 255]    | 256 |
| 5    | 5        | [0, 3124]   | 3125 |

**Verificación para el ejemplo 1994 en base 5 con 5 dígitos**:

- Capacidad: $5^5 = 3125$ (se pueden representar 3125 números diferentes)
- Rango: $[0, 5^5 - 1] = [0, 3124]$
- Verificación: 1994 está en el rango $[0, 3124]$ ✓
- Representación: 30434₅ (5 dígitos)

###### Puntos adicionales (2.1.1.6.1.3-2.1.1.6.1.5)

- Comparación entre números naturales representados en longitud fija n y base $B \le 16$ para un sistema nativo de computación con bits (base 2)
- Sistemas de representación decimal en base binaria (BCD)
- Sistemas de representación binaria en base 2

**Relación base-dígitos-rango (2.1.1.6.2)**:

- Relación entre la base de numeración, el número de dígitos y el rango de valores representables

---

##### 2.1.1.7 Números Enteros con Signo

**Magnitud y signo (2.1.1.7.1)**:

- Representación en longitud fija

**Complemento a la base B (2.1.1.7.2)**:

- Complemento a 2 (2.1.1.7.2.1) (longitud fija, base B=2)
- Complemento a 10 (2.1.1.7.2.2) (longitud fija, base 10)
- BCD exceso a 3 y BCD Aitken (2.1.1.7.2.3)

**Exceso a un sesgo k (2.1.1.7.3)**:

- Representación con sesgo

---

##### 2.1.1.8 Operaciones Aritméticas

**Comparación de números (2.1.1.8.1)**:

- Comparación entre números representados en:
  - Magnitud y signo (2.1.1.8.1.1)
  - Complemento a 2 (2.1.1.8.1.2)
  - Exceso a un sesgo k (2.1.1.8.1.3)

**Suma y resta de números naturales (2.1.1.8.2)**:

- Suma y resta de números naturales en base B

**Operaciones de complementación (2.1.1.8.3)**:

- Operaciones de complementación a la base B (CB) y a la base B menos 1 (CB-1)

**Inversión de signo (2.1.1.8.4)**:

- Inversión de signo (IS) en números enteros representados en:
  - Magnitud y signo (2.1.1.8.4.1)
  - Complemento a la base B (2.1.1.8.4.2)
  - Exceso a un sesgo k (2.1.1.8.4.3)

**Suma y resta de números enteros (2.1.1.8.5)**:

- Suma y resta de números enteros representados en:
  - Magnitud y signo (2.1.1.8.5.1)
  - Complemento a la base B (2.1.1.8.5.2)
  - Exceso a un sesgo k (2.1.1.8.5.3)

**Multiplicación de números naturales (2.1.1.8.6)**:

- Multiplicación de números naturales en base B

**División y resto (2.1.1.8.7)**:

- División y el resto entre números naturales en base B=2

---

##### 2.1.1.9 Representación de Números con Parte Fraccionaria

**Representación fija (fixed-point) (2.1.1.9.1)**:

- Concepto de punto fijo

**Conversiones entre formatos (2.1.1.9.2)**:

- Paso de una representación E,L-E, donde E es la parte entera y L-E es la parte fraccionaria F, L es la longitud total del número (2.1.1.9.2.1)
- Paso de una base B a otra B' en representación de longitud fija y punto fijo (2.1.1.9.2.2)
- Paso entre bases 10 y 2 en representación de punto fijo (2.1.1.9.2.3)
- Paso entre bases que son potencias de una base común B (2.1.1.9.2.4)
- Paso entre bases 2, 4, 8 y 16 (2.1.1.9.2.5)
- Paso entre bases 3, 9 y 27 (2.1.1.9.2.6)

**Rango y precisión (2.1.1.9.3)**:

- Rangos de valores representables para una longitud fija L y una parte entera de longitud E. Base B. (2.1.1.9.3.1)
- El épsilon de esta representación. (2.1.1.9.3.2)

**Representación en punto flotante (2.1.1.9.4)**:

- Representación de números en punto flotante (2.1.1.9.4.1)
- Representación en punto flotante según la norma IEEE 754 (2.1.1.9.4.2)
- El épsilon de la representación en punto flotante (2.1.1.9.4.3)
- Los rangos de valores representables en punto flotante según la norma IEEE 754 (2.1.1.9.4.4)
- Formas normalizadas y denormalizadas (2.1.1.9.4.5)

**Operaciones en punto flotante (2.1.1.9.5)**:

- Operaciones de redondeo y truncamiento (2.1.1.9.5.1)
- Función 'normalizar' en punto flotante (2.1.1.9.5.2)
- Conversión entre representaciones en punto fijo y punto flotante (2.1.1.9.5.3)
- Operaciones aritméticas en punto flotante: suma, resta, multiplicación y división (2.1.1.9.5.4)

#### 2.1.2 Sistemas de Representación Alfanumérica

**Codificación de Datos**:

- Conceptos fundamentales
- ASCII y Unicode (UTF-8, UTF-16 y UTF-32)

**Sistemas de Detección de Errores**:

- Distancia de Hamming
- Condición de detección de errores
- Códigos de redundancia cíclica (CRC)

**Sistemas de Detección/Corrección de Errores**:

- Condición de corrección de errores
- Códigos de Hamming

---

### 2.2 Álgebras de Boole

#### 2.2.1 Los Postulados de Huntington de 1904

**Estructura Fundamental**:

- Conjunto $B$, operación de suma ('+' o $\lor$) y de producto ('·' o $\land$) (genéricos)
- Condiciones de cierre y existencia de '0' y '1' en el conjunto $B$
- Suma y Producto son funciones de $B \times B \to B$

**Propiedades de Conmutatividad**:

- '+' es conmutativa
- '·' es conmutativa

**Elementos Neutros**:

- '+' tiene neutro '0'
- '·' tiene neutro '1'

**Distributividad**:

- '+' es distributiva respecto a '·'
- '·' es distributiva respecto a '+'

**Complemento**:

- Para todo $a \in B$ existe al menos un elemento $a' \in B$ tal que:
  - $a + a' = 1$
  - $a \cdot a' = 0$

#### 2.2.2 Propiedades y Teoremas del Álgebra de Boole

**Propiedades Básicas**:

1. El neutro es único
2. Si $0 = 1$ entonces el álgebra es trivial
3. El complemento es único (Definición de la función complemento)
4. El complemento es involutivo

**Operaciones Simples**:
5. Idempotencia de la suma y del producto
6. Leyes de absorción de la suma y del producto
7. Leyes de simplificación de la suma y del producto
8. Leyes de simplificación/expansión de Shannon
9. Leyes de Morgan

**Operaciones Complejas**:
10. Leyes de consenso
11. Asociatividad de la suma y del producto

**Funciones Lógicas Derivadas**:

- Definición de la función not and (NAND) y not or (NOR)
- Propiedades de las funciones NAND y NOR
- Funciones completas
- Definición de la función lógica exclusiva (XOR) y (XNOR)
- Propiedades de las funciones XOR y XNOR
- Definición de la función implicación (IMP) y bi-implicación (BI-IMP)
- Propiedades de las funciones IMP y BI-IMP
- Definición de la función suma módulo 2 (SUM2) y producto módulo 2 (PROD2)
- Propiedades de las funciones SUM2 y PROD2

**Estructura Algebraica**:
21. Dualidad de teoremas y expresiones booleanas
22. Leyes complementarias
23. El álgebra de Boole vista como un retículo (orden parcial)
24. Máximos y mínimos en el álgebra de Boole
25. Elementos complementarios en el álgebra de Boole (no se pueden comparar si no son el 0 o el 1)

**Estructuras Algebraicas Especiales**:

- El grupo abeliano $(B, \text{XOR}, 0)$ y $(B, \text{XNOR}, 1)$
- El grupo abeliano $(B, \text{IMP}, 1)$ y $(B, \text{BI-IMP}, 0)$
- El anillo conmutativo $(B, \text{XOR}, \text{AND}, 0, 1)$
- El anillo conmutativo $(B, \text{XNOR}, \text{AND}, 1, 0)$
- El cuerpo $(B, \text{SUM2}, \text{PROD2}, 0, 1)$
- El espacio vectorial $(B^n, \text{SUM2}, \text{PROD2}, 0, 1)$

#### 2.2.3 El Álgebra de Conmutación de Shannon

- Definición y propiedades
- El álgebra de Shannon es un álgebra de Boole
- Todas las propiedades y postulados de Huntington son válidos en el álgebra de Shannon
- Búsqueda de las tablas de verdad de las funciones lógicas básicas
- Derivación de las propiedades partiendo de las tablas de verdad

#### 2.2.4 Las Puertas Lógicas Básicas

**Puertas Fundamentales**:

- Puerta AND
- Puerta OR
- Puerta NOT

**Puertas Derivadas**:

- Puerta NAND
- Puerta NOR
- Puerta XOR
- Puerta XNOR
- Puerta IMP
- Puerta BI-IMP

**Sistemas Completos de Puertas Lógicas**:

- Sistemas completos con puertas AND, OR y NOT
- Sistemas completos con puertas OR, AND y NOT
- Sistemas completos con puertas NAND
- Sistemas completos con puertas NOR
- Sistemas completos con puertas XOR, AND y 1
- Sistemas completos con puertas XNOR, OR y 0

**Propiedades Mediante Puertas Lógicas**:

- Cada propiedad expresada como una conexión de puertas lógicas
- Simulación de las propiedades mediante tablas de verdad
- Simulación de las propiedades mediante circuitos lógicos y cronogramas de tiempo

#### 2.2.5 Funciones Lógicas

**Definición y Conceptos**:

- Definición de función lógica
- Funciones que admiten un predicado sobre n variables
- Simulación de funciones lógicas sobre magnitudes cualesquiera
- Composición de funciones lógicas

**Funciones de n Variables Booleanas**:

- $n=0$: Constantes (0 y 1)
- $n=1$: Identidad, Negación y constantes
- $n=2$: Funciones lógicas básicas (AND, OR, NAND, NOR, XOR, XNOR, IMP, BI-IMP)
- $n>2$: Combinaciones de las anteriores (número explosivo de funciones)

**Representaciones de Funciones Lógicas**:

- Tablas de verdad
- Expresiones booleanas
- Mapas de Karnough
- Circuitos lógicos

**Evaluación mediante Tablas de Verdad**:

- Simulador de funciones a partir de una tabla
- Generador de tablas de verdad a partir de una función
- Traductor de tablas de verdad a mapas de Karnough
- Generador de expresiones canónicas (suma de productos - minitérminos)
- Generador de expresiones canónicas (producto de sumas - maxitérminos)

**Evaluación mediante Mapas de Karnough**:

- Traductor de mapas a tablas de verdad
- Generador de expresiones minimizadas (suma de productos)
- Generador de expresiones minimizadas (producto de sumas)

**Evaluación mediante Expresiones Booleanas**:

- Evaluador y simulador de funciones
- Traductor a tablas de verdad
- Generador de formas canónicas
- Minimización por Quine-McCluskey
- Multiplicidad de formas simplificadas
- Introducción de pesos (costes) en simplificación
- Algoritmo de Petrick

**Evaluación mediante Circuitos Lógicos**:

- Traductor de circuitos a expresiones booleanas
- Simulador de funciones a partir de circuitos

#### 2.2.6 Sistemas Combinacionales Básicos

**Puertas Comerciales**:

- Puertas básicas de la serie 74LSxx
- Inversores y buffers
- NAND, NOR, AND, OR de múltiples entradas

**Componentes Avanzados**:

- XOR/XNOR como inversores controlados
- AND/NAND como interruptores controlados

**Codificadores**:

- Codificador 4 a 2
- Codificador 8 a 3
- Minitérmino como codificador fundamental
- Maxitérmino como codificador fundamental
- Codificadores comerciales 74LSxx
- Interconexión para ampliar entradas

**Decodificadores**:

- Decodificador 2 a 4 (HPRI, LPRI)
- Decodificador 3 a 8 (HPRI, LPRI)
- Decodificadores comerciales 74LSxx
- Interconexión para ampliar salidas

**Conmutadores (Multiplexores)**:

- Conmutador 2 a 1
- Multiplexores

**Demultiplexores**:

- Electores básicos
- Demultiplexores

**Otros Circuitos**:

- Comparadores
- Sumadores y restadores
- Multiplicadores combinacionales
- Conversores de código (Gray ↔ Binario)

#### 2.2.7 Sistemas Combinacionales Avanzados

- Análisis y diseño de sistemas combinacionales
- Unidades Aritmético Lógicas (ALU)
- Sumas y restas en BCD
- Decodificadores de 7 segmentos
- Retardo de propagación y glitches
- Problemas de carrera y soluciones
- Problemas de fan-out y soluciones
- Otros estados lógicos no-determinísticos

---

### 2.3 Sistemas Secuenciales

#### 2.3.1 Introducción

- ¿Por qué son diferentes de los sistemas combinacionales?
- ¿Por qué son necesarios?

#### 2.3.2 Elementos Básicos

**Latches (Asíncronos)**:

- Latch fundamental RS (con puertas NAND y NOR)
- Latches con control de habilitación (sincronía por nivel)
- Latches por ciclo de reloj (master-slave)
- Latches por flanco de subida o bajada

**Flip-Flops**:

- Flip-flop D
- Flip-flop T
- Flip-flop JK
- Flip-flop RS
- Flip-flops con entradas asíncronas (preset y/o clear)
- Cualquier flip-flop a partir del latch RS
- Cualquier flip-flop a partir de otro flip-flop

#### 2.3.3 Sistemas Secuenciales Principales

**Contadores**:

- Contadores síncronos
- Contadores asíncronos
- Contadores de módulo N

**Registros**:

- Registros de desplazamiento
- Registros paralelos
- Combinaciones de registros

**Construcción de Memoria Digital**:

- Pequeñas memorias a partir de flip-flops
- Organización de memorias

#### 2.3.4 Máquinas de Estados Finitos (FSM)

**Conceptos**:

- Introducción
- Conceptos básicos

**Herramientas de Diseño**:

- Diagramas de estados
- Tablas de transición de estados
- Diseño de FSM
- Ejemplos prácticos

#### 2.3.5 Memorias Digitales

**Tipos de Memoria**:

- ROM (Read-Only Memory)
- RAM (Random Access Memory)
- Flash Memory

**Características**:

- Conceptos básicos
- Organización y jerarquía de memorias

---

## 3️⃣ Electrónica Analógica

### 3.1 Dispositivos Lineales Pasivos

#### 3.1.1 Leyes Fundamentales de la Electricidad

- Ley de Ohm
- Leyes de Kirchhoff (Voltaje y Corriente)

#### 3.1.2 Componentes Pasivos

**Resistencias**:

- Comportamiento según Ley de Ohm
- Codificación de valores

**Condensadores**:

- Ley de capacidad y carga
- Comportamiento dinámico

**Inductancias**:

- Ley de inductancia y flujo magnético
- Comportamiento dinámico

**Inductancia Mutua**:

- Transformadores
- Relaciones de transformación

**Fuentes de Energía**:

- Fuentes de tensión ideales y reales
- Fuentes de corriente ideales y reales

---

## 📝 Notas

- Este temario cubre los fundamentos de la Electrónica Digital
- Cada sección incluye teoría, ejercicios prácticos y simulaciones
- Los ejercicios están organizados por nivel de dificultad
- Se incluyen referencias a circuitos integrados comerciales

---

*Última actualización: Enero 2026*  
*Estado: En desarrollo progresivo*
