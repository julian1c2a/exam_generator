import json
import os
import random
from typing import List, Dict, Any
from core.generator_base import ExerciseData
from core.catalog import EXERCISE_CATALOG

class ExamBuilder:
    def __init__(self, config_file: str):
        self.config = self._load_config(config_file)
        self._configure_seed()

    def _load_config(self, filename: str) -> Dict[str, Any]:
        if not os.path.exists(filename):
            raise FileNotFoundError(f"El archivo de configuración '{filename}' no existe.")
        
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _configure_seed(self):
        """Configura la semilla aleatoria si está presente en la configuración."""
        seed = self.config.get("seed")
        if seed is not None:
            print(f"🎲 Semilla fija detectada: {seed}. La generación será determinista.")
            random.seed(seed)
        else:
            print("🎲 Semilla aleatoria (random).")

    def build(self) -> List[ExerciseData]:
        """
        Construye el examen generando los datos para cada ejercicio definido en la configuración.
        """
        exercises_data = []
        requested_exercises = self.config.get("exercises", [])

        print(f"🏗️  Construyendo examen: {self.config.get('title', 'Sin título')}")

        for req in requested_exercises:
            ex_id = req.get("id")
            qty = req.get("qty", 1)
            difficulty = req.get("difficulty", 1)

            if ex_id not in EXERCISE_CATALOG:
                print(f"⚠️  Advertencia: El ejercicio '{ex_id}' no existe en el catálogo. Saltando.")
                continue

            generator = EXERCISE_CATALOG[ex_id]
            print(f"   🔹 Generando {qty}x '{ex_id}' ({generator.topic})...")

            for _ in range(qty):
                # Generar el ejercicio
                data = generator.generate(difficulty=difficulty)
                exercises_data.append(data)

        return exercises_data
