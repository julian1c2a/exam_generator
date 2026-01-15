"""
Sistemas de Numeracion: Posicionales vs No Posicionales

Este modulo explora diferentes sistemas de numeracion y sus caracteristicas:

1. Sistemas no posicionales: Números Romanos
2. Sistemas posicionales por potencias: Base 5 (ejemplo)
3. Sistemas posicionales con bases variables: Notacion de tiempo
4. Conversiones entre ellos
"""

from typing import Dict, Tuple, List


# ============================================================================
# PARTE 1: NÚMEROS ROMANOS (Sistema No Posicional)
# ============================================================================

NUMEROS_ROMANOS_VALORES = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
    'IV': 4,
    'IX': 9,
    'XL': 40,
    'XC': 90,
    'CD': 400,
    'CM': 900,
}

VALORES_ROMANOS_INVERSO = {
    1000: 'M',
    900: 'CM',
    500: 'D',
    400: 'CD',
    100: 'C',
    90: 'XC',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    5: 'V',
    4: 'IV',
    1: 'I',
}


def decimal_a_romano(numero: int) -> str:
    """
    Convierte un número decimal a números romanos.
    
    El sistema romano es NO POSICIONAL:
    - El valor no depende de la posicion, sino del simbolo
    - Cada simbolo tiene un valor fijo
    - Se puede escribir de múltiples formas (aunque la moderna respeta reglas)
    
    Ejemplo: 1994 = MCMXCIV
      M (1000) + CM (900) + XC (90) + IV (4) = 1994
    """
    resultado = ""
    
    for valor, simbolo in VALORES_ROMANOS_INVERSO.items():
        mientras_cantidad = numero // valor
        if mientras_cantidad:
            resultado += simbolo * mientras_cantidad
            numero -= valor * mientras_cantidad
    
    return resultado


def romano_a_decimal(romano_str: str) -> int:
    """
    Convierte números romanos a decimal.
    
    El sistema romano permite solo UNA representacion correcta para cada número
    (con las reglas modernas), pero historicamente habia variaciones.
    
    Reglas:
    - Los simbolos se suman de izquierda a derecha
    - I, X, C, M pueden aparecer hasta 3 veces seguidas
    - V, L, D aparecen como maximo una vez
    - Para restar: I antes de V o X, X antes de L o C, C antes de D o M
    """
    romano_str = romano_str.upper()
    
    # Reemplazar subtracciones por sus valores
    subtracciones = [
        ('IV', 'IIII'),
        ('IX', 'VIIII'),
        ('XL', 'XXXX'),
        ('XC', 'LXXXX'),
        ('CD', 'CCCC'),
        ('CM', 'DCCCC'),
    ]
    
    for resta, suma_equivalente in subtracciones:
        if resta in romano_str:
            romano_str = romano_str.replace(resta, suma_equivalente)
    
    resultado = 0
    for simbolo in romano_str:
        if simbolo in NUMEROS_ROMANOS_VALORES:
            resultado += NUMEROS_ROMANOS_VALORES[simbolo]
    
    return resultado


def explicar_romano(numero: int) -> Dict:
    """
    Explica la conversion de decimal a romano paso a paso.
    """
    romano = decimal_a_romano(numero)
    
    # Desglosar
    desglose = []
    numero_temp = numero
    
    for valor, simbolo in VALORES_ROMANOS_INVERSO.items():
        mientras_cantidad = numero_temp // valor
        if mientras_cantidad:
            desglose.append({
                'valor': valor,
                'simbolo': simbolo,
                'cantidad': mientras_cantidad,
                'representacion': simbolo * mientras_cantidad,
                'resta': valor * mientras_cantidad
            })
            numero_temp -= valor * mientras_cantidad
    
    return {
        'numero_decimal': numero,
        'romano': romano,
        'desglose': desglose,
        'explicacion': f"{numero} en romano = {' + '.join([d['representacion'] for d in desglose])}"
    }


