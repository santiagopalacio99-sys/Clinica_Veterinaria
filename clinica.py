from animal import Animal
from cita import Cita
from excepciones import (
    AnimalYaRegistradoError,
    AnimalNoEncontradoError,
    VeterinarioOcupadoError,
)


class Clinica:
    """Representa la clínica veterinaria. Guarda los animales registrados y las
    citas agendadas, y controla los problemas con excepciones personalizadas."""

    def __init__(self, nombre):
        """Crea la clínica con las listas de animales y citas vacías."""
        self.set_nombre(nombre)
        self._animales = []
        self._citas = []

    def get_nombre(self):
        """Devuelve el nombre de la clínica."""
        return self._nombre

    def get_animales(self):
        """Devuelve la lista de animales registrados."""
        return self._animales

    def get_citas(self):
        """Devuelve la lista de citas agendadas."""
        return self._citas

    def set_nombre(self, nombre):
        """Cambia el nombre. Lanza ValueError si está vacío."""
        if nombre.strip() != "":
            self._nombre = nombre
        else:
            raise ValueError("El nombre de la clínica no puede estar vacío")

    def registrar_animal(self, animal):
        """Registra un animal. Lanza AnimalYaRegistradoError si ya está registrado."""
        if not isinstance(animal, Animal):
            raise ValueError("Solo se puede registrar un Animal válido")
        if animal in self._animales:
            raise AnimalYaRegistradoError(f"{animal.get_nombre()} ya está registrado en la clínica")
        self._animales.append(animal)

    def buscar_animal(self, nombre):
        """Devuelve el animal con ese nombre. Lanza AnimalNoEncontradoError si no existe."""
        for animal in self._animales:
            if animal.get_nombre() == nombre:
                return animal
        raise AnimalNoEncontradoError(f"No hay ningún animal registrado con el nombre {nombre}")

    def agendar_cita(self, cita):
        """Agenda una cita. Lanza VeterinarioOcupadoError si el veterinario ya tiene
        otra cita a la misma fecha y hora."""
        if not isinstance(cita, Cita):
            raise ValueError("Solo se puede agendar una Cita válida")
        for otra in self._citas:
            mismo_veterinario = otra.get_veterinario() == cita.get_veterinario()
            misma_fecha = otra.get_fecha() == cita.get_fecha()
            misma_hora = otra.get_hora() == cita.get_hora()
            if mismo_veterinario and misma_fecha and misma_hora:
                raise VeterinarioOcupadoError(
                    f"{cita.get_veterinario().get_nombre()} ya tiene una cita el "
                    f"{cita.get_fecha()} a las {cita.get_hora()}"
                )
        self._citas.append(cita)

    def mostrar_animales(self):
        """Muestra el nombre y la especie de los animales registrados."""
        if len(self._animales) == 0:
            print("No hay animales registrados")
        else:
            for animal in self._animales:
                print(f"- {animal.get_nombre()} ({type(animal).__name__})")