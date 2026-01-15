# 📚 Temario de Fundamentos de Electrónica

---

## 1️⃣ Introducción a la Electrónica

### Conceptos Básicos

- Magnitudes fundamentales
- Ley de Ohm
- Potencia eléctrica

### Componentes Electrónicos

- Resistencias
- Condensadores
- Bobinas
- Semiconductores

---

## 2️⃣ Electrónica Digital

### 2.1 Sistemas de Representación de la Información

#### 2.1.1 Sistemas de Numeración

**Bases Teóricas**:

- Sistemas de numeración posicionales y no posicionales
- Sistemas de numeración posicionales: por potencias de la base B
- Conversión entre sistemas de numeración con pesos potencias de una base B
- Sistemas de numeración no posicionales: números romanos

**Sistemas Binarios, Octales y Hexadecimales**:

- Sistemas de numeración binaria: conversión entre binario y decimal
- Sistemas de numeración octal y hexadecimal: conversión entre octal, hexadecimal y decimal
- Conversión entre binario, octal y hexadecimal
- Sistema de conversión entre representación de en base B y base B' dónde $b^n = b'^m$

**Representación en Longitud Fija**:

- Representación de números naturales en un registro de longitud fija de $n$ dígitos
  - Sistemas de representación decimal en base decimal (BCD)
  - Sistemas de representación binaria en base 2
- Relación entre la base de numeración, el número de dígitos y el rango de valores representables

**Números Enteros con Signo**:

- Magnitud y signo (longitud fija)
- Complemento a la base B (longitud fija)
  - Complemento a 2 (longitud fija, base B=2)
  - Complemento a 10 (longitud fija, base 10)
  - BCD exceso a 3 y BCD Aitken
- Exceso a un sesgo k (longitud fija)

**Operaciones Aritméticas**:

- La comparación entre números representados en:
  - Magnitud y signo
  - Complemento a 2
  - Exceso a un sesgo k
- La suma y la resta de números naturales en base B
- Las operaciones de complementación a la base B (CB) y a la base B menos 1 (CB-1)
- La inversión de signo (IS) en números enteros representados en:
  - Magnitud y signo
  - Complemento a la base B
  - Exceso a un sesgo k
- La suma y la resta de números enteros representados en:
  - Magnitud y signo
  - Complemento a la base B
  - Exceso a un sesgo k
- La multiplicación de números naturales en base B
- La división y el resto entre números naturales en base B=2

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

- Magnitudes fundamentales
- Ley de Ohm
- Potencia eléctrica

### Componentes Electrónicos

- Resistencias
- Condensadores
- Bobinas
- Semiconductores

---

## 2️⃣ Electrónica Digital

### 2.1 Sistemas de Representación de la Información

#### 2.1.1 Sistemas de Numeración

**Bases Teóricas**:

- Sistemas de numeración posicionales y no posicionales
- Sistemas de numeración posicionales: por potencias de la base B
- Conversión entre sistemas de numeración con pesos potencias de una base B
- Sistemas de numeración no posicionales: números romanos

**Sistemas Binarios, Octales y Hexadecimales**:

- Sistemas de numeración binaria: conversión entre binario y decimal
- Sistemas de numeración octal y hexadecimal: conversión entre octal, hexadecimal y decimal
- Conversión entre binario, octal y hexadecimal
- Sistema de conversión entre representación de en base B y base B' dónde $b^n = b'^m$

**Representación en Longitud Fija**:

- Representación de números naturales en un registro de longitud fija de $n$ dígitos
  - Sistemas de representación decimal en base decimal (BCD)
  - Sistemas de representación binaria en base 2
- Relación entre la base de numeración, el número de dígitos y el rango de valores representables

**Números Enteros con Signo**:

- Magnitud y signo (longitud fija)
- Complemento a la base B (longitud fija)
  - Complemento a 2 (longitud fija, base B=2)
  - Complemento a 10 (longitud fija, base 10)
  - BCD exceso a 3 y BCD Aitken
- Exceso a un sesgo k (longitud fija)

**Operaciones Aritméticas**:

- La comparación entre números representados en:
  - Magnitud y signo
  - Complemento a 2
  - Exceso a un sesgo k
- La suma y la resta de números naturales en base B
- Las operaciones de complementación a la base B (CB) y a la base B menos 1 (CB-1)
- La inversión de signo (IS) en números enteros representados en:
  - Magnitud y signo
  - Complemento a la base B
  - Exceso a un sesgo k
- La suma y la resta de números enteros representados en:
  - Magnitud y signo
  - Complemento a la base B
  - Exceso a un sesgo k
- La multiplicación de números naturales en base B
- La división y el resto entre números naturales en base B=2

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

