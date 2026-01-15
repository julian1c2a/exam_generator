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
