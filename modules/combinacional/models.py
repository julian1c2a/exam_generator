from dataclasses import dataclass
from typing import List, Dict, Any
from core.generator_base import ExerciseData

@dataclass
class KarnaughExerciseData(ExerciseData):
    truth_table_outputs: List[int] # 16 valores (0 o 1)
    canon_type: str # "Minitérminos" o "Maxitérminos"
    gate_type: str # "NAND" o "NOR"
    vars_name: List[str] # ["A", "B", "C", "D"]
    out_name: str # "F"

@dataclass
class LogicProblemExerciseData(ExerciseData):
    context_title: str
    variables_desc: List[str]
    output_desc: str
    logic_description: str
    vars_clean: List[str] # ["P", "T", "N", "M"]
    out_clean: str        # "E"

@dataclass
class MSIExerciseData(ExerciseData):
    block_type: str # "MUX", "COMPARADOR", "SUMADOR"
    params: Dict[str, Any]
