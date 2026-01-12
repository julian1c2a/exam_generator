from dataclasses import dataclass
from typing import List, Optional

@dataclass
class ConversionRow:
    label: str
    val_decimal: int
    target_col_idx: int # Qué columna debe rellenar el generador (el resto vacías)
    target_val_str: str

@dataclass
class ArithmeticOp:
    op_type: str # "Suma" o "Resta"
    system: str  # "Binario Natural" o "Complemento a 2"
    operand1: str
    operand2: str
    operator_symbol: str

@dataclass
class Exercise1Data:
    rows: List[ConversionRow]
    operations: List[ArithmeticOp]
    n_bits: int

@dataclass
class Exercise2Data:
    truth_table_outputs: List[int] # 16 valores
    canon_type: str # "Minitérminos" o "Maxitérminos"
    gate_type: str # "NAND" o "NOR"

@dataclass
class Exercise3Data:
    title: str
    variables: List[str]
    output_name: str
    logic_description: str
    var_names_clean: List[str] # ["A", "B", "C", "D"]
    out_name_clean: str        # "Z"

@dataclass
class Exercise4Data:
    block_type: str # "MUX", "COMPARADOR", "SUMADOR"
    # Datos específicos según tipo (diccionario flexible)
    params: dict

@dataclass
class Exercise5Data:
    ff_type: str
    edge_type: str # "Subida" o "Bajada"
    logic_type: str # "SHIFT" o "COUNTER"
    has_async: bool
    async_type: str # "Preset", "Clear"
    async_level: str # "0" o "1"

    # Datos del cronograma
    total_cycles: int
    clk_sequence: str
    async_sequence: str
    input_sequence: str
    output_placeholder: str