# ============================================================================
# PARTE 2: SISTEMAS POSICIONALES POR POTENCIAS (Base 5)
# ============================================================================

def decimal_a_base_5(numero: int) -> str:
    """
    Convierte decimal a base 5.
    
    Sistema POSICIONAL: El valor de cada digito depende de su posicion.
    Posicion 0 = 5^0 = 1
    Posicion 1 = 5^1 = 5
    Posicion 2 = 5^2 = 25
    etc.
    
    Ejemplo: 1994 en decimal
    1994 / 5 = 398 resto 4
    398 / 5 = 79 resto 3
    79 / 5 = 15 resto 4
    15 / 5 = 3 resto 0
    3 / 5 = 0 resto 3
    
    Resultado: 30434_5 (leyendo los restos de abajo a arriba)
    Verificacion: 3*5^4 + 0*5^3 + 4*5^2 + 3*5^1 + 4*5^0 = 1875 + 0 + 100 + 15 + 4 = 1994
    """
    if numero == 0:
        return "0"
    
    digitos = []
    while numero > 0:
        digitos.append(str(numero % 5))
        numero //= 5
    
    return ''.join(digitos[::-1])


def base_5_a_decimal(base_5_str: str) -> int:
    """
    Convierte base 5 a decimal.
    
    El valor se calcula como:
    Número = d_n*5^n + d_(n-1)*5^(n-1) + ... + d_0*5^0
    """
    resultado = 0
    for i, digito in enumerate(reversed(base_5_str)):
        resultado += int(digito) * (5 ** i)
    
    return resultado


def explicar_base_5(numero: int) -> Dict:
    """
    Explica la conversion de decimal a base 5 paso a paso.
    """
    base_5 = decimal_a_base_5(numero)
    
    # Desglose por divisiones
    divisiones = []
    temp = numero
    while temp > 0:
        dividendo = temp
        divisor = 5
        cociente = temp // 5
        resto = temp % 5
        divisiones.append({
            'dividendo': dividendo,
            'divisor': divisor,
            'cociente': cociente,
            'resto': resto
        })
        temp = cociente
    
    # Desglose por potencias (de vuelta)
    potencias = []
    for i, digito in enumerate(reversed(base_5)):
        valor_posicion = 5 ** i
        valor_digito = int(digito)
        aporte = valor_digito * valor_posicion
        potencias.append({
            'posicion': i,
            'digito': digito,
            'potencia': valor_posicion,
            'calculo': f"{digito}*5^{i}",
            'valor': aporte
        })
    
    return {
        'número_decimal': numero,
        'base_5': base_5,
        'divisiones': divisiones,
        'potencias': potencias,
        'suma_final': sum(p['valor'] for p in potencias),
        'explicacion': f"{numero}_1_0 = {base_5}_5"
    }


# ============================================================================
# PARTE 3: SISTEMA POSICIONAL CON BASES VARIABLES (Notacion de Tiempo)
# ============================================================================

def decimal_a_tiempo(segundos_totales: int) -> str:
    """
    Convierte segundos a formato HH:MM:SS.
    
    Este es un sistema POSICIONAL pero CON BASES VARIABLES:
    - Base 24 para horas (max 23)
    - Base 60 para minutos (max 59)
    - Base 60 para segundos (max 59)
    
    NO es una base única, sino un sistema posicional MIXTO.
    
    Ejemplo: 3661 segundos
    3661 / 60 = 61 minutos, 1 segundo
    61 / 60 = 1 hora, 1 minuto
    
    Resultado: 01:01:01 (1 hora, 1 minuto, 1 segundo)
    """
    horas = segundos_totales // 3600
    minutos = (segundos_totales % 3600) // 60
    segundos = segundos_totales % 60
    
    return f"{horas:02d}:{minutos:02d}:{segundos:02d}"


def tiempo_a_decimal(tiempo_str: str) -> int:
    """
    Convierte HH:MM:SS a segundos.
    """
    partes = tiempo_str.split(':')
    if len(partes) != 3:
        raise ValueError("Formato debe ser HH:MM:SS")
    
    horas, minutos, segundos = map(int, partes)
    return horas * 3600 + minutos * 60 + segundos


