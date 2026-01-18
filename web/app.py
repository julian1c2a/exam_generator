#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GeneratorFEExercises - Web Server (Fase 7)
Interfaz Web Interactiva para simuladores de números

Simuladores Disponibles:
  1. IEEE754 Interactivo - Visualización bit a bit
  2. Calculadora de Bases - Conversiones paso a paso
  3. Visualizador de Distribución - Gráficas comparativas

Uso:
    python app.py
    # Accede a http://localhost:5000
"""

import os
import sys
from pathlib import Path

from flask import Flask, render_template, jsonify, request
from flask_cors import CORS

# Agregar core/ al path para importar módulos
SCRIPT_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(SCRIPT_DIR))

try:
    from core.ieee754 import IEEE754Gen
    from core.punto_fijo_unified import FixedPointUnified
except ImportError as e:
    print(f"Error importando módulos core: {e}")
    sys.exit(1)

# ============================================================================
# Configuración Flask
# ============================================================================

app = Flask(__name__, 
            template_folder='templates',
            static_folder='static')

# Habilitar CORS
CORS(app)

# Configuración
app.config['JSON_SORT_KEYS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# ============================================================================
# Rutas principales (HTML)
# ============================================================================

@app.route('/')
def index():
    """Página principal - Menú de simuladores"""
    return render_template('index.html')

@app.route('/ieee754')
def ieee754_simulator():
    """Simulador IEEE754 Interactivo"""
    return render_template('ieee754.html')

@app.route('/converter')
def converter():
    """Calculadora de Conversión de Bases"""
    return render_template('converter.html')

@app.route('/distribution')
def distribution_visualizer():
    """Visualizador de Distribución de Números"""
    return render_template('distribution.html')

@app.route('/bcd-biquinario')
def bcd_biquinario():
    """Convertidor BCD y Biquinario"""
    return render_template('bcd-biquinario.html')

# ============================================================================
# API: IEEE754
# ============================================================================

@app.route('/api/ieee754/encode', methods=['POST'])
def ieee754_encode():
    """Codificar número decimal a IEEE754"""
    try:
        data = request.get_json()
        value = float(data.get('value'))
        base = int(data.get('base', 2))
        E_bits = int(data.get('E_bits', 8))
        F_bits = int(data.get('F_bits', 23))
        
        ieee = IEEE754Gen(base=base, E_bits=E_bits, F_bits=F_bits)
        encoded = ieee.encode(value)
        bits = bin(encoded)[2:].zfill(1 + E_bits + F_bits)
        hex_repr = hex(encoded)
        decoded = ieee.decode(encoded)
        
        return jsonify({
            'success': True,
            'value': value,
            'bits': bits,
            'hex': hex_repr,
            'sign': bits[0],
            'exponent': bits[1:1+E_bits],
            'mantissa': bits[1+E_bits:],
            'decoded': decoded,
            'valid': True
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@app.route('/api/ieee754/characteristics', methods=['POST'])
def ieee754_characteristics():
    """Obtener características de IEEE754"""
    try:
        data = request.get_json()
        base = int(data.get('base', 2))
        E_bits = int(data.get('E_bits', 8))
        F_bits = int(data.get('F_bits', 23))
        
        ieee = IEEE754Gen(base=base, E_bits=E_bits, F_bits=F_bits)
        
        return jsonify({
            'success': True,
            'base': base,
            'E_bits': E_bits,
            'F_bits': F_bits,
            'total_bits': 1 + E_bits + F_bits,
            'E_min': ieee.E_min,
            'E_max': ieee.E_max,
            'min_positive': float(ieee.min_positive),
            'max_positive': float(ieee.max_positive),
            'epsilon': float(ieee.epsilon_machine)
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@app.route('/api/ieee754/special', methods=['POST'])
def ieee754_special():
    """Obtener números especiales (∞, NaN, etc)"""
    try:
        data = request.get_json()
        base = int(data.get('base', 2))
        E_bits = int(data.get('E_bits', 8))
        F_bits = int(data.get('F_bits', 23))
        
        total_bits = 1 + E_bits + F_bits
        E_all_ones = (1 << E_bits) - 1
        
        # Representaciones especiales
        zero_bits = 0
        neg_zero_bits = 1 << (total_bits - 1)
        inf_bits = (E_all_ones << F_bits)
        neg_inf_bits = (1 << (total_bits - 1)) | inf_bits
        qnan_bits = inf_bits | (1 << (F_bits - 1))
        snan_bits = neg_inf_bits | 1
        
        def to_bits(value):
            return bin(value)[2:].zfill(total_bits)
        
        return jsonify({
            'success': True,
            'base': base,
            'E_bits': E_bits,
            'F_bits': F_bits,
            'total_bits': total_bits,
            'positive_zero': to_bits(zero_bits),
            'negative_zero': to_bits(neg_zero_bits),
            'positive_infinity': to_bits(inf_bits),
            'negative_infinity': to_bits(neg_inf_bits),
            'qnan': to_bits(qnan_bits),
            'snan': to_bits(snan_bits)
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

# ============================================================================
# API: Convertidor de Bases
# ============================================================================

@app.route('/api/convert', methods=['POST'])
def convert_bases():
    """Convertir número entre múltiples bases"""
    try:
        data = request.get_json()
        value = str(data.get('value')).strip()
        from_base = int(data.get('from_base', 10))
        to_bases = data.get('to_bases', [2, 8, 10, 16])
        
        # Convertir a decimal
        if from_base == 10:
            decimal_value = int(value)
        else:
            decimal_value = int(value, from_base)
        
        # Convertir a cada base solicitada
        results = {}
        for target_base in to_bases:
            if target_base == 10:
                result_value = str(decimal_value)
            elif target_base == 2:
                result_value = bin(decimal_value)[2:]
            elif target_base == 8:
                result_value = oct(decimal_value)[2:]
            elif target_base == 16:
                result_value = hex(decimal_value)[2:].upper()
            else:
                # Conversión genérica
                if decimal_value == 0:
                    result_value = '0'
                else:
                    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                    result_value = ''
                    temp = decimal_value
                    while temp > 0:
                        result_value = digits[temp % target_base] + result_value
                        temp //= target_base
            
            results[str(target_base)] = {
                'value': result_value,
                'decimal': decimal_value
            }
        
        return jsonify({
            'success': True,
            'value': value,
            'from_base': from_base,
            'decimal_equivalent': decimal_value,
            'results': results
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

# ============================================================================
# API: Distribución
# ============================================================================

@app.route('/api/distribution/fixed_point', methods=['POST'])
def distribution_fixed_point():
    """Analizar distribución de números en punto fijo"""
    try:
        data = request.get_json()
        E = int(data.get('E', 4))
        F = int(data.get('F', 4))
        representation = data.get('representation', 'unsigned')
        
        fp = FixedPointUnified(E=E, F=F, base=2, 
                              signed=(representation != 'unsigned'),
                              representation=representation if representation != 'unsigned' else None)
        
        total_bits = E + F
        total_numbers = 2 ** total_bits
        
        return jsonify({
            'success': True,
            'E': E,
            'F': F,
            'representation': representation,
            'min_value': float(fp.min_value),
            'max_value': float(fp.max_value),
            'epsilon': float(fp.epsilon),
            'total_bits': total_bits,
            'total_numbers': total_numbers,
            'statistics': {
                'range': [float(fp.min_value), float(fp.max_value)],
                'gap_min': float(fp.epsilon),
                'gap_max': float(fp.epsilon),
                'uniform': True
            }
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@app.route('/api/distribution/chart-data', methods=['POST'])
def distribution_chart_data():
    """Obtener datos para gráfica de distribución (Chart.js compatible)"""
    try:
        data = request.get_json()
        E = int(data.get('E', 4))
        F = int(data.get('F', 4))
        representation = data.get('representation', 'unsigned')
        
        fp = FixedPointUnified(E=E, F=F, base=2, 
                              signed=(representation != 'unsigned'),
                              representation=representation if representation != 'unsigned' else None)
        
        total_bits = E + F
        total_numbers = 2 ** total_bits
        
        # Generar datos de frecuencia para gráfica de distribución
        # Dividir rango en 50 bins para visualización
        min_val = float(fp.min_value)
        max_val = float(fp.max_value)
        epsilon = float(fp.epsilon)
        
        # Crear bins
        num_bins = min(50, total_numbers)
        bin_width = (max_val - min_val) / num_bins if max_val > min_val else 1.0
        
        labels = []
        frequencies = []
        
        for i in range(num_bins):
            bin_start = min_val + (i * bin_width)
            bin_end = bin_start + bin_width
            bin_center = (bin_start + bin_end) / 2
            
            # Estimar frecuencia (uniforme en punto fijo)
            if max_val > min_val:
                frequency = total_numbers / num_bins
            else:
                frequency = total_numbers
            
            labels.append(f"{bin_center:.2f}")
            frequencies.append(frequency)
        
        return jsonify({
            'success': True,
            'chart_type': 'bar',
            'E': E,
            'F': F,
            'representation': representation,
            'labels': labels,
            'datasets': [
                {
                    'label': f'Distribución de Números ({representation})',
                    'data': frequencies,
                    'backgroundColor': 'rgba(75, 192, 192, 0.6)',
                    'borderColor': 'rgba(75, 192, 192, 1)',
                    'borderWidth': 1,
                    'tension': 0.1
                }
            ],
            'statistics': {
                'min': min_val,
                'max': max_val,
                'epsilon': epsilon,
                'total_numbers': total_numbers,
                'total_bits': total_bits,
                'uniform': True,
                'gap_type': 'uniforme'
            }
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

# ============================================================================
# API: Representaciones Especiales - BCD y Biquinarios
# ============================================================================

@app.route('/api/representations/bcd', methods=['POST'])
def bcd_conversion():
    """Convertir número decimal a BCD (Binary Coded Decimal)"""
    try:
        data = request.get_json()
        number = int(data.get('number', 0))
        
        # Validar rango
        if number < 0 or number > 9999:
            return jsonify({
                'success': False,
                'error': 'BCD soporta números de 0 a 9999'
            }), 400
        
        # Convertir a BCD
        bcd_str = ''
        temp = number
        for _ in range(4):
            digit = temp % 10
            bcd_str = format(digit, '04b') + bcd_str
            temp //= 10
        
        bcd_str = bcd_str.lstrip('0') or '0000'
        
        # Generar visualización de nibbles
        nibbles = []
        for digit in str(number).zfill(4):
            nibbles.append({
                'digit': int(digit),
                'binary': format(int(digit), '04b'),
                'hex': format(int(digit), 'x')
            })
        
        return jsonify({
            'success': True,
            'number': number,
            'bcd_binary': bcd_str,
            'bcd_hex': hex(int(bcd_str, 2)),
            'bcd_decimal': int(bcd_str, 2),
            'nibbles': nibbles,
            'total_bits': len(bcd_str),
            'info': {
                'name': 'Binary Coded Decimal',
                'description': 'Cada dígito decimal se codifica en 4 bits',
                'range': '0-9999',
                'bits_per_digit': 4
            }
        })
    
    except ValueError:
        return jsonify({
            'success': False,
            'error': 'Número inválido'
        }), 400
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@app.route('/api/representations/biquinario', methods=['POST'])
def biquinario_conversion():
    """Convertir número decimal a Biquinario (7 bits)"""
    try:
        data = request.get_json()
        number = int(data.get('number', 0))
        
        # Validar rango (0-99)
        if number < 0 or number > 99:
            return jsonify({
                'success': False,
                'error': 'Biquinario soporta números de 0 a 99'
            }), 400
        
        # Sistema Biquinario: 7 bits (5, 4, 3, 2, 1, 0)
        # Primeros 2 bits: quinario (0-4), últimos 5 bits: binario (0-1)
        
        quinary = number // 5      # Primer dígito (0-4 cuando number < 99)
        binary_part = number % 5   # Segundo dígito (0-4)
        
        # Binario de 3 bits para cada parte
        quinary_bin = format(quinary, '02b')
        binary_bin = format(binary_part, '03b')
        
        biquia_full = quinary_bin + binary_bin
        
        return jsonify({
            'success': True,
            'number': number,
            'biquinario': biquia_full,
            'biquinario_hex': hex(int(biquia_full, 2)),
            'biquinario_decimal': int(biquia_full, 2),
            'components': {
                'quinario_part': {
                    'value': quinary,
                    'binary': quinary_bin,
                    'position': '5-4'
                },
                'binary_part': {
                    'value': binary_part,
                    'binary': binary_bin,
                    'position': '3-2-1'
                }
            },
            'total_bits': len(biquia_full),
            'info': {
                'name': 'Biquinario',
                'description': 'Sistema de 2 dígitos: uno quinario (base 5) y otro binario',
                'range': '0-99',
                'structure': '2 bits quinario + 3 bits binario'
            }
        })
    
    except ValueError:
        return jsonify({
            'success': False,
            'error': 'Número inválido'
        }), 400
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@app.route('/api/representations/compare', methods=['POST'])
def compare_representations():
    """Comparar múltiples representaciones de un número"""
    try:
        data = request.get_json()
        number = int(data.get('number', 0))
        
        representations = {}
        
        # Binario
        try:
            representations['binary'] = format(number, 'b')
        except:
            representations['binary'] = 'N/A'
        
        # Octal
        try:
            representations['octal'] = oct(number)[2:]
        except:
            representations['octal'] = 'N/A'
        
        # Hexadecimal
        try:
            representations['hexadecimal'] = hex(number)[2:]
        except:
            representations['hexadecimal'] = 'N/A'
        
        # BCD (si está en rango)
        if 0 <= number <= 9999:
            bcd_str = ''
            temp = number
            for _ in range(4):
                digit = temp % 10
                bcd_str = format(digit, '04b') + bcd_str
                temp //= 10
            representations['bcd'] = bcd_str.lstrip('0') or '0000'
        
        # Biquinario (si está en rango)
        if 0 <= number <= 99:
            quinary = number // 5
            binary_part = number % 5
            biq = format(quinary, '02b') + format(binary_part, '03b')
            representations['biquinario'] = biq
        
        return jsonify({
            'success': True,
            'decimal': number,
            'representations': representations,
            'comparison': {
                'total_representations': len(representations),
                'max_bits': max(len(str(v)) for v in representations.values() if v != 'N/A')
            }
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

# ============================================================================
# API: Health Check
# ============================================================================

@app.route('/api/health', methods=['GET'])
def health_check():
    """Verificar que el servidor está activo"""
    return jsonify({
        'status': 'ok',
        'version': '7.0.0',
        'message': 'GeneratorFEExercises Web API - Fase 7'
    })

# ============================================================================
# Error Handlers
# ============================================================================

@app.errorhandler(404)
def not_found(error):
    """Manejar rutas no encontradas"""
    return jsonify({
        'success': False,
        'error': 'Ruta no encontrada',
        'status': 404
    }), 404

@app.errorhandler(500)
def server_error(error):
    """Manejar errores del servidor"""
    return jsonify({
        'success': False,
        'error': 'Error interno del servidor',
        'status': 500
    }), 500

# ============================================================================
# Main
# ============================================================================

if __name__ == '__main__':
    print("""
╔════════════════════════════════════════════════════════════════════╗
║  GeneratorFEExercises - Web UI (Fase 7)                            ║
║                                                                    ║
║  Iniciando servidor en http://localhost:5000                      ║
║                                                                    ║
║  Simuladores Disponibles:                                          ║
║    • IEEE754 Interactivo:  http://localhost:5000/ieee754          ║
║    • Calculadora de Bases: http://localhost:5000/converter        ║
║    • Visualizador:         http://localhost:5000/distribution     ║
║                                                                    ║
║  API Endpoints:                                                    ║
║    POST   /api/ieee754/encode                                     ║
║    POST   /api/ieee754/characteristics                            ║
║    POST   /api/ieee754/special                                    ║
║    POST   /api/convert                                            ║
║    POST   /api/distribution/fixed_point                           ║
║    GET    /api/health                                             ║
║                                                                    ║
║  Presiona CTRL+C para detener                                     ║
╚════════════════════════════════════════════════════════════════════╝
    """)
    
    app.run(debug=True, host='localhost', port=5000)
