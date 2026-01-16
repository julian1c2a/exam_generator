"""
SECCIÓN 2.1.1.7: Números Enteros con Signo

Tema: Representación en Magnitud y Signo (M&S)

La representación más natural de números enteros con signo es la que usamos
en matemáticas desde niños: escribimos un signo (+/-) y una magnitud.

En binario de longitud fija, usamos:
- Bit MSB (índice n-1): Bit de signo
  - 0 = positivo (+)
  - 1 = negativo (-)
- Bits MSB-1 hasta LSB: Magnitud (valor absoluto)

Ejemplo: En 8 bits (M&S8)
┌─────────────────────────────────┐
│ 0 1 0 1 0 1 1 0 │  = +86 (decimal)
│ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ │
│ s m m m m m m m │  (s=signo, m=magnitud)
│ 7 6 5 4 3 2 1 0 │  (índices de bit)
└─────────────────────────────────┘

Bit 7 (MSB, signo) = 0 → positivo
Bits 6-0 (magnitud) = 1010110₂ = 86₁₀
Valor = +86

Otro ejemplo: En 8 bits (M&S8)
┌─────────────────────────────────┐
│ 1 1 0 1 0 1 1 0 │  = -86 (decimal)
│ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ │
│ s m m m m m m m │
│ 7 6 5 4 3 2 1 0 │
└─────────────────────────────────┘

Bit 7 (MSB, signo) = 1 → negativo
Bits 6-0 (magnitud) = 1010110₂ = 86₁₀
Valor = -86

PROPIEDADES FUNDAMENTALES:

1. RANGO DE REPRESENTACIÓN (n bits):
   - Números negativos: [-2^(n-1) + 1, -1]
   - Números positivos: [1, 2^(n-1) - 1]
   - Dos representaciones para 0: +0 (00...0) y -0 (10...0)
   - Rango total: [-2^(n-1) + 1, 2^(n-1) - 1]

2. CAPACIDAD:
   - Total de valores diferentes: 2^n - 1
   - (2^n combinaciones menos 1 por la duplicación del 0)

3. EFICACIA:
   - η = (2^n - 1) / 2^n = 1 - (1/2^n) ≈ 1 para n grande

4. VENTAJAS:
   - Intuitivo: como escribimos números a mano
   - Negación simple: invertir el bit de signo
   - Multiplicación/División: |A|·|B| con ajuste de signo

5. DESVENTAJAS:
   - Suma y resta requieren algoritmos diferentes
   - Comparación de negativos es invertida
   - Dos representaciones para el 0
   - Necesita validación de igualdad especial

CONVENCIÓN MSB/LSB:
- MSB (Most Significant Bit) = bit n-1 = bit de signo
- LSB (Least Significant Bit) = bit 0 = bit menos significativo de magnitud
"""

from typing import Dict, Tuple, List, Union
import math


# ============================================================================
# PARTE 1: ANÁLISIS DE RANGO Y CAPACIDAD
# ============================================================================