*Sección en desarrollo...*
         1. Puerta AND
         2. Puerta OR
         3. Puerta NOT
      5. Otras formas de ver las puertas lógicas
         1. Puerta NAND
         2. Puerta NOR
         3. Puerta XOR
         4. Puerta XNOR
         5. Puerta IMP
         6. Puerta BI-IMP
      6. Sistemas completos de puertas lógicas
         1. Sistemas completos con puertas AND, OR y NOT
         2. Sistemas completos con puertas OR, AND y NOT
         3. Sistemas completos con puertas NAND
         4. Sistemas completos con puertas NOR
         5. Sistemas completos con puertas XOR, AND y 1
         6. Sistemas completos con puertas XNOR, OR y 0
      7. Las propiedades de las puertas lógicas conectándolas con las leyes del álgebra de Boole.
         1. Cada propiedad expresada como una conexión de puertas lógicas
         2. Simulación de las propiedades mediante tablas de verdad
         3. Simulación de las propiedades mediante circuitos lógicos y cronogramas de tiempo
      8. Funciones lógicas.
         1. Definición de función lógica
            1. Crear una función python que admita un predicado sobre n variables de cualquier tipo y devuelba True/False
            2. Simulación de funciones lógicas que dependen de magnitudes cualquieras (no solo booleanas)
            3. Composición de las anteriores funciones lógicas
            4. Funciones lógicas de n variables dependientes booleanas
               1. n=0 Constantes (0 y 1)
               2. n=1 Identidad, Negación y constantes
               3. n=2 Funciones lógicas básicas (AND, OR, NAND, NOR, XOR, XNOR, IMP, BI-IMP)
               4. n>2 Combinaciones de las anteriores. Número explosivo de funciones lógicas.
         2. Representación de funciones lógicas mediante tablas de verdad
         3. Representación de funciones lógicas mediante expresiones booleanas
         4. Representación de funciones lógicas mediante tablas de Karnough
         5. Representación de funciones lógicas mediante circuitos lógicos
         7. Evaluación de funciones lógicas
            1. Evaluación mediante tablas de verdad
               1. Simulador de funciones a partir de una tabla de verdad
               2. Generador de tablas de verdad a partir de una función lógica 8.1.1.
               3. Traductor de funciones de verdad a tablas de Karnough
               4. Generador de expresiones lógicas como suma de productos (minitérminos)
               5. Generador de expresiones lógicas como producto de sumas (maxitérminos)
            2. Evaluación mediante tablas de verdad de Karnough
               1. Traductor de tablas de Karnough a tablas de verdad
               2. Generador de expresiones lógicas minimizadas como suma de productos (minitérminos)
               3. Generador de expresiones lógicas minimizadas como producto de sumas (maxitérminos)
            2. Evaluación mediante expresiones booleanas
               1. Evaluador y simulador de funciones a partir de una expresión booleana
               2. Traductor de expresiones booleanas a tablas de verdad
               3. Generador de expresiones booleanas canónicas como suma de productos (minitérminos) a partir de una dada.
               4. Generador de expresiones booleanas canónicas como producto de sumas (maxitérminos) a partir de una dada.
               5. Generar funciones booleanas por minitérminos minimizadas por el método de Quine-McCluskey
               6. Generar funciones booleanas por maxitérminos minimizadas por el método de Quine-McCluskey
               7. Multiplicidad de formas simplificadas de una misma función lógica
               8. Intgroducción de pesos (costes) a la hora de simplificar funciones lógicas
               9. Algoritmo de Petrick
            3. Evaluación mediante circuitos lógicos
               1. Traductor de circuitos lógicos a expresiones booleanas
               2. Simulador de funciones a partir de un circuito lógico
      11. Sistemas combinacionales básicos
         1. Puertas básicas comerciales de la serie 74LSxx
         2. Inversores y buffers
         3. NAND de 2, 3, 4 y 8 entradas
         4. NOR de 2, 3, 4 y 8 entradas
         5. AND de 2, 3, 4 y 8 entradas
         6. OR de 2, 3, 4 y 8 entradas
         7. XOR de 2 entradas
         1. Inversores controlados con puertas XOR y XNOR
         2. Interruptores controlados con puertas AND y NAND
         3. Codificadores
            1. Implementación de un codificador 4 a 2
            2. Implementación de un codificador 8 a 3
            3. Un minitérmino como un codificador fundamental
            4. Un maxitérmino como un codificador fundamental
            5. Codificadores comerciales de la serie 74LSxx (Funcionamiento y diseño)
            6. Interconexión de codificadores para ampliar el número de entradas
         4. Decodificadores
            1. El problema fundamental de la decodificación (codificador compuesto con decodificador y viceversa)
            2. Implementación de un decodificador 2 a 4 HPRI, LPRI
            3. Implementación de un decodificador 3 a 8 HPRI, LPRI
            4. Decodificadores comerciales de la serie 74LSxx (Funcionamiento y diseño)
            5. Interconexión de decodificadores para ampliar el número de salidas
         5. Conmutadores básicos de 2 señales a 1
            1. Diseño, expresión lógica, tabla de verdad y circuito lógico
            2. Implementación de un conmutador 2 a 1
            3. Simulación y cronogramas de tiempo
         6. Multiplexores
            1. El multiplexor como conmutador avanzado
         7. Electores básicos de 1 señal a 2
         8. Demultiplexores
         9. Comparadores
         10. Sumadores y restadores
         11. Multiplicadores combinacionales
         12. Conversores de código: Gray -> Binario y Binario -> Gray
      12. Sistemas combinacionales avanzados
         1. Análisis y diseño de sistemas combinacionales
         2. Unidades Aritmético Lógicas (ALU)
         3. Sistemas de sumas y restas en BCD
         4. Codificadores y decodificadores de 7 segmentos
         5. Retardo de propagación y glitches
         6. Problemas de carrera y cómo evitarlos
         7. Problemas de fan-out y como evitarlos
         8. Otros estados lógicos no-lógicos
      13. Sistemas secuenciales
         1. Introducción a los sistemas secuenciales ¿Por qué son diferentes de los combinaciones? ¿Por qué son necesarios?
         2. Latch fundamental (completamente asíncrono) RS, con puertas NAND y NOR
         3. Latches con control de habilitación (sincronía por nivel)
         4. Latches por ciclo de reloj (master-slave)
         5. Latches por flanco de subida o de bajada del reloj.
         6. Flip-flop D, T, JK y RS
         7. Flip-flop con entradas asíncronas de preset y/o clear
         8. Cualquier flip-flop se puede construir a partir de un latch fundamental RS
         9. Cualquier flip-flop se puede construir a partir de otro flip-flop cualquiera.
         10. Los principales sistemas secuenciales: contadores y registros
         11. Contadores síncronos y asíncronos
         12. Registros de desplazamiento
         13. Constgruimos una memoria digital (pequeña) a partir de flip-flops
         14. Máquinas de estados finitos
            1. Introducción y conceptos básicos
            2. Diagramas de estados
            3. Tablas de transición de estados
            4. Diseño de máquinas de estados finitos
            5. Ejemplos de máquinas de estados finitos
         15. Memorias digitales
            1. Conceptos básicos
            2. Memorias ROM
            3. Memorias RAM
            4. Memorias Flash
            5. Organización y jerarquía de memorias
