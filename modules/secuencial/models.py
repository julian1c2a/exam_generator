from dataclasses import dataclass
from core.generator_base import ExerciseData

@dataclass
class SequentialExerciseData(ExerciseData):
    ff_type: str # "JK", "D", "T"
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