def rango_ms(n_bits: int) -> Dict[str, Union[int, Tuple[int, int]]]:
    """
    Calcula el rango de valores representables en M&S con n bits.
    
    Args:
        n_bits: Número total de bits (incluyendo bit de signo)
    
    Returns:
        Dict con:
        - min_negativo: Número más pequeño (más negativo)
        - max_negativo: -1 (número negativo más grande)
        - cero_positivo: 0
        - cero_negativo: 0 (representación alternativa)
        - min_positivo: 1
        - max_positivo: Número más grande
        - rango_negativos: Tupla (min_neg, max_neg)
        - rango_positivos: Tupla (min_pos, max_pos)
        - rango_total: Tupla (min_global, max_global)
        - magnitud_bits: Número de bits para magnitud (n-1)
        - capacidad: Total de valores diferentes (2^n - 1)
        - eficacia: Porcentaje de combinaciones usadas
    
    Ejemplo:
        rango_ms(8) retorna:
        {
            'min_negativo': -127,
            'max_negativo': -1,
            'min_positivo': 1,
            'max_positivo': 127,
            'rango_total': (-127, 127),
            'capacidad': 255,
            'eficacia': 0.9961 (99.61%)
        }
    """
    if n_bits < 2:
        raise ValueError("Se requieren al menos 2 bits (1 signo + 1 magnitud)")
    
    magnitud_bits = n_bits - 1
    max_magnitud = 2 ** magnitud_bits - 1
    
    min_negativo = -max_magnitud
    max_negativo = -1
    min_positivo = 1
    max_positivo = max_magnitud
    
    total_combinaciones = 2 ** n_bits
    capacidad = total_combinaciones - 1  # Menos 1 por la duplicación del 0
    eficacia = capacidad / total_combinaciones
    
    return {
        'min_negativo': min_negativo,
        'max_negativo': max_negativo,
        'cero': 0,
        'min_positivo': min_positivo,
        'max_positivo': max_positivo,
        'rango_negativos': (min_negativo, max_negativo),
        'rango_positivos': (min_positivo, max_positivo),
        'rango_total': (min_negativo, max_positivo),
        'magnitud_bits': magnitud_bits,
        'bits_totales': n_bits,
        'capacidad': capacidad,
        'total_combinaciones': total_combinaciones,
        'eficacia': eficacia,
        'porcentaje_eficacia': f"{eficacia*100:.2f}%"
    }


def analizar_ms(n_bits: int) -> str:
    """
    Análisis detallado de M&S para n bits.
    
    Retorna explicación en texto comprensible.
    """
    info = rango_ms(n_bits)
    
    texto = f"""
╔════════════════════════════════════════════════════════════════╗
║  ANÁLISIS: Magnitud y Signo con {info['bits_totales']} bits
╚════════════════════════════════════════════════════════════════╝

ESTRUCTURA:
  • Bit MSB (índice {info['magnitud_bits']}): Bit de signo (0=+, 1=-)
  • Bits {info['magnitud_bits']-1} hasta 0: Magnitud (valor absoluto)

RANGO DE VALORES:
  • Negativos: [{info['min_negativo']:6d}, {info['max_negativo']:6d}]
  • Positivos: [{info['min_positivo']:6d}, {info['max_positivo']:6d}]
  • Especial:  [0, -0] (dos representaciones del cero)
  
RANGO TOTAL: [{info['min_negativo']:6d}, {info['max_positivo']:6d}]

CAPACIDAD Y EFICIENCIA:
  • Combinaciones totales: 2^{info['bits_totales']} = {info['total_combinaciones']}
  • Valores representables: {info['capacidad']} (menos 1 por -0)
  • Eficacia: {info['porcentaje_eficacia']}

EJEMPLOS DE REPRESENTACIÓN:

Número +{info['max_positivo']}:
  Signo: 0 (positivo)
  Magnitud: {info['max_positivo']} en {info['magnitud_bits']} bits = {bin(info['max_positivo'])[2:].zfill(info['magnitud_bits'])}
  Representación: 0{bin(info['max_positivo'])[2:].zfill(info['magnitud_bits'])}

Número -{info['max_positivo']}:
  Signo: 1 (negativo)
  Magnitud: {info['max_positivo']} en {info['magnitud_bits']} bits = {bin(info['max_positivo'])[2:].zfill(info['magnitud_bits'])}
  Representación: 1{bin(info['max_positivo'])[2:].zfill(info['magnitud_bits'])}

Número +0:
  Representación: 0{'0' * info['magnitud_bits']}

Número -0:
  Representación: 1{'0' * info['magnitud_bits']}
"""
    return texto


# ============================================================================
# PARTE 2: CONVERSIÓN DECIMAL ↔ M&S
# ============================================================================

