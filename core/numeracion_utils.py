"""
Utilidades para conversiones numéricas.
Funciones para convertir entre sistemas de numeración usando métodos explícitos.
"""

from typing import Union, Tuple, List


def decimal_a_binario_divisiones(numero: Union[int, str], bits: int = None) -> str:
    """
    Convierte un número decimal a binario usando sucesivas divisiones por 2.
    
    Método: 
        - Dividir el número entre 2
        - Guardar el resto (0 o 1)
        - Continuar con el cociente
        - Repetir hasta cociente = 0
        - Los restos en orden inverso forman el binario
    
    Args:
        numero: Número decimal (int o str). Si es str, se convierte a int.
        bits: (Opcional) Número mínimo de bits para padding con ceros.
    
    Returns:
        String con el binario en formato claro: "10101₂" o "0b10101"
        Si bits se especifica, retorna con ese ancho: "00010101₂"
    
    Raises:
        ValueError: Si el input no es un número válido o es negativo.
    
    Ejemplos:
        >>> decimal_a_binario_divisiones("13")
        '1101₂'
        
        >>> decimal_a_binario_divisiones(255, bits=8)
        '11111111₂'
        
        >>> decimal_a_binario_divisiones(42, bits=8)
        '00101010₂'
    """
    
    # Validar y convertir entrada
    try:
        if isinstance(numero, str):
            numero = int(numero.strip())
        else:
            numero = int(numero)
    except (ValueError, TypeError):
        raise ValueError(f"No se puede convertir '{numero}' a número entero")
    
    if numero < 0:
        raise ValueError(f"El número debe ser no-negativo, recibido: {numero}")
    
    # Caso especial: cero
    if numero == 0:
        resultado = "0"
    else:
        # Método de divisiones sucesivas por 2
        restos: List[str] = []
        dividendo = numero
        
        while dividendo > 0:
            resto = dividendo % 2  # Resto de la división por 2
            restos.append(str(resto))  # Guardar resto
            dividendo = dividendo // 2  # Cociente entero
        
        # Los restos están en orden inverso, así que los invertimos
        resultado = "".join(reversed(restos))
    
    # Padding con ceros si se especifica número de bits
    if bits is not None:
        if len(resultado) > bits:
            raise ValueError(f"El número requiere más de {bits} bits (necesita {len(resultado)})")
        resultado = resultado.zfill(bits)
    
    # Retornar con notación clara de base 2
    return f"{resultado}₂"


def decimal_a_binario_con_pasos(numero: Union[int, str]) -> dict:
    """
    Convierte decimal a binario mostrando todos los pasos de las divisiones.
    
    Útil para fines educativos y demostraciones.
    
    Args:
        numero: Número decimal (int o str)
    
    Returns:
        Dict con:
        - 'numero': Número original
        - 'pasos': Lista de pasos [(dividendo, cociente, resto), ...]
        - 'restos': Lista de restos en orden
        - 'binario': Resultado final con notación "xxxxx₂"
        - 'explicacion': Texto explicativo del proceso
    
    Ejemplos:
        >>> resultado = decimal_a_binario_con_pasos("13")
        >>> print(resultado['explicacion'])
        13 ÷ 2 = 6 resto 1
        6 ÷ 2 = 3 resto 0
        3 ÷ 2 = 1 resto 1
        1 ÷ 2 = 0 resto 1
        
        Leyendo los restos de abajo hacia arriba: 1101₂
    """
    
    # Validar y convertir
    try:
        if isinstance(numero, str):
            numero_int = int(numero.strip())
        else:
            numero_int = int(numero)
    except (ValueError, TypeError):
        raise ValueError(f"No se puede convertir '{numero}' a número entero")
    
    if numero_int < 0:
        raise ValueError(f"El número debe ser no-negativo")
    
    numero_original = numero_int
    pasos = []
    restos = []
    
    if numero_int == 0:
        pasos.append((0, 0, 0))
        restos.append(0)
        binario_resultado = "0₂"
    else:
        dividendo = numero_int
        while dividendo > 0:
            cociente = dividendo // 2
            resto = dividendo % 2
            
            pasos.append((dividendo, cociente, resto))
            restos.append(resto)
            dividendo = cociente
        
        # Invertir restos para obtener el binario
        binario_resultado = "".join(str(r) for r in reversed(restos)) + "₂"
    
    # Construir explicación paso a paso
    explicacion_lineas = []
    for dividendo, cociente, resto in pasos:
        explicacion_lineas.append(f"{dividendo} ÷ 2 = {cociente} resto {resto}")
    
    explicacion_lineas.append("")
    explicacion_lineas.append(f"Leyendo los restos de abajo hacia arriba: {binario_resultado}")
    
    explicacion = "\n".join(explicacion_lineas)
    
    return {
        'numero': numero_original,
        'pasos': pasos,
        'restos': restos,
        'binario': binario_resultado,
        'explicacion': explicacion
    }


