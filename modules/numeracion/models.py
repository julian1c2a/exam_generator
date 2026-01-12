from dataclasses import dataclass
from typing import List, Optional
from core.generator_base import ExerciseData

@dataclass
class ConversionRow:
    label: str
    val_decimal: int
    target_col_idx: int
    target_val_str: str
    # Soluciones pre-calculadas para todas las columnas
    sol_bin: str
    sol_c2: str
    sol_sm: str
    sol_bcd: str

@dataclass
class ArithmeticOp:
    op_type: str
    system: str
    operand1: str
    operand2: str
    operator_symbol: str
    # Soluciones
    val1_dec: int
    val2_dec: int
    result_dec: int
    result_bin: str # String binario del resultado (N bits)
    overflow: bool
    underflow: bool
    carry_bits: str # String con los bits de acarreo

@dataclass
class ConversionExerciseData(ExerciseData):
    n_bits: int
    rows: List[ConversionRow]
    operations: List[ArithmeticOp]
