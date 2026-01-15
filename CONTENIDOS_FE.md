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