def decimal_a_binario_verbose(numero: Union[int, str]) -> str:
    """
    Convierte decimal a binario retornando tanto el resultado como los pasos.
    
    Formato retornado es un string con todos los pasos de forma visual.
    
    Args:
        numero: Número decimal (int o str)
    
    Returns:
        String con explicación completa del proceso de conversión
    
    Ejemplo:
        >>> print(decimal_a_binario_verbose("13"))
        Convertir 13 a binario (sucesivas divisiones por 2):
        
        13 ÷ 2 = 6 resto 1
         6 ÷ 2 = 3 resto 0
         3 ÷ 2 = 1 resto 1
         1 ÷ 2 = 0 resto 1
        
        Resultado: 1101₂
        
        (Leer los restos de abajo hacia arriba)
    """
    resultado = decimal_a_binario_con_pasos(numero)
    
    lineas = [
        f"Convertir {resultado['numero']} a binario (sucesivas divisiones por 2):",
        ""
    ]
    
    # Agregar pasos con indentación visual
    for i, (dividendo, cociente, resto) in enumerate(resultado['pasos']):
        espacios = " " * (1 if dividendo >= 10 else 0)
        lineas.append(f"{espacios}{dividendo} ÷ 2 = {cociente} resto {resto}")
    
    lineas.extend([
        "",
        f"Resultado: {resultado['binario']}",
        "",
        "(Leer los restos de abajo hacia arriba)"
    ])
    
    return "\n".join(lineas)


def validar_numero_decimal(numero: Union[int, str, float]) -> Tuple[bool, str]:
    """
    Valida si un input es un número decimal válido para conversiones.
    
    Args:
        numero: Input a validar
    
    Returns:
        Tupla (es_valido: bool, mensaje: str)
    
    Ejemplos:
        >>> validar_numero_decimal("42")
        (True, "42 es un número decimal válido")
        
        >>> validar_numero_decimal("-5")
        (False, "El número debe ser no-negativo")
    """
    try:
        if isinstance(numero, str):
            num = int(numero.strip())
        else:
            num = int(numero)
        
        if num < 0:
            return False, "El número debe ser no-negativo"
        
        return True, f"{num} es un número decimal válido"
    
    except (ValueError, TypeError):
        return False, f"'{numero}' no es un número decimal válido"


# Funciones adicionales para otras bases
def decimal_a_octal_divisiones(numero: Union[int, str], bits: int = None) -> str:
    """Convierte decimal a octal usando divisiones sucesivas por 8."""
    try:
        num = int(numero) if isinstance(numero, str) else int(numero)
    except (ValueError, TypeError):
        raise ValueError(f"No se puede convertir '{numero}' a número")
    
    if num < 0:
        raise ValueError("El número debe ser no-negativo")
    
    if num == 0:
        resultado = "0"
    else:
        digitos = []
        while num > 0:
            digitos.append(str(num % 8))
            num //= 8
        resultado = "".join(reversed(digitos))
    
    if bits is not None:
        resultado = resultado.zfill(bits)
    
    return f"{resultado}₈"


def decimal_a_hexadecimal_divisiones(numero: Union[int, str], bits: int = None) -> str:
    """Convierte decimal a hexadecimal usando divisiones sucesivas por 16."""
    try:
        num = int(numero) if isinstance(numero, str) else int(numero)
    except (ValueError, TypeError):
        raise ValueError(f"No se puede convertir '{numero}' a número")
    
    if num < 0:
        raise ValueError("El número debe ser no-negativo")
    
    digitos_hex = "0123456789ABCDEF"
    
    if num == 0:
        resultado = "0"
    else:
        digitos = []
        while num > 0:
            digitos.append(digitos_hex[num % 16])
            num //= 16
        resultado = "".join(reversed(digitos))
    
    if bits is not None:
        resultado = resultado.zfill(bits)
    
    return f"{resultado}₁₆"


