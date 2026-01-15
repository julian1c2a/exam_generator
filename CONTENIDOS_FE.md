*** Temario de Fundamentos de Electrónica ***
```
1. Introducción a la Electrónica:
   1. Conceptos básicos
   2. Componentes electrónicos
2. Electrónica Digital
   1. Sistemas de Representación de la Información
      1. Sistemas de numeración
         1. Sistemas de numeración posicionales y no posicionales
         2. Sistemas de numeración posicionales: por potencias de la base B
         3. Conversión entre sistemas de numeración con pesos potencias de una base B
         4. Sistemas de numeración no posicionales: números romanos
         5. Sistemas de numeración binaria: conversión entre binario y decimal
         6. Sistemas de numeración octal y hexadecimal: conversión entre octal, hexadecimal y decimal
         7. Conversión entre binario, octal y hexadecimal
         8. Sistema de conversión entre representación de en base B y base B' dónde b^n = b'^m
         9. Representación de números naturales en un registro de longitud fija, de n dígitos
             1. Sistemas de representación decimal en base decimal (BCD)
             2. Sistemas de representación binaria en base 2
         10. Relación entre la base de numeración, el número de dígitos y el rango de valores representables
         11. Representación de números enteros con signo: magnitud y signo (longitud fija)
         12. Representación de números enteros con signo: complemento a la base B (longitud fija)
             1. Representación de números enteros con signo: complemento a 2 (longitud fija, base B=2)
             2. Representación de números enteros con signo: complemento a 10 (longitud fija, base 10) BCD exceso a 3 y BCD Aitken
         13. Representación de números enteros con signo: exceso a un sesgo k (longitud fija)
         14. La comparación entre números representados en magnitud y signo
         15. La comparación entre números representados en complemento a 2
         16. La comparación entre números representados en exceso a un sesgo k
         17. La suma y la resta de números natutrales en base B
         18. Las operaciones de complementación a la base B (CB) y a la base B menos 1 (CBm1)
         19. La inversión de signo (IS) en números enteros representados en magnitud y signo
         20. La inversión de signo (IS) en números enteros representados en complemento a la base B
         21. La inversión de signo (IS) en números enteros representados en exceso a un sesgo k
         22. La suma y la resta de números enteros representados en magnitud y signo
         23. La suma y la resta de números enteros representados en complemento a la base B
         24. La suma y la resta de números enteros representados en exceso a un sesgo k
         25. La multiplicación de números naturales en base B
         26. La división y el resto entre números naturales en base B=2
      2. Sistemas de representación alfanumérica
         1. Codificación de datos
         2. ASCII y Unicode (UTF-8, UTF-16 y UTF-32)
         3. Sistemas de detección de errores
         4. Distancia de Hamming
         5. Condición de detección de errores
         6. Códigos de redundancia cíclica (CRC)
         7. Sistemas de detección/corrección de errores
         8. Condición de corrección de errores
         9. Códigos de Hamming
   2. Álgebras de Boole
      1. Los postulados de Huntington de 1904
         1. Conjunto $B$, operación de suma ('+' o $\or$) y de producto ('*' o $\and$) (genéricos), condiciones de cierre y existencia de '0' y '1' en el conjunto $B$
         2. Suma y Producto son funciones de $B × B \to B$
         3.a '+' es conmutativa
         3.b '*' es conmutativa
         4.a '+' tiene neutro '0'
         4.b '*' tiene neutro '1'
         5.a '+' es distributiva respecto a '*'
         5.b '*' es distributiva respecto a '+'
         6   Para todo $a \in B$ existe al menos un elemento $a' \in B$ tal que:
             1.a $a + a' = 1$
             1.b $a * a' = 0$
      2. Propiedades (teoremas) del álgebra de Boole
         1. El neutro es único
         2. Si $0 = 1$ entonces el álgebra es trivial
         3. El complemento es único (Definición de la función complemento)
         4. El complemento es involutivo
         5. Idempotencia de la suma y del producto
         6. Leyes de absorción de la suma y del producto
         7. Leyes de simplificación de la suma y del producto
         8. Leyes de simplificación/expansión de Shannon
         9. Leyes de Morgan
         10. Leyes de consenso
         11. Asociatividad de la suma y del producto
         12. Definición de la función not and (NAND) y not or (NOR)
         13. Propiedades de las funciones NAND y NOR
         14. Funciones completas
         15. Definción de la función lógica o exlusiva (XOR) y (XNOR)
         16. Propiedades de las funciones XOR y XNOR
         17. Definición de la función lógica implicación (IMP) y bi-implicación (BI-IMP)
         18. Propiedades de las funciones IMP y BI-IMP
         19. Definición de la función lógica suma módulo 2 (SUM2) y producto módulo 2 (PROD2)
         20. Propiedades de las funciones SUM2 y PROD2
         21. Dualidad de teoremas y expresiones booleanas
         22. Leyes complementarias
         23. El álgebra de Boole vista como un retículo (orden parcial)
         24. Máximos y mínimos en el álgebra de Boole
         25. Elementos complementarios en el álgebra de Boole (no se pueden comparar si no son el 0 o el 1)
         26. El grupo abeliano (B, XOR, 0) y (B, XNOR, 1)
         27. El grupo abeliano (B, IMP, 1) y (B, BI-IMP, 0)
         28. El anillo conmutativo (B, XOR, AND, 0, 1)
         29. El anillo conmutativo (B, XNOR, AND, 1, 0)
         30. El cuerpo (B, SUM2, PROD2, 0, 1)
         31. El espacio vectorial (B^n, SUM2, PROD2, 0, 1)
      3. El álgebra de conmutación de Shannon
         1. Definición y propiedades
         2. El álgebra de Shannon es un álgebra de Boole
         3. Todas las propiedades y postulados de Huntington son válidos en el álgebra de Shannon
         4. Búsqueda de las tablas de verdad de las funciones lógicas básicas
         5. Derivación de las propiedades partiendo de las tablas de verdad
      4. Las puertas lógicas básicas
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