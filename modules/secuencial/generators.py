import random
from core.generator_base import ExerciseGenerator
from modules.secuencial.models import SequentialExerciseData

class SequentialGenerator(ExerciseGenerator):
    def topic(self) -> str:
        return "Sistemas Secuenciales"

    def generate(self, difficulty: int = 1) -> SequentialExerciseData:
        ff = random.choice(['JK', 'D', 'T'])
        has_async = random.choice([True, False])
        total_cycles = 12 # Ciclos visuales completos
        width_units = total_cycles * 2 # Unidades de medio ciclo (24)

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

        return SequentialExerciseData(
            title="Sistemas Secuenciales",
            description="Analice el cronograma adjunto para el sistema secuencial dado.",
            ff_type=ff,
            edge_type=random.choice(['Subida', 'Bajada']),
            logic_type='SHIFT' if ff == 'D' else 'COUNTER',
            has_async=has_async,
            async_type=async_type,
            async_level=async_level,
            total_cycles=total_cycles,
            clk_sequence=f"{width_units}{{C}}",
            async_sequence=async_seq,
            input_sequence=input_seq,
            output_placeholder=f"{width_units}{{}}"
        )