# ============================================================================
# FUNCIONES GENERALIZADAS PARA CUALQUIER BASE (2-36)
# ============================================================================

def validar_base(base: int) -> bool:
    """
    Valida que una base esté en el rango permitido (2-36).
    
    Bases soportadas:
    - 2-10: Dígitos 0-9
    - 11-36: Dígitos 0-9 + Letras A-Z
    
    Args:
        base: Base numérica a validar
    
    Returns:
        True si la base es válida, False en caso contrario
    """
    return isinstance(base, int) and 2 <= base <= 36


def obtener_digitos_para_base(base: int) -> str:
    """
    Obtiene el conjunto de dígitos válidos para una base.
    
    Para bases 2-10: '0123456789'
    Para bases 11-36: '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    Args:
        base: Base numérica (2-36)
    
    Returns:
        String con los dígitos válidos para esa base
    
    Raises:
        ValueError: Si la base no está en rango 2-36
    """
    if not validar_base(base):
        raise ValueError(f"Base debe estar entre 2 y 36, recibido: {base}")
    
    return "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:base]


def decimal_a_base_b_divisiones(numero: Union[int, str], base: int, bits: int = None) -> str:
    """
    Convierte un número decimal a una base B (2-36) usando divisiones sucesivas.
    
    Método:
        - Dividir el número entre la base
        - Guardar el resto (dígito en la nueva base)
        - Continuar con el cociente
        - Repetir hasta cociente = 0
        - Los restos en orden inverso forman el resultado
    
    Args:
        numero: Número decimal (int o str)
        base: Base destino (2-36)
            - 2: Binario
            - 8: Octal
            - 10: Decimal (sin cambio)
            - 16: Hexadecimal
            - 36: Alphanumeric (máximo soportado)
        bits: (Opcional) Número mínimo de dígitos para padding
    
    Returns:
        String con el número en la base especificada, con subíndice
        Ej: "1A5₁₆", "373₈", "10101₂"
    
    Raises:
        ValueError: Si el input no es válido o base está fuera de rango
    
    Ejemplos:
        >>> decimal_a_base_b_divisiones(173, 2)  # Binario
        '10101101₂'
        
        >>> decimal_a_base_b_divisiones(255, 16)  # Hexadecimal
        'FF₁₆'
        
        >>> decimal_a_base_b_divisiones(100, 36)  # Base 36
        '2S₃₆'
        
        >>> decimal_a_base_b_divisiones(42, 8)  # Octal
        '52₈'
    """
    # Validar base
    if not validar_base(base):
        raise ValueError(f"Base debe estar entre 2 y 36, recibido: {base}")
    
    # Validar y convertir número
    try:
        if isinstance(numero, str):
            num = int(numero.strip())
        else:
            num = int(numero)
    except (ValueError, TypeError):
        raise ValueError(f"No se puede convertir '{numero}' a número entero")
    
    if num < 0:
        raise ValueError(f"El número debe ser no-negativo, recibido: {num}")
    
    # Obtener dígitos permitidos para esta base
    digitos = obtener_digitos_para_base(base)
    
    # Caso especial: cero
    if num == 0:
        resultado = "0"
    else:
        # Algoritmo de divisiones sucesivas
        digitos_resultado = []
        while num > 0:
            resto = num % base  # Dígito en la nueva base
            digitos_resultado.append(digitos[resto])  # Convertir a carácter
            num //= base  # Dividir entre la base
        
        # Los dígitos están en orden inverso
        resultado = "".join(reversed(digitos_resultado))
    
    # Padding si se especifica
    if bits is not None:
        if len(resultado) > bits:
            raise ValueError(f"Resultado requiere más de {bits} dígitos (necesita {len(resultado)})")
        resultado = resultado.zfill(bits)
    
    # Crear subíndice para la base
    # Convertir números de base > 9 a subíndice (ej: 16 → ₁₆)
    base_str = str(base)
    subindices = {
        '0': '₀', '1': '₁', '2': '₂', '3': '₃', '4': '₄',
        '5': '₅', '6': '₆', '7': '₇', '8': '₈', '9': '₉'
    }
    base_subindice = ''.join(subindices.get(d, d) for d in base_str)
    
    return f"{resultado}{base_subindice}"