3. Electrónica Analógica

   1. Dispositivos Lineales Pasivos
      1. Leyes fundamentales de la electricidad
         1. Ley de Ohm
         2. Leyes de Kirchhoff
      2. Resistencias (Ley de Ohm)
      3. Condensadores (Ley de la capacidad y la carga)
      4. Inductancias (Ley de la inductancia y el flujo magnético)
      5. Inductancia mutua: Transformadores
      6. Fuentes de tensión y de corriente ideales y reales.
      7. Fuentes dependientes
      8. Asociación de elementos pasivos
         1. Asociación en serie
         2. Asociación en paralelo
         3. Asociación mixta
      9. Ordenación del circuito por nodos.
      10. Ordenación del circuito por lazos.
   2. Análisis de circuitos eléctricos
      1. Principio de superposición
      2. Ley de Thevenin y Ley de Norton
      3. Circuitos con corriente alterna (AC)
         1. Magnitudes eficaces
         2. Impedancia y admitancia
         3. Potencia en AC
         4. Leyes de Kirchhoff en AC
         5. Análisis de circuitos en AC
      4. Introducción a los semiconductores
      5. Diodo semiconductor
         1. Comportamiento y características del diodo
         2. Modelos de diodo: Ideal, Real y Linealizado
         3. Diodos zener: sus modelos
         4. Aplicaciones del diodo
            1. Rectificadores
            2. Limitadores de tensión
      6. Transistor Bipolar de Unión (BJT)
         1. Estructura y funcionamiento del BJT
         2. Características del BJT
         3. Modelos del BJT: Ideal, Real y Linealizado
         4. Configuraciones básicas de amplificación con BJT
            1. Configuración emisor común
            2. Configuración base común
            3. Configuración colector común
         5. Análisis de circuitos con BJT
      7. Transistor de Efecto Campo (FET, JFET y MOSFET)
         1. Estructura y funcionamiento del FET
         2. Características del FET
         3. Modelos del FET: Ideal, Real y Linealizado
         4. Configuraciones básicas de amplificación con FET
            1. Configuración drenador común
            2. Configuración puerta común
            3. Configuración fuente común
         5. Análisis de circuitos con FET
      8. Amplificadores operacionales
         1. Estructura y funcionamiento del amplificador operacional
         2. Características del amplificador operacional ideal
         3. Amplificadores operacionales reales: saturación.
         4. Amplificadores operacionales reales: amplificación real, impedancia de entrada, impedancia de salida y ancho de banda.
         5. Configuraciones básicas con amplificadores operacionales
            1. El operacional en lazo abierto
            2. El operacional en lazo cerrado y realimentación únicamente negativa
               1. Concepto de realimentación negativa
               2. Ventajas de la realimentación negativa
               3. Desventajas de la realimentación negativa
               4. Ley de cortocircuito virtual
               5. Principales configuraciones con realimentación negativa
                  1. Seguidor de tensión
                  2. Amplificador inversor
                  3. Sumador ponderado (inversor)
                  4. Amplificador no inversor
                  5. Restador ponderado
                  6. Integrador
                  7. Derivador
                  8. El amplificador de instrumentación
                  9. Otros circuitos con amplificadores operacionales: filtros activos  
            3. El operacional en lazo cerrado con alguna realimentación positiva
               1. Circuito oscilador con amplificador operacional
               2. Generador de funciones con amplificador operacional

```