def explicar_tiempo(segundos_totales: int) -> Dict:
    """
    Explica la conversion de segundos a tiempo paso a paso.
    """
    tiempo = decimal_a_tiempo(segundos_totales)
    
    horas = segundos_totales // 3600
    minutos = (segundos_totales % 3600) // 60
    segundos = segundos_totales % 60
    
    return {
        'segundos_totales': segundos_totales,
        'tiempo': tiempo,
        'desglose': {
            'horas': horas,
            'minutos': minutos,
            'segundos': segundos,
        },
        'calculo': f"{horas}*3600 + {minutos}*60 + {segundos} = {segundos_totales}",
        'explicacion': f"Sistema POSICIONAL con bases variables (24, 60, 60)"
    }


# ============================================================================
# PARTE 4: COMPARACIÓN Y EJEMPLOS
# ============================================================================

def comparar_sistemas(numero: int) -> Dict:
    """
    Muestra la representacion del mismo número en diferentes sistemas.
    """
    return {
        'número_decimal': numero,
        'sistemas': {
            'romano': {
                'representacion': decimal_a_romano(numero),
                'tipo': 'No Posicional',
                'descripcion': 'Cada simbolo tiene valor fijo'
            },
            'base_5': {
                'representacion': decimal_a_base_5(numero),
                'tipo': 'Posicional (potencias de 5)',
                'descripcion': 'Valor depende de posicion'
            },
            'base_10': {
                'representacion': str(numero),
                'tipo': 'Posicional (potencias de 10)',
                'descripcion': 'Sistema decimal moderno'
            }
        }
    }


def demostrar_unicidad() -> Dict:
    """
    Demuestra que cada sistema tiene representacion ÚNICA.
    
    Sistemas posicionales: Para cada número natural, existe UNA única
    representacion en una base dada (sin ceros a la izquierda).
    
    Sistema romano (moderno): Tambien existe una única representacion
    según las reglas de notacion.
    """
    números = [4, 9, 27, 99, 1994]
    
    ejemplos = []
    for num in números:
        rom = decimal_a_romano(num)
        b5 = decimal_a_base_5(num)
        b10 = str(num)
        
        # Verificar conversiones inversas
        rom_inverso = romano_a_decimal(rom)
        b5_inverso = base_5_a_decimal(b5)
        
        ejemplos.append({
            'número': num,
            'romano': rom,
            'base_5': b5,
            'base_10': b10,
            'verificacion': {
                'romano_inverso': rom_inverso == num,
                'base_5_inverso': b5_inverso == num
            }
        })
    
    return {
        'titulo': 'Unicidad de Representacion',
        'descripcion': 'Cada sistema posicional tiene UNA única representacion para cada número',
        'ejemplos': ejemplos,
        'conclusion': 'Todas las conversiones inversas son correctas: cada número tiene una única representacion en cada sistema'
    }


# ============================================================================
# PARTE 5: REPRESENTACIÓN EN LONGITUD FIJA (2.1.1.6)
# ============================================================================

def capacidad_representacion(base: int, longitud: int) -> int:
    """
    Calcula la capacidad de representación (2.1.1.6.1.1).
    
    La capacidad es el número total de valores diferentes que se pueden
    representar en una base dada con una longitud fija.
    
    Fórmula: capacidad(B, n) = B^n
    
    Args:
        base: Base del sistema de numeración (B)
        longitud: Número de dígitos disponibles (n)
    
    Returns:
        int: B^n = número de valores representables
        
    Ejemplos:
        capacidad_representacion(2, 3) = 8   (00 a 111 en binario)
        capacidad_representacion(2, 8) = 256 (00000000 a 11111111)
        capacidad_representacion(10, 3) = 1000 (000 a 999)
        capacidad_representacion(16, 2) = 256 (00 a FF)
    """
    return base ** longitud