def decimal_a_base_b_con_pasos(numero: Union[int, str], base: int) -> dict:
    """
    Convierte decimal a base B mostrando todos los pasos de las divisiones.
    
    Útil para fines educativos y demostraciones.
    
    Args:
        numero: Número decimal (int o str)
        base: Base destino (2-36)
    
    Returns:
        Dict con:
        - 'numero': Número original
        - 'base': Base destino
        - 'pasos': Lista de pasos [(dividendo, cociente, resto_digito), ...]
        - 'digitos': Lista de dígitos en orden inverso
        - 'resultado': Resultado final con notación "xxxxx_base"
        - 'explicacion': Texto explicativo del proceso
    
    Ejemplos:
        >>> resultado = decimal_a_base_b_con_pasos(255, 16)
        >>> print(resultado['resultado'])
        'FF₁₆'
    """
    # Validar base
    if not validar_base(base):
        raise ValueError(f"Base debe estar entre 2 y 36, recibido: {base}")
    
    # Validar y convertir
    try:
        if isinstance(numero, str):
            numero_int = int(numero.strip())
        else:
            numero_int = int(numero)
    except (ValueError, TypeError):
        raise ValueError(f"No se puede convertir '{numero}' a número entero")
    
    if numero_int < 0:
        raise ValueError("El número debe ser no-negativo")
    
    digitos_tabla = obtener_digitos_para_base(base)
    numero_original = numero_int
    pasos = []
    digitos = []
    
    if numero_int == 0:
        pasos.append((0, 0, "0"))
        digitos.append("0")
        base_str = str(base)
        subindices = {
            '0': '₀', '1': '₁', '2': '₂', '3': '₃', '4': '₄',
            '5': '₅', '6': '₆', '7': '₇', '8': '₈', '9': '₉'
        }
        base_subindice = ''.join(subindices.get(d, d) for d in base_str)
        resultado_final = f"0{base_subindice}"
    else:
        dividendo = numero_int
        while dividendo > 0:
            cociente = dividendo // base
            resto = dividendo % base
            digito_char = digitos_tabla[resto]
            
            pasos.append((dividendo, cociente, digito_char))
            digitos.append(digito_char)
            dividendo = cociente
        
        # Invertir dígitos para obtener el resultado
        resultado = "".join(reversed(digitos))
        
        base_str = str(base)
        subindices = {
            '0': '₀', '1': '₁', '2': '₂', '3': '₃', '4': '₄',
            '5': '₅', '6': '₆', '7': '₇', '8': '₈', '9': '₉'
        }
        base_subindice = ''.join(subindices.get(d, d) for d in base_str)
        resultado_final = f"{resultado}{base_subindice}"
    
    # Construir explicación paso a paso
    explicacion_lineas = []
    explicacion_lineas.append(f"Convirtiendo {numero_original} a base {base}:")
    explicacion_lineas.append("")
    
    for dividendo, cociente, digito in pasos:
        explicacion_lineas.append(f"{dividendo} ÷ {base} = {cociente} resto {digito}")
    
    explicacion_lineas.append("")
    explicacion_lineas.append(f"Leyendo los restos de abajo hacia arriba: {resultado_final}")
    
    explicacion = "\n".join(explicacion_lineas)
    
    return {
        'numero': numero_original,
        'base': base,
        'pasos': pasos,
        'digitos': digitos,
        'resultado': resultado_final,
        'explicacion': explicacion
    }


def decimal_a_base_b_verbose(numero: Union[int, str], base: int) -> str:
    """
    Convierte decimal a base B retornando explicación visual completa.
    
    Args:
        numero: Número decimal (int o str)
        base: Base destino (2-36)
    
    Returns:
        String con explicación completa del proceso de conversión
    """
    resultado = decimal_a_base_b_con_pasos(numero, base)
    
    lineas = [
        f"Convertir {resultado['numero']} a base {resultado['base']} (divisiones sucesivas):",
        ""
    ]
    
    # Agregar pasos con indentación visual
    for dividendo, cociente, digito in resultado['pasos']:
        espacios = " " * (len(str(dividendo)) - 2) if dividendo >= 10 else ""
        lineas.append(f"{espacios}{dividendo} ÷ {base} = {cociente} resto {digito}")
    
    lineas.extend([
        "",
        f"Resultado: {resultado['resultado']}",
        "",
        "(Leer los restos de abajo hacia arriba)"
    ])
    
    return "\n".join(lineas)
