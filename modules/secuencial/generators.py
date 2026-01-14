import random
from core.generator_base import ExerciseGenerator
from modules.secuencial.models import SequentialExerciseData

class SequentialGenerator(ExerciseGenerator):
    def topic(self) -> str:
        return "Sistemas Secuenciales"

    def generate(self, difficulty: int = 1) -> SequentialExerciseData:
        # 1. Configuración del Circuito
        ff_type = random.choice(['JK', 'T']) # Simplificado a JK y T como en el renderer
        edge_type = random.choice(['Subida', 'Bajada'])
        logic_type = random.choice(['COUNTER', 'SHIFT'])
        
        has_async = random.choice([True, False])
        async_type = 'Set' if random.random() < 0.5 else 'Reset'
        
        # 2. Generación de Secuencias
        num_cycles = 12
        width_units = num_cycles * 2 # 24 unidades de tiempo
        
        # Generación de Entrada E (Estable por ciclo)
        # Para evitar condiciones de carrera, la entrada cambia solo entre ciclos completos.
        # Esto asegura setup/hold time suficiente para flancos de subida o bajada.
        input_seq_chars = []
        for _ in range(num_cycles):
            val = random.choice(['L', 'H'])
            input_seq_chars.append(val) # Primera mitad del ciclo
            input_seq_chars.append(val) # Segunda mitad del ciclo
            
        input_sequence = "".join(input_seq_chars)
        
        # Generación de Asíncrona (Set/Reset)
        async_sequence = ""
        if has_async:
            # Activo a nivel bajo (0) según enunciado del renderer
            # Generamos un pulso activo (L) en algún momento
            pulse_start = random.randint(2, 6) # Empezar un poco después del inicio
            pulse_len = 2 # Duración del pulso (1 ciclo completo)
            
            pre_h = pulse_start
            post_h = width_units - pre_h - pulse_len
            
            # Formato RLE para tikz-timing: "4H 2L 18H"
            async_sequence = f"{pre_h}H {pulse_len}L {post_h}H"

        return SequentialExerciseData(
            title="Sistemas Secuenciales",
            description=f"Síncrono ({logic_type}) por {edge_type}. FF {ff_type}. Async \\textbf{{{async_type}(asyn)}} a nivel 0.",
            ff_type=ff_type,
            edge_type=edge_type,
            logic_type=logic_type,
            has_async=has_async,
            async_level="0",
            async_type=async_type,
            clk_sequence=f"{width_units}{{C}}", # 24{C}
            input_sequence=input_sequence,
            async_sequence=async_sequence,
            output_placeholder=f"{width_units}{{}}" # Espacio vacío
        )