def rango_representacion(base: int, longitud: int) -> Tuple[int, int]:
    """
    Calcula el rango de valores representables (2.1.1.6.1.2).
    
    Para una base B y longitud l, el rango es [0, B^l - 1] (cerrado).
    
    Args:
        base: Base del sistema de numeración (B)
        longitud: Número de dígitos disponibles (l)
    
    Returns:
        Tuple[int, int]: (mínimo, máximo) = (0, B^l - 1)
        
    Ejemplos:
        rango_representacion(2, 3) = (0, 7)
        rango_representacion(2, 8) = (0, 255)
        rango_representacion(10, 2) = (0, 99)
        rango_representacion(16, 2) = (0, 255)
    """
    capacidad = base ** longitud
    return (0, capacidad - 1)


def longitud_representacion(numero: int, base: int) -> int:
    """
    Calcula la longitud mínima de representación (2.1.1.6.1.2).
    
    Devuelve el mínimo número de dígitos necesarios para representar
    un número en una base dada.
    
    Fórmula: longitud(x, B) = ⌊log_B(x)⌋ + 1
    
    Esto es el logaritmo entero en base B + 1.
    
    Args:
        numero: Número a representar (x)
        base: Base del sistema de numeración (B)
    
    Returns:
        int: Número mínimo de dígitos necesarios
        
    Raises:
        ValueError: Si numero < 1 o base < 2
        
    Ejemplos:
        longitud_representacion(27, 10) = 2  (27 requiere 2 dígitos)
        longitud_representacion(255, 2) = 8  (255 = 11111111₂)
        longitud_representacion(1994, 5) = 5 (1994 = 30434₅)
        longitud_representacion(9, 10) = 1   (9 requiere 1 dígito)
    """
    import math
    
    if numero < 1:
        raise ValueError("El número debe ser positivo (≥ 1)")
    if base < 2:
        raise ValueError("La base debe ser ≥ 2")
    
    if numero == 0:
        return 1
    
    # ⌊log_B(x)⌋ + 1
    return math.floor(math.log(numero, base)) + 1


def analisis_representacion(numero: int, base: int, longitud: int = None) -> Dict:
    """
    Análisis completo de capacidad y rango de representación.
    
    Combina: capacidad(B, n), rango(B, n), y longitud(x, B).
    
    Args:
        numero: Número a analizar
        base: Base del sistema
        longitud: Longitud fija (opcional, si None se calcula automáticamente)
    
    Returns:
        Dict con análisis completo
    """
    if longitud is None:
        longitud = longitud_representacion(numero, base)
    
    capacidad = capacidad_representacion(base, longitud)
    rango_min, rango_max = rango_representacion(base, longitud)
    longitud_min = longitud_representacion(numero, base)
    
    está_en_rango = rango_min <= numero <= rango_max
    
    return {
        'número': numero,
        'base': base,
        'longitud_fija': longitud,
        'longitud_mínima': longitud_min,
        'capacidad': capacidad,
        'rango': f'[{rango_min}, {rango_max}]',
        'rango_min': rango_min,
        'rango_max': rango_max,
        'en_rango': está_en_rango,
        'fórmula_capacidad': f'{base}^{longitud} = {capacidad}',
        'fórmula_rango_máximo': f'{base}^{longitud} - 1 = {rango_max}'
    }


# ============================================================================
# EJEMPLOS Y EDUCACIÓN
# ============================================================================

# ============================================================================
# PARTE 6: CONVERSIONES GENÉRICAS ENTRE BASES
# ============================================================================

