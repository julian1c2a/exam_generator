from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any

@dataclass
class ExerciseData:
    """Clase base para los datos de cualquier ejercicio."""
    title: str
    description: str
    # Los datos específicos se añadirán en las subclases

class ExerciseGenerator(ABC):
    @abstractmethod
    def generate(self, difficulty: int = 1) -> ExerciseData:
        """
        Genera una instancia aleatoria del ejercicio.
        :param difficulty: Nivel de dificultad (1-3).
        :return: Objeto con los datos del ejercicio.
        """
        pass

    @property
    @abstractmethod
    def topic(self) -> str:
        """Devuelve el nombre del tema (ej: 'Secuencial')."""
        pass