def decimal_a_ms(numero: int, n_bits: int) -> str:
    """
    Convierte un número decimal a M&S con n bits.
    
    Args:
        numero: Número decimal a convertir (int)
        n_bits: Número de bits total
    
    Returns:
        String con la representación en M&S
    
    Raises:
        ValueError: Si el número no cabe en el rango
    
    Ejemplo:
        decimal_a_ms(86, 8) → '01010110'
        decimal_a_ms(-86, 8) → '11010110'
        decimal_a_ms(0, 8) → '00000000' (+0)
    """
    info = rango_ms(n_bits)
    
    if numero < info['min_negativo'] or numero > info['max_positivo']:
        raise ValueError(
            f"Número {numero} fuera de rango [{info['min_negativo']}, {info['max_positivo']}] "
            f"para M&S con {n_bits} bits"
        )
    
    magnitud_bits = n_bits - 1
    
    if numero > 0:
        # Número positivo: bit de signo = 0
        signo_bit = '0'
        magnitud = numero
    elif numero < 0:
        # Número negativo: bit de signo = 1
        signo_bit = '1'
        magnitud = abs(numero)
    else:
        # Número cero: representación +0
        signo_bit = '0'
        magnitud = 0
    
    # Representar magnitud en binario con magnitud_bits dígitos
    magnitud_bin = bin(magnitud)[2:].zfill(magnitud_bits)
    
    return signo_bit + magnitud_bin


def ms_a_decimal(representacion_ms: str) -> int:
    """
    Convierte una representación M&S a decimal.
    
    Args:
        representacion_ms: String de 0s y 1s en M&S
    
    Returns:
        Número decimal equivalente
    
    Raises:
        ValueError: Si la representación no es válida
    
    Ejemplo:
        ms_a_decimal('01010110') → 86
        ms_a_decimal('11010110') → -86
        ms_a_decimal('00000000') → 0
        ms_a_decimal('10000000') → 0 (también -0)
    """
    if not representacion_ms:
        raise ValueError("Representación vacía")
    
    if not all(c in '01' for c in representacion_ms):
        raise ValueError(f"Caracteres inválidos en '{representacion_ms}'")
    
    n_bits = len(representacion_ms)
    magnitud_bits = n_bits - 1
    
    signo_bit = int(representacion_ms[0])
    magnitud_bits_str = representacion_ms[1:]
    magnitud = int(magnitud_bits_str, 2)
    
    if magnitud == 0:
        # El cero, independientemente del signo
        return 0
    
    # Si signo es 1, el número es negativo
    if signo_bit == 1:
        return -magnitud
    else:
        return magnitud


def explicar_conversion_ms(numero: int, n_bits: int) -> Dict[str, Union[int, str, Dict]]:
    """
    Explica paso a paso la conversión de decimal a M&S.
    
    Args:
        numero: Número decimal
        n_bits: Número de bits
    
    Returns:
        Dict con explicación detallada
    """
    info = rango_ms(n_bits)
    representacion = decimal_a_ms(numero, n_bits)
    
    magnitud_bits = n_bits - 1
    signo_bit = representacion[0]
    magnitud_bits_str = representacion[1:]
    magnitud = int(magnitud_bits_str, 2)
    
    return {
        'numero_decimal': numero,
        'n_bits': n_bits,
        'magnitud_bits': magnitud_bits,
        'en_rango': numero >= info['min_negativo'] and numero <= info['max_positivo'],
        'es_positivo': numero > 0,
        'es_negativo': numero < 0,
        'es_cero': numero == 0,
        'paso_1_signo': {
            'descripcion': 'Determinar el signo',
            'numero': numero,
            'signo': 'positivo (+)' if numero >= 0 else 'negativo (-)',
            'bit_signo': signo_bit,
            'significado': '0 = positivo, 1 = negativo'
        },
        'paso_2_magnitud': {
            'descripcion': 'Obtener la magnitud (valor absoluto)',
            'numero': numero,
            'magnitud': magnitud,
            'bits_disponibles': magnitud_bits,
            'conversion_binaria': {
                'magnitud_decimal': magnitud,
                'magnitud_binaria': magnitud_bits_str,
                'longitud': len(magnitud_bits_str)
            }
        },
        'paso_3_combinacion': {
            'descripcion': 'Combinar signo + magnitud',
            'signo_bit': signo_bit,
            'magnitud_bits': magnitud_bits_str,
            'representacion_final': representacion
        },
        'resultado_final': {
            'representacion': representacion,
            'formato': f"M&S{n_bits}",
            'valor_recuperado': ms_a_decimal(representacion)
        }
    }