def decimal_a_base_B(numero: int, base: int) -> str:
    """
    Convierte un número decimal a cualquier base B (2-36).
    
    Algoritmo: Divisiones sucesivas
    - Dividir numero entre base, guardar el resto
    - El resto es un dígito en base B
    - Repetir con el cociente hasta que sea 0
    
    Parámetros:
        numero: Número decimal a convertir (>= 0)
        base: Base destino (2-36)
        
    Retorna:
        String con la representación en base B
        Usa dígitos 0-9 y letras A-Z para bases > 10
        
    Ejemplos:
        decimal_a_base_B(1994, 5) → "30434"
        decimal_a_base_B(255, 2) → "11111111"
        decimal_a_base_B(255, 16) → "ff"
        
    Referencias: 2.1.1.3 (Conversión de Base 10 a Base B)
    """
    if numero == 0:
        return "0"
    
    if not (2 <= base <= 36):
        raise ValueError("Base debe estar entre 2 y 36")
    
    digitos = "0123456789abcdefghijklmnopqrstuvwxyz"
    resultado = []
    
    while numero > 0:
        resultado.append(digitos[numero % base])
        numero //= base
    
    return ''.join(reversed(resultado))


def base_B_a_decimal(numero_str: str, base: int) -> int:
    """
    Convierte un número en base B a decimal.
    
    Algoritmo: Evaluación del polinomio
    Número_B = d_n * B^n + d_(n-1) * B^(n-1) + ... + d_0 * B^0
    
    Parámetros:
        numero_str: String con la representación en base B
        base: Base origen (2-36)
        
    Retorna:
        Número en decimal (base 10)
        
    Ejemplos:
        base_B_a_decimal("30434", 5) → 1994
        base_B_a_decimal("11111111", 2) → 255
        base_B_a_decimal("ff", 16) → 255
        
    Referencias: 2.1.1.3 (Conversión de Base B a Base 10)
    """
    if not (2 <= base <= 36):
        raise ValueError("Base debe estar entre 2 y 36")
    
    digitos = "0123456789abcdefghijklmnopqrstuvwxyz"
    numero_str = numero_str.lower()
    resultado = 0
    
    for i, digito in enumerate(reversed(numero_str)):
        if digito not in digitos[:base]:
            raise ValueError(f"Dígito '{digito}' inválido para base {base}")
        resultado += digitos.index(digito) * (base ** i)
    
    return resultado


def base_B_a_base_B_prima(numero_str: str, base_origen: int, base_destino: int) -> str:
    """
    Conversión genérica entre dos bases B y B' (2-36).
    
    Método: Conversión a través de decimal
    1. Convertir de base B a decimal
    2. Convertir de decimal a base B'
    
    Parámetros:
        numero_str: Número en base B
        base_origen: Base B (2-36)
        base_destino: Base B' (2-36)
        
    Retorna:
        String con la representación en base B'
        
    Ejemplos:
        base_B_a_base_B_prima("30434", 5, 2) → "11111001010"
        base_B_a_base_B_prima("ff", 16, 10) → "255"
        base_B_a_base_B_prima("1010", 2, 8) → "12"
        
    Referencias: 2.1.1.3 (Conversión entre Sistemas de Numeración)
    """
    decimal = base_B_a_decimal(numero_str, base_origen)
    return decimal_a_base_B(decimal, base_destino)


