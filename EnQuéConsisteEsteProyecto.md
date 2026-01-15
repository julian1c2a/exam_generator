### QUÉ SE PROPONE ESTE PROYECTO ###

Este proyecto tiene un punto de partida: soy profesor de Fundamentos de Electrónica, asignatura obligatoria en todas las Ingenierías Industriales en la Universidad de Málaga, pero de hecho también lo es en toda Europa, y en muchas otras titulaciones. Anterioremente he impartido otras asignaturas de Electrónica, tanto de carácter básico como ésta, como otras más avanzadas. Las de carácter básico ha sido Electrónica Básica (como esta misma pero anual), como Electrónica Digital. Las más avanzadas son Sistemas Digitales Avanzados y Microelectrónica.

Más que hacer un libro, que no es este proyecto, lo que quiero, para comenzar es un sistema de apuntes y ejercicios que puedan usar mis alumnos (y cualquiera que quiera aprender los fundamentos de la electrónica) de forma libre y gratuita, y más aún con un sistema de autoevaluación que les permita comprobar sus conocimientos y habilidades. Básicamente, quiero que termine siendo un programa que corra en una web de forma interactiva, y que permita a los alumnos aprender y practicar los contenidos de la asignatura.

Para poder poner ruedas a esto, voy a comenzar alrevés de lo habitual: me enfocaré primero en los ejercicios y problemas, y luego en los contenidos teóricos. Incluso como en un programa de ordenador no se pueden hacer prácticas de electrónica (físicos), espero poder aprovechar herramientas libres de simulación de circuitos electrónicos para que los alumnos puedan practicar y experimentar con circuitos electrónicos sin necesidad de disponer de un laboratorio físico.

Vamos a empezar a describir el temario de la asignatura, tal y como se imparte en la Universidad de Málaga, y que es muy similar al que se imparte en otras universidades españolas y europeas. Posteriormente, iremos añadiendo ejercicios y problemas relacionados con cada tema. Realmente se puede extender muchísismo por los bordes, y si hay ayuda de colaboradores, se extenderá mucho más. Pero el objetivo es tener un núcleo básico, que pueda ser ampliado posteriormente.

El temario básico es el siguiente:

```Temario de Fundamentos de Electrónica
1. Introducción a la Electrónica:
    1. Conceptos básicos
    2. Componentes electrónicos
    3. Leyes fundamentales
    4. Circuitos lineales
2. Electrónica Digital
    1. Sistemas de Representación de la Información
       1. Sistemas de numeración
       2. Sistemas de representación alfanumérica
       3. Codificación de datos
       4. Sistemas de detección de errores
       5. Sistemas de detección/corrección de errores
    2. Álgebras de Boole
         1. Los postulados de Huntington de 1904
         2. Propiedades (teoremas) del álgebra de Boole
         3. El álgebra de conmutación de Shannon
         4. Las puertas lógicas básicas
         5. Otras formas de ver las puertas lógicas
         6. Sistemas completos de puertas lógicas
         7. Las propiedades de las puertas lógicas conectándolas con las leyes del álgebra de Boole.
         8. Funciones lógicas.
         9. Formas de representación de las funciones lógicas.
            1. Formas canónicas
            2. Maxitérminos y minitérminos
            3. Solo puertas NAND y solo puertas NOR
            4. Tablas de verdad
            5. Mapa de Karnaugh (como forma de organizar y representar tablas de verdad)
            6. Fórmulas de conversión entre las distintas formas de representación
            7. Fórmulas booleanas para la representación de funciones lógicas
         10. Simplificación de funciones lógicas
            1. Simplificación algebraica
            2. Simplificación mediante mapas de Karnaugh
            3. Simplificación mediante el método de Quine-McCluskey
            4. Otras formas de simplificación
         11. Sistemas combinacionales básicos
            1. Codificadores
            2. Decodificadores
            3. Multiplexores
            4. Demultiplexores
            5. Comparadores
            6. Sumadores y restadores
            7. Multiplicadores combinacionales
            8. Conversores de código: Gray -> Binario y Binario -> Gray
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
        1. Resistencias (Ley de Ohm)
        2. Condensadores (Ley de la capacidad y la carga)
        3. Inductancias (Ley de la inductancia y el flujo magnético)
        4. Inductancia mutua: Transformadores
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
        7. Transistor de Efecto Campo (FET)
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

Cada uno de los puntos anteriores tiene un conjunto de subpuntos que han de ser expuestos, pero en vez de desarrollarlos de forma teórica, se nombrarán y pasaremos a su implementación: un sistema que produzca problemas y sus soluciones. En principio estos problemas y sus soluciones estarán en forma de texto json, pero posteriormente se implementará un sistema web que permita a los alumnos practicar con ellos de forma interactiva. Para cada uno de ellos nos hará falta un generador del problema y un generador de la soución. Probleams y soluciones formarán una pequeña base de conocimientos que se irá ampliando con el tiempo, y hay que elegir bien la forma de almacenmarlos para que sea fácil ampliarlos y modificarlos, no solo por un programa como python (es nuestra elección de lenguaje de programación, aunque problablemente demos rudimentos de C y VHDL).

Cada tema tendrá una serie de ejercicios y problemas asociados, que irán aumentando en número y dificultad con el tiempo. El objetivo es que los alumnos puedan practicar y aprender de forma autónoma, y que el sistema pueda evaluar sus respuestas y proporcionar retroalimentación inmediata.

Para manejar este proyecto, utilizaremos herramientas de control de versiones como Git, y alojaremos el código y los recursos en plataformas como GitHub o GitLab. Esto facilitará la colaboración con otros educadores y desarrolladores interesados en contribuir al proyecto.

Ahora entramos en la parte de desarrollo Python del proyecto. Necesitamos una herramienta que nos permita generar ejercicios y problemas de forma automática, junto con sus soluciones. Esto implica crear funciones y clases en Python que puedan generar estos problemas basándose en parámetros específicos, y luego calcular las soluciones correspondientes. Utilizaremos un enfoque muy moldular, de forma que la producción  de problemas y soluciones será un proceso completamente independiente del sistema web que se utilizará para la interacción con los alumnos, o del sistema latex con el que se podrán escribir automáticamente documentos.

Cuando haya que generar un problema y sus solución (o souluciones), y este haya de representarse con un renderizado, entraremos en un problema importante: nuestro python ha de ser capaz de generar codigo latex que represente lo que el problema requiera. El problema fundamental es que el problema se hace más difícil si el problema requiere gráficos o diagramas. Comforme se vaya desarroyando el proyecto, de forma paralela necesitaremos desarrollar los renderers latex y html que se necesiten. Para esto podemos usar librerías como Matplotlib para gráficos, y TikZ para diagramas en LaTeX. Aunque quizás encontremos otras librerías más específicas para ciertos tipos de diagramas electrónicos, o más flexibles que TikZ. En cualquier caso, el objetivo es que el sistema pueda generar automáticamente los gráficos y diagramas necesarios para cada problema y su solución.

La producción de los gráficos y dagramas será una parte del proyecto especialmente difícil, por lo que se habrá de abordar con mucho cuidado. Necesitaremos un montón de renderers específicos, uno desacoplados de otros. Para los renderers concretos usaremos el método de renderers gneralistas que maracarán el tamaño y el marco y qué pueden admitir, y luego un render espcífico hará las tareas más importantes y sencillas. Otro renderer escribirán el texto que tenga que haber en el gráfico y otro render dibujará elementos de más detalle, desacoplando cada parte del proceso, eligiendo apra esto un sistema de representación legible, sencillo y completo, por ejemplo en json.