# ============================================================================
# PARTE 3: OPERACIONES EN M&S
# ============================================================================

def negacion_ms(representacion_ms: str) -> str:
    """
    Obtiene el negativo de un número en M&S (multiplicación por -1).
    
    Operación: Invertir el bit de signo (flip)
    - 0 → 1 (positivo a negativo)
    - 1 → 0 (negativo a positivo)
    
    Args:
        representacion_ms: String en M&S
    
    Returns:
        String con la negación
    
    Ejemplo:
        negacion_ms('01010110') → '11010110'  (+86 → -86)
        negacion_ms('11010110') → '01010110'  (-86 → +86)
        negacion_ms('00000000') → '10000000'  (+0 → -0)
    """
    signo_bit = int(representacion_ms[0])
    magnitud_bits = representacion_ms[1:]
    
    nuevo_signo = 1 - signo_bit  # Flip del bit
    
    return str(nuevo_signo) + magnitud_bits


def es_positivo_ms(representacion_ms: str) -> bool:
    """¿El número es positivo o cero en M&S?"""
    return representacion_ms[0] == '0'


def es_negativo_ms(representacion_ms: str) -> bool:
    """¿El número es negativo en M&S?"""
    return representacion_ms[0] == '1'


def es_cero_ms(representacion_ms: str) -> bool:
    """¿El número es cero (en cualquier representación)?"""
    magnitud_bits = representacion_ms[1:]
    return all(c == '0' for c in magnitud_bits)


def valor_absoluto_ms(representacion_ms: str) -> int:
    """
    Obtiene el valor absoluto de un número en M&S.
    
    Ejemplo:
        valor_absoluto_ms('11010110') → 86
    """
    magnitud_bits = representacion_ms[1:]
    return int(magnitud_bits, 2)


def comparar_ms(rep_a: str, rep_b: str) -> int:
    """
    Compara dos números en M&S.
    
    Returns:
        -1 si A < B
         0 si A = B
         1 si A > B
    
    Nota: La comparación de números negativos es "invertida" en M&S.
    Ejemplo: -100 < -50, pero en M&S la magnitud de -100 es mayor.
    Por eso necesitamos este algoritmo especial.
    """
    val_a = ms_a_decimal(rep_a)
    val_b = ms_a_decimal(rep_b)
    
    if val_a < val_b:
        return -1
    elif val_a > val_b:
        return 1
    else:
        return 0


# ============================================================================
# PARTE 4: VALIDACIÓN Y ANÁLISIS
# ============================================================================

def validar_representacion_ms(representacion_ms: str, n_bits_esperado: int = None) -> Dict[str, Union[bool, str]]:
    """
    Valida que una representación sea válida en M&S.
    
    Args:
        representacion_ms: String a validar
        n_bits_esperado: Número de bits esperado (opcional)
    
    Returns:
        Dict con validación
    """
    errores = []
    
    # Validar caracteres
    if not all(c in '01' for c in representacion_ms):
        errores.append("Contiene caracteres que no son 0 o 1")
    
    # Validar longitud
    if len(representacion_ms) < 2:
        errores.append("Debe tener al menos 2 bits (1 signo + 1 magnitud)")
    
    # Validar longitud esperada
    if n_bits_esperado and len(representacion_ms) != n_bits_esperado:
        errores.append(f"Longitud {len(representacion_ms)}, se esperaba {n_bits_esperado}")
    
    return {
        'valida': len(errores) == 0,
        'errores': errores,
        'longitud': len(representacion_ms),
        'es_binario': all(c in '01' for c in representacion_ms) if representacion_ms else False
    }


