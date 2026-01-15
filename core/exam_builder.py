import json
import os
import random
from typing import List, Dict, Any, Optional
from core.generator_base import ExerciseData, ExerciseGenerator, ExerciseRandomizer
from core.catalog import EXERCISE_CATALOG

class ExamBuilder:
    def __init__(self, config_file: str):
        self.config = self._load_config(config_file)
        self._configure_seed()
        self.exercises_data: List[ExerciseData] = []
        self.exercises_json: List[Dict[str, Any]] = []

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
        
        ARQUITECTURA ORTOGONAL:
        1. Si el config especifica 'problem_json', usa generador directo (sin aleatorización)
        2. Si especifica 'randomizer_params', usa aleatorizador + generador con seed
        3. Si no especifica nada, usa generador legacy (backward compatibility)
        
        IMPORTANTE: Genera dos salidas paralelas:
        1. self.exercises_data: List[ExerciseData] objetos Python (para renderers Python)
        2. self.exercises_json: List[Dict] JSON agnóstico (para cualquier renderer agnóstico)
        """
        self.exercises_data = []
        self.exercises_json = []
        requested_exercises = self.config.get("exercises", [])

        print(f"🏗️  Construyendo examen: {self.config.get('title', 'Sin título')}")

        for req in requested_exercises:
            ex_id = req.get("id")
            qty = req.get("qty", 1)
            difficulty = req.get("difficulty", 1)

            if ex_id not in EXERCISE_CATALOG:
                print(f"⚠️  Advertencia: El ejercicio '{ex_id}' no existe en el catálogo. Saltando.")
                continue

            # Buscar generador en el catálogo
            generator = EXERCISE_CATALOG[ex_id]
            print(f"   🔹 Generando {qty}x '{ex_id}' ({generator.topic})...")

            for i in range(qty):
                # RUTA 1: JSON Manual (sin aleatorización) - DEBUG/TESTING
                if 'problem_json' in req:
                    problem_dict = req['problem_json']
                    print(f"      📄 Usando JSON manual (sin aleatorización)")
                    
                    if hasattr(generator, 'generate_from_problem'):
                        # Usar generador directo
                        data = generator.generate_from_problem(problem_dict)
                    else:
                        # Fallback: usar generate legacy
                        data = generator.generate(difficulty=difficulty)
                
                # RUTA 2: Con Aleatorizador + Seed Controlable - PRODUCCIÓN
                elif 'randomizer_params' in req:
                    randomizer_params = req['randomizer_params']
                    randomizer_seed = randomizer_params.get('seed')
                    
                    if randomizer_seed is not None:
                        print(f"      🎲 Generando con seed={randomizer_seed} (reproducible)")
                    else:
                        print(f"      🎲 Generando sin seed (aleatorio)")
                    
                    # Buscar aleatorizador (por convención: mismo nombre + 'Randomizer')
                    randomizer_class_name = generator.__class__.__name__.replace('Generator', 'Randomizer')
                    
                    # Crear aleatorizador (aquí simplificado, mejorar después)
                    # TODO: Implementar registro de aleatorizadores similar a generadores
                    if hasattr(generator, '__class__'):
                        # Obtener módulo del generador
                        module = __import__(generator.__class__.__module__, fromlist=[randomizer_class_name])
                        if hasattr(module, randomizer_class_name):
                            randomizer_class = getattr(module, randomizer_class_name)
                            randomizer = randomizer_class(**randomizer_params.get('args', {}))
                            
                            # Generar problema aleatorio
                            problem = randomizer.randomize(seed=randomizer_seed)
                            
                            # Pasar al generador
                            if hasattr(generator, 'generate_from_problem'):
                                data = generator.generate_from_problem(problem)
                            else:
                                data = generator.generate(difficulty=difficulty)
                        else:
                            # Fallback
                            data = generator.generate(difficulty=difficulty)
                    else:
                        data = generator.generate(difficulty=difficulty)
                
                # RUTA 3: Generación Legacy (backward compatibility)
                else:
                    data = generator.generate(difficulty=difficulty)
                
                self.exercises_data.append(data)
                
                # Serializar a JSON agnóstico
                if hasattr(data, 'asdict'):
                    self.exercises_json.append(data.asdict())
                else:
                    # Fallback para ejercicios sin asdict()
                    self.exercises_json.append({
                        "title": getattr(data, 'title', ''),
                        "description": getattr(data, 'description', ''),
                        "data": str(data)
                    })

        return self.exercises_data
    
    def get_exercises_json(self) -> List[Dict[str, Any]]:
        """Devuelve los ejercicios en formato JSON agnóstico (salida intermedia)."""
        return self.exercises_json
    
    def save_intermediate_json(self, output_file: str = None) -> str:
        """
        Guarda el JSON intermedio agnóstico en un archivo.
        
        Este es el PRODUCTO PRINCIPAL de la generación.
        Los renderers consumen este JSON, no los objetos Python.
        
        Args:
            output_file: Ruta del archivo. Si es None, usa {config_title}_ejercicios.json
        
        Returns:
            Ruta del archivo guardado
        """
        if not self.exercises_json:
            raise RuntimeError("No hay ejercicios generados. Llama a build() primero.")
        
        if output_file is None:
            config_title = self.config.get("title", "exam").replace(" ", "_").lower()
            output_file = os.path.join("build", "json", f"{config_title}_ejercicios.json")
        
        # Crear directorio si no existe
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        # Preparar salida con metadata
        output = {
            "exam_metadata": {
                "title": self.config.get("title", "Sin título"),
                "description": self.config.get("description", ""),
                "seed": self.config.get("seed"),
                "total_exercises": len(self.exercises_json)
            },
            "exercises": self.exercises_json
        }
        
        # Guardar con formato legible
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(output, f, ensure_ascii=False, indent=2)
        
        print(f"💾 JSON intermedio guardado: {os.path.abspath(output_file)}")
        return output_file
