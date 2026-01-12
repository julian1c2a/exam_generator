from modules.numeracion.generators import BinaryConversionGenerator
from modules.combinacional.generators import KarnaughGenerator, LogicProblemGenerator, MSIGenerator
from modules.secuencial.generators import SequentialGenerator

# Registro central de ejercicios
EXERCISE_CATALOG = {
    "num_conversion_8bits": BinaryConversionGenerator(),
    "karnaugh_4vars": KarnaughGenerator(),
    "logic_problem": LogicProblemGenerator(),
    "msi_analysis": MSIGenerator(),
    "sequential_analysis": SequentialGenerator()
}