def analizar_representacion_ms(representacion_ms: str) -> Dict:
    """
    Análisis completo de una representación en M&S.
    """
    validacion = validar_representacion_ms(representacion_ms)
    
    if not validacion['valida']:
        return {
            'valida': False,
            'errores': validacion['errores']
        }
    
    n_bits = len(representacion_ms)
    magnitud_bits = n_bits - 1
    
    signo_bit = int(representacion_ms[0])
    magnitud_bits_str = representacion_ms[1:]
    magnitud = int(magnitud_bits_str, 2)
    
    valor = ms_a_decimal(representacion_ms)
    
    rango_info = rango_ms(n_bits)
    
    return {
        'valida': True,
        'representacion': representacion_ms,
        'n_bits': n_bits,
        'estructura': {
            'bit_signo': f"bit {magnitud_bits} = {signo_bit}",
            'bits_magnitud': f"bits {magnitud_bits-1} a 0 = {magnitud_bits_str}",
            'signo_significado': 'positivo (+)' if signo_bit == 0 else 'negativo (-)'
        },
        'valor_decimal': valor,
        'magnitud': magnitud,
        'en_rango': valor >= rango_info['min_negativo'] and valor <= rango_info['max_positivo'],
        'es_positivo': valor > 0,
        'es_negativo': valor < 0,
        'es_cero': valor == 0,
        'es_positivo_cero': representacion_ms == '0' * n_bits,
        'es_negativo_cero': representacion_ms == '1' + '0' * magnitud_bits,
        'rango_disponible': rango_info['rango_total'],
        'negacion': negacion_ms(representacion_ms)
    }


# ============================================================================
# PARTE 5: CONSTRUCTORES Y UTILIDADES
# ============================================================================

def crear_cero_positivo_ms(n_bits: int) -> str:
    """
    Crea la representación de +0 en M&S.
    
    Ejemplo:
        crear_cero_positivo_ms(8) → '00000000'
    """
    return '0' * n_bits


def crear_cero_negativo_ms(n_bits: int) -> str:
    """
    Crea la representación de -0 en M&S.
    
    Ejemplo:
        crear_cero_negativo_ms(8) → '10000000'
    """
    magnitud_bits = n_bits - 1
    return '1' + '0' * magnitud_bits


def generar_tabla_ms(n_bits: int) -> List[Dict]:
    """
    Genera tabla completa de valores representables en M&S.
    
    Retorna lista de dicts con:
    - decimal: valor decimal
    - ms_representation: representación en M&S
    - signo: + o -
    - magnitud: valor absoluto
    """
    info = rango_ms(n_bits)
    tabla = []
    
    # Negativos
    for i in range(info['min_negativo'], 0):
        tabla.append({
            'decimal': i,
            'ms': decimal_a_ms(i, n_bits),
            'signo': '-',
            'magnitud': abs(i)
        })
    
    # Ceros
    tabla.append({
        'decimal': 0,
        'ms': crear_cero_positivo_ms(n_bits),
        'signo': '+',
        'magnitud': 0,
        'nota': '+0'
    })
    
    tabla.append({
        'decimal': 0,
        'ms': crear_cero_negativo_ms(n_bits),
        'signo': '-',
        'magnitud': 0,
        'nota': '-0 (duplicado)'
    })
    
    # Positivos
    for i in range(1, info['max_positivo'] + 1):
        tabla.append({
            'decimal': i,
            'ms': decimal_a_ms(i, n_bits),
            'signo': '+',
            'magnitud': i
        })
    
    return tabla


def mostrar_tabla_ms(n_bits: int) -> str:
    """
    Muestra tabla de M&S en formato legible.
    """
    tabla = generar_tabla_ms(n_bits)
    
    lineas = [
        f"╔ Tabla de Magnitud y Signo ({n_bits} bits) ╗",
        "┌──────────┬────────────┬──────┬───────────┐",
        "│ Decimal  │ M&S Repr.  │ Sign │ Magnitud  │",
        "├──────────┼────────────┼──────┼───────────┤"
    ]
    
    for entrada in tabla:
        decimal = entrada['decimal']
        ms = entrada['ms']
        signo = entrada['signo']
        magnitud = entrada['magnitud']
        nota = entrada.get('nota', '')
        
        linea = f"│ {decimal:8d} │ {ms:10s} │  {signo}   │ {magnitud:9d} │"
        if nota:
            linea += f"  {nota}"
        lineas.append(linea)
    
    lineas.append("└──────────┴────────────┴──────┴───────────┘")
    
    return "\n".join(lineas)
