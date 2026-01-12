import random
import json
from typing import List
from exam_model import *

class ExamGenerator:
    def __init__(self, scenarios_file: str):
        with open(scenarios_file, 'r', encoding='utf-8') as f:
            self.scenarios = json.load(f)

    def _int_to_bin(self, val: int, bits: int) -> str:
        return format(val if val >= 0 else (1 << bits) + val, f'0{bits}b')

    def _int_to_bcd(self, val: int) -> str:
        if not (0 <= val <= 99): return "NR"
        return f"{val // 10:04b} {val % 10:04b}"

    def _int_to_sm(self, val: int, bits: int) -> str:
        if val >= 0: return format(val, f'0{bits}b')
        return '1' + format(abs(val), f'0{bits - 1}b')

    def generate_ej1(self) -> Exercise1Data:
        rows = []
        labels = ['a', 'b', 'c', 'd']
        saved_vals = [] # Para las operaciones

        for label in labels:
            col_idx = random.choice([1, 1, 2, 3, 3, 4, 4, 5]) # Ponderado
            val = 0
            text_val = ""

            # Generar valor válido según columna
            es_signed = col_idx in [1, 3, 4]
            sign = -1 if (es_signed and random.random() < 0.7) else 1

            if col_idx == 1: # Decimal
                val = sign * random.randint(0, 120)
                text_val = str(val)
            elif col_idx == 2: # Binario Nat
                val = random.randint(0, 255)
                text_val = self._int_to_bin(val, 8)
            elif col_idx == 3: # C2
                val = sign * random.randint(0, 127)
                text_val = self._int_to_bin(val, 8)
            elif col_idx == 4: # SM
                val = sign * random.randint(0, 127)
                text_val = self._int_to_sm(val, 8)
            elif col_idx == 5: # BCD
                val = random.randint(0, 99)
                text_val = self._int_to_bcd(val)

            rows.append(ConversionRow(label, val, col_idx, text_val))
            saved_vals.append((label, val))

        ops = []
        if len(saved_vals) >= 2:
            for _ in range(2):
                f1 = random.choice(saved_vals)
                f2 = random.choice([x for x in saved_vals if x != f1])
                is_sum = random.choice([True, False])
                ops.append(ArithmeticOp(
                    op_type="Suma" if is_sum else "Resta",
                    system=random.choice(['Binario Natural', 'Complemento a 2']),
                    operand1=f1[0],
                    operand2=f2[0],
                    operator_symbol="+" if is_sum else "-"
                ))

        return Exercise1Data(rows, ops, 8)

    def generate_ej2(self) -> Exercise2Data:
        es_minterms = random.choice([True, False])
        target = 1 if es_minterms else 0
        default = 0 if es_minterms else 1
        outputs = [default] * 16

        # Generar grupos adyacentes para asegurar simplificación
        for _ in range(random.randint(3, 6)):
            idx1 = random.randint(0, 15)
            idx2 = idx1 ^ (1 << random.randint(0, 3))
            outputs[idx1] = target
            outputs[idx2] = target

        return Exercise2Data(
            truth_table_outputs=outputs,
            canon_type="Minitérminos (Suma de Productos)" if es_minterms else "Maxitérminos (Producto de Sumas)",
            gate_type="NAND" if es_minterms else "NOR"
        )

    def generate_ej3(self) -> Exercise3Data:
        sc = random.choice(self.scenarios)
        logic = random.choice(sc["logicas"])
        # Limpieza de nombres de variables para las tablas
        vars_clean = [v.split(':')[0].strip() for v in sc["vars"]]
        out_clean = sc["salida"].split(':')[0].strip()

        return Exercise3Data(
            title=sc["titulo"],
            variables=sc["vars"],
            output_name=sc["salida"],
            logic_description=logic,
            var_names_clean=vars_clean,
            out_name_clean=out_clean
        )

    def generate_ej4(self) -> Exercise4Data:
        tipo = random.choice(['MUX', 'COMPARADOR', 'SUMADOR'])
        params = {}

        if tipo == 'MUX':
            params['inputs'] = [random.randint(0, 1) for _ in range(16)]
            params['cases'] = []
            for _ in range(3):
                params['cases'].append({
                    'addr': random.randint(0, 15),
                    'ena': random.choice([0, 1])
                })
        elif tipo == 'COMPARADOR':
            params['A'] = random.randint(0, 15)
            params['B'] = random.randint(0, 15)
            params['cascada'] = [random.randint(0, 1) for _ in range(3)] # gr, eq, le
        elif tipo == 'SUMADOR':
            params['A'] = random.randint(0, 15)
            params['B'] = random.randint(0, 15)
            params['Cin'] = random.randint(0, 1)

        return Exercise4Data(block_type=tipo, params=params)

    def generate_ej5(self) -> Exercise5Data:
        ff = random.choice(['JK', 'D', 'T'])
        has_async = random.choice([True, False])
        total_cycles = 12 # Ciclos visuales completos
        width_units = total_cycles * 2 # Unidades de medio ciclo

        # Generar secuencias
        input_seq = "".join(["H" if random.randint(0, 1) else "L" for _ in range(width_units)])

        # Async Logic
        async_type = ""
        async_level = ""
        async_seq = ""

        if has_async:
            async_type = random.choice(['Preset', 'Clear', 'Set', 'Reset'])
            async_level = random.choice(['1', '0'])
            active_high = (async_level == '1')
            # 2 unidades activo, resto inactivo
            if active_high:
                async_seq = f"2H {width_units - 2}L"
            else:
                async_seq = f"2L {width_units - 2}H"

        return Exercise5Data(
            ff_type=ff,
            edge_type=random.choice(['Subida', 'Bajada']),
            logic_type='SHIFT' if ff == 'D' else 'COUNTER',
            has_async=has_async,
            async_type=async_type,
            async_level=async_level,
            total_cycles=total_cycles,
            clk_sequence=f"{total_cycles}{{C}}",
            async_sequence=async_seq,
            input_sequence=input_seq,
            output_placeholder=f"{width_units}{{U}}" # Unknown/Empty space
        )