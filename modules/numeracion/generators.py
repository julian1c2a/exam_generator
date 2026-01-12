import random
from core.generator_base import ExerciseGenerator
from modules.numeracion.models import ConversionExerciseData, ConversionRow, ArithmeticOp

class BinaryConversionGenerator(ExerciseGenerator):
    def topic(self) -> str:
        return "Representación Numérica"

    def _int_to_bin(self, val: int, bits: int) -> str:
        return format(val if val >= 0 else (1 << bits) + val, f'0{bits}b')

    def _int_to_bcd(self, val: int) -> str:
        if not (0 <= val <= 99): return "NR"
        return f"{val // 10:04b} {val % 10:04b}"

    def _int_to_sm(self, val: int, bits: int) -> str:
        if val >= 0: return format(val, f'0{bits}b')
        return '1' + format(abs(val), f'0{bits - 1}b')

    def generate(self, difficulty: int = 1) -> ConversionExerciseData:
        n_bits = 8
        rows = []
        labels = ['a', 'b', 'c', 'd']
        saved_vals = {} # Diccionario para acceso rápido por etiqueta

        for label in labels:
            col_idx = random.choice([1, 1, 2, 3, 3, 4, 4, 5])
            val = 0
            text_val = ""

            es_signed = col_idx in [1, 3, 4]
            sign = -1 if (es_signed and random.random() < 0.7) else 1

            if col_idx == 1: # Decimal
                val = sign * random.randint(0, 120)
                text_val = str(val)
            elif col_idx == 2: # Binario Nat
                val = random.randint(0, 255)
                text_val = self._int_to_bin(val, n_bits)
            elif col_idx == 3: # C2
                val = sign * random.randint(0, 127)
                text_val = self._int_to_bin(val, n_bits)
            elif col_idx == 4: # SM
                val = sign * random.randint(0, 127)
                text_val = self._int_to_sm(val, n_bits)
            elif col_idx == 5: # BCD
                val = random.randint(0, 99)
                text_val = self._int_to_bcd(val)

            # Calcular soluciones
            sol_bin = self._int_to_bin(val, n_bits) if 0 <= val <= 255 else "NR"
            sol_c2 = self._int_to_bin(val, n_bits) if -128 <= val <= 127 else "NR"
            sol_sm = self._int_to_sm(val, n_bits) if -127 <= val <= 127 else "NR"
            sol_bcd = self._int_to_bcd(val)

            rows.append(ConversionRow(label, val, col_idx, text_val, sol_bin, sol_c2, sol_sm, sol_bcd))
            saved_vals[label] = val

        ops = []
        if len(saved_vals) >= 2:
            for _ in range(2):
                l1 = random.choice(labels)
                l2 = random.choice([l for l in labels if l != l1])
                v1 = saved_vals[l1]
                v2 = saved_vals[l2]
                
                is_sum = random.choice([True, False])
                res = v1 + v2 if is_sum else v1 - v2
                
                # Simulación de acarreo (simplificada para visualización)
                # En un sistema real habría que simular la ALU bit a bit para obtener los acarreos intermedios
                # Por ahora dejaremos carry_bits vacío o simulado si es necesario
                
                ops.append(ArithmeticOp(
                    op_type="Suma" if is_sum else "Resta",
                    system=random.choice(['Binario Natural', 'Complemento a 2']),
                    operand1=l1,
                    operand2=l2,
                    operator_symbol="+" if is_sum else "-",
                    val1_dec=v1,
                    val2_dec=v2,
                    result_dec=res,
                    result_bin=self._int_to_bin(res, n_bits), # Ojo: esto asume C2 para negativos
                    overflow=False, # TODO: Calcular overflow real
                    underflow=False,
                    carry_bits=""
                ))

        return ConversionExerciseData(
            title="Sistemas de Representación",
            description=f"Complete la tabla. Registro de {n_bits} bits.",
            n_bits=n_bits,
            rows=rows,
            operations=ops
        )
