import random
from typing import Dict, Any
from core.generator_base import ExerciseGenerator, ExerciseRandomizer
from modules.numeracion.models import ConversionExerciseData, ConversionRow, ArithmeticOp

class ConversionRowRandomizer(ExerciseRandomizer):
    """ALEATORIZADOR: Genera parámetros del problema para ConversionRow."""
    
    def topic(self) -> str:
        return "Representación Numérica"
    
    def randomize(self, seed: int | None = None) -> Dict[str, Any]:
        """
        Genera parámetros del PROBLEMA de forma aleatoria.
        
        Returns:
            Dict con los parámetros del problema, listo para pasar al generador.
        """
        if seed is not None:
            random.seed(seed)
        
        n_bits = 8
        col_idx = random.choice([1, 1, 2, 3, 3, 4, 4, 5])
        val = 0
        text_val = ""
        
        es_signed = col_idx in [1, 3, 4]
        sign = -1 if (es_signed and random.random() < 0.7) else 1
        
        if col_idx == 1:  # Decimal
            val = sign * random.randint(0, 120)
            text_val = str(val)
        elif col_idx == 2:  # Binario Natural
            val = random.randint(0, 255)
            text_val = self._int_to_bin(val, n_bits)
        elif col_idx == 3:  # C2
            val = sign * random.randint(0, 127)
            text_val = self._int_to_bin(val, n_bits)
        elif col_idx == 4:  # SM
            val = sign * random.randint(0, 127)
            text_val = self._int_to_sm(val, n_bits)
        elif col_idx == 5:  # BCD
            val = random.randint(0, 99)
            text_val = self._int_to_bcd(val)
        
        # Retornar SOLO los parámetros del problema
        return {
            'label': random.choice(['a', 'b', 'c', 'd']),
            'val_decimal': val,
            'target_col_idx': col_idx,
            'representable': text_val != "NR"
        }
    
    def _int_to_bin(self, val: int, bits: int) -> str:
        return format(val if val >= 0 else (1 << bits) + val, f'0{bits}b')
    
    def _int_to_bcd(self, val: int) -> str:
        if not (0 <= val <= 99): return "NR"
        return f"{val // 10:04b} {val % 10:04b}"
    
    def _int_to_sm(self, val: int, bits: int) -> str:
        if val >= 0: return format(val, f'0{bits}b')
        return '1' + format(abs(val), f'0{bits - 1}b')


class ConversionRowGenerator(ExerciseGenerator):
    """GENERADOR: Calcula solución para ConversionRow."""
    
    def topic(self) -> str:
        return "Representación Numérica"
    
    def generate_from_problem(self, problem_dict: Dict[str, Any]) -> ConversionRow:
        """
        DETERMINISTA: Recibe parámetros del problema y calcula solución.
        
        Args:
            problem_dict: {
                'label': 'a',
                'val_decimal': 157,
                'target_col_idx': 0,
                'representable': True
            }
        
        Returns:
            ConversionRow: Ejercicio completo (problema + solución).
        """
        label = problem_dict['label']
        val_decimal = problem_dict['val_decimal']
        target_col_idx = problem_dict['target_col_idx']
        representable = problem_dict['representable']
        
        n_bits = 8
        
        # CALCULAR SOLUCIÓN (determinista, basada en val_decimal)
        sol_bin = self._int_to_bin(val_decimal, n_bits) if 0 <= val_decimal <= 255 else "NR"
        sol_c2 = self._int_to_bin(val_decimal, n_bits) if -128 <= val_decimal <= 127 else "NR"
        sol_sm = self._int_to_sm(val_decimal, n_bits) if -127 <= val_decimal <= 127 else "NR"
        sol_bcd = self._int_to_bcd(val_decimal)
        
        # Determinar target_val_str según target_col_idx
        if target_col_idx == 1:  # Decimal
            target_val_str = str(val_decimal)
        elif target_col_idx == 2:  # Binario Natural
            target_val_str = sol_bin
        elif target_col_idx == 3:  # C2
            target_val_str = sol_c2
        elif target_col_idx == 4:  # SM
            target_val_str = sol_sm
        elif target_col_idx == 5:  # BCD
            target_val_str = sol_bcd
        else:
            target_val_str = "ERROR"
        
        return ConversionRow(
            title="Conversión entre Bases Numéricas",
            description=f"Convertir {val_decimal} a múltiples sistemas",
            label=label,
            val_decimal=val_decimal,
            target_col_idx=target_col_idx,
            representable=representable,
            target_val_str=target_val_str,
            sol_bin=sol_bin,
            sol_c2=sol_c2,
            sol_sm=sol_sm,
            sol_bcd=sol_bcd
        )
    
    def _int_to_bin(self, val: int, bits: int) -> str:
        return format(val if val >= 0 else (1 << bits) + val, f'0{bits}b')
    
    def _int_to_bcd(self, val: int) -> str:
        if not (0 <= val <= 99): return "NR"
        return f"{val // 10:04b} {val % 10:04b}"
    
    def _int_to_sm(self, val: int, bits: int) -> str:
        if val >= 0: return format(val, f'0{bits}b')
        return '1' + format(abs(val), f'0{bits - 1}b')


class BinaryConversionGenerator(ExerciseGenerator):
    """GENERADOR LEGACY: Compatible hacia atrás."""
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

    def generate_from_problem(self, problem_dict: Dict[str, Any]) -> ConversionExerciseData:
        """
        NOTA: Este método no se usa en BinaryConversionGenerator (opera a nivel de ejercicio completo).
        """
        raise NotImplementedError("BinaryConversionGenerator opera a nivel de ejercicio completo")

    def generate(self, difficulty: int = 1) -> ConversionExerciseData:
        """
        MÉTODO LEGACY: Genera ejercicio completo con tabla de conversión.
        Utiliza aleatorizador internamente para mantener compatibilidad.
        """
        n_bits = 8
        rows = []
        labels = ['a', 'b', 'c', 'd']
        saved_vals = {}
        
        randomizer = ConversionRowRandomizer()

        for label in labels:
            # Usar aleatorizador
            problem = randomizer.randomize(seed=None)
            
            # Usar generador
            generator = ConversionRowGenerator()
            row = generator.generate_from_problem(problem)
            
            rows.append(row)
            saved_vals[label] = problem['val_decimal']

        ops = []
        if len(saved_vals) >= 2:
            for _ in range(2):
                l1 = random.choice(labels)
                l2 = random.choice([l for l in labels if l != l1])
                v1 = saved_vals[l1]
                v2 = saved_vals[l2]
                
                is_sum = random.choice([True, False])
                res = v1 + v2 if is_sum else v1 - v2
                
                ops.append(ArithmeticOp(
                    title="Operación Aritmética",
                    description=f"Realizar {'suma' if is_sum else 'resta'} en {random.choice(['binario', 'complemento a 2'])}",
                    op_type="suma" if is_sum else "resta",
                    system=random.choice(['binario', 'c2']),
                    operand1=l1,
                    operand2=l2,
                    operator_symbol="+" if is_sum else "-",
                    val1_dec=v1,
                    val2_dec=v2,
                    result_dec=res,
                    result_bin=self._int_to_bin(res, n_bits),
                    overflow=False,
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
