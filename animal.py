from abc import ABC, abstractmethod
from dueno import Dueno
from historial_clinico import HistorialClinico


class Animal(ABC):
    """Clase abstracta que representa a un animal atendido en la clínica.
    Guarda nombre, edad, peso, su dueño y su historial clínico.
    No se puede instanciar: debe ser un Perro, un Gato o un Ave."""

    def __init__(self, nombre, edad, peso, dueno):
        """Crea el animal. Su HistorialClinico se crea aquí adentro (composición)."""
        self.set_nombre(nombre)
        self.set_edad(edad)
        self.set_peso(peso)
        self.set_dueno(dueno)
        self._historial = HistorialClinico()

    def get_nombre(self):
        """Devuelve el nombre."""
        return self._nombre

    def get_edad(self):
        """Devuelve la edad en años."""
        return self._edad

    def get_peso(self):
        """Devuelve el peso en kilogramos."""
        return self._peso

    def get_dueno(self):
        """Devuelve el objeto Dueno del animal."""
        return self._dueno

    def get_historial(self):
        """Devuelve el objeto HistorialClinico del animal."""
        return self._historial

    def set_nombre(self, nombre):
        """Cambia el nombre. Lanza ValueError si está vacío."""
        if nombre.strip() != "":
            self._nombre = nombre
        else:
            raise ValueError("El nombre del animal no puede estar vacío")

    def set_edad(self, edad):
        """Cambia la edad. Lanza ValueError si es negativa."""
        if edad >= 0:
            self._edad = edad
        else:
            raise ValueError("La edad no puede ser negativa")

    def set_peso(self, peso):
        """Cambia el peso. Lanza ValueError si no es mayor que cero."""
        if peso > 0:
            self._peso = peso
        else:
            raise ValueError("El peso debe ser mayor que cero")

    def set_dueno(self, dueno):
        """Cambia el dueño. Lanza ValueError si no es un objeto Dueno."""
        if isinstance(dueno, Dueno):
            self._dueno = dueno
        else:
            raise ValueError("El dueño debe ser un Dueno válido")

    def mostrar_informacion(self):
        """Muestra los datos generales del animal y el nombre de su dueño."""
        print(f"nombre: {self._nombre}")
        print(f"edad: {self._edad} años")
        print(f"peso: {self._peso} kg")
        print(f"dueño: {self._dueno.get_nombre()}")

    @abstractmethod
    def emitir_sonido(self):
        """Método abstracto: cada tipo de animal define su propio sonido."""
        pass
