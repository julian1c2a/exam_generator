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
# EJEMPLOS Y EDUCACIÓN
# ============================================================================

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