def base_B_a_base_B_prima_potencias(numero_str: str, base_comun: int, 
                                    exponente_origen: int, 
                                    exponente_destino: int) -> str:
    """
    Conversión eficiente entre bases relacionadas B = b^n y B' = b^(n').
    
    Cuando la base origen B = b^n y la base destino B' = b^(n'),
    se puede convertir de manera más eficiente agrupando dígitos en la base común b.
    
    Método:
    1. Convertir B → b (agrupando/expandiendo n dígitos de base B)
    2. Convertir b → B' (agrupando n' dígitos de base b)
    
    Parámetros:
        numero_str: Número en base B (donde B = base_comun^exponente_origen)
        base_comun: Base b (2, 3, 5, etc.)
        exponente_origen: n tal que B = b^n
        exponente_destino: n' tal que B' = b^(n')
        
    Retorna:
        String con la representación en base B' (donde B' = b^(n'))
        
    Ejemplos:
        # Convertir binario (2^1) a hexadecimal (2^4)
        base_B_a_base_B_prima_potencias("11111111", 2, 1, 4) → "ff"
        
        # Convertir hexadecimal (2^4) a binario (2^1)
        base_B_a_base_B_prima_potencias("ff", 2, 4, 1) → "11111111"
        
        # Convertir binario (2^1) a octal (2^3)
        base_B_a_base_B_prima_potencias("1111", 2, 1, 3) → "17"
        
        # Convertir base 3 (3^1) a base 27 (3^3)
        base_B_a_base_B_prima_potencias("010021002", 3, 1, 3) → "122"
        
    Referencias: 2.1.1.5.4 (Sistema de conversión entre representación de bases relacionadas)
    
    Notas:
        - Si exponente_origen > exponente_destino: expandir dígitos y reagrupar
        - Si exponente_origen < exponente_destino: agrupar exponente_destino dígitos
        - Mucho más eficiente que pasar por decimal para bases grandes
    """
    if exponente_origen == exponente_destino:
        return numero_str
    
    # Primero: Convertir a base b (expandir exponente_origen dígitos en exponente_origen*log(base) dígitos)
    digitos_base_comun = []
    for digito_char in numero_str:
        # Convertir cada dígito de base B a su valor en base b
        digito_valor = int(digito_char, base_comun ** exponente_origen)
        
        # Expandir a exponente_origen dígitos en base b
        for _ in range(exponente_origen):
            digitos_base_comun.append(digito_valor % base_comun)
            digito_valor //= base_comun
        digitos_base_comun.reverse()
    
    # Segundo: Convertir de base b a base B' (agrupar exponente_destino dígitos)
    digitos_base_comun.reverse()  # Para procesar de derecha a izquierda
    resultado_digitos = []
    
    while digitos_base_comun:
        # Tomar exponente_destino dígitos de base b
        grupo = []
        for _ in range(exponente_destino):
            if digitos_base_comun:
                grupo.append(digitos_base_comun.pop())
        
        # Convertir grupo de base b a un dígito de base B'
        valor_digito = 0
        for digito in reversed(grupo):
            valor_digito = valor_digito * base_comun + digito
        
        resultado_digitos.append(valor_digito)
    
    # Convertir a string usando dígitos 0-9, a-z
    digitos_str = "0123456789abcdefghijklmnopqrstuvwxyz"
    resultado = ''.join(digitos_str[d] for d in reversed(resultado_digitos))
    
    return resultado if resultado else "0"


if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("SISTEMAS DE NUMERACIÓN: Posicionales vs No Posicionales")
    print("=" * 70)
    
    # Ejemplo 1: Número Romano
    print("\n1. SISTEMA ROMANO (No Posicional)")
    print("-" * 70)
    numero = 1994
    explicacion = explicar_romano(numero)
    print(f"Número: {numero}_1_0 = {explicacion['romano']}")
    print(f"Desglose:")
    for d in explicacion['desglose']:
        print(f"  {d['cantidad']}* {d['simbolo']} = {d['representacion']} ({d['resta']})")
    
    # Ejemplo 2: Base 5
    print("\n2. SISTEMA BASE 5 (Posicional - Potencias)")
    print("-" * 70)
    número_base5 = 1994
    explicacion_b5 = explicar_base_5(número_base5)
    print(f"Número: {número_base5}_1_0 = {explicacion_b5['base_5']}_5")
    print(f"Calculo:")
    for p in explicacion_b5['potencias']:
        print(f"  {p['calculo']} = {p['valor']}")
    print(f"  Suma: {explicacion_b5['suma_final']}")
    
    # Ejemplo 3: Tiempo
    print("\n3. SISTEMA DE TIEMPO (Posicional - Bases Variables)")
    print("-" * 70)
    segundos = 3661
    explicacion_tiempo = explicar_tiempo(segundos)
    print(f"Número: {segundos} segundos = {explicacion_tiempo['tiempo']}")
    print(f"Desglose: {explicacion_tiempo['calculo']}")
    
    print("\n" + "=" * 70)
