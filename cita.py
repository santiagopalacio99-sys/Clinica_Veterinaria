from animal import Animal
from veterinario import Veterinario


class Cita:
    """Representa una cita entre un veterinario y un animal.
    Guarda objetos Veterinario y Animal, además de la fecha, la hora y el motivo."""

    def __init__(self, fecha, hora, motivo, veterinario, animal):
        """Crea la cita. Cada dato pasa por su método set para validarlo."""
        self.set_fecha(fecha)
        self.set_hora(hora)
        self.set_motivo(motivo)
        self.set_veterinario(veterinario)
        self.set_animal(animal)

    def get_fecha(self):
        """Devuelve la fecha."""
        return self._fecha

    def get_hora(self):
        """Devuelve la hora."""
        return self._hora

    def get_motivo(self):
        """Devuelve el motivo."""
        return self._motivo

    def get_veterinario(self):
        """Devuelve el objeto Veterinario de la cita."""
        return self._veterinario

    def get_animal(self):
        """Devuelve el objeto Animal de la cita."""
        return self._animal

    def set_fecha(self, fecha):
        """Cambia la fecha. Lanza ValueError si está vacía."""
        if fecha.strip() != "":
            self._fecha = fecha
        else:
            raise ValueError("La fecha no puede estar vacía")

    def set_hora(self, hora):
        """Cambia la hora. Lanza ValueError si está vacía."""
        if hora.strip() != "":
            self._hora = hora
        else:
            raise ValueError("La hora no puede estar vacía")

    def set_motivo(self, motivo):
        """Cambia el motivo. Lanza ValueError si está vacío."""
        if motivo.strip() != "":
            self._motivo = motivo
        else:
            raise ValueError("El motivo no puede estar vacío")

    def set_veterinario(self, veterinario):
        """Cambia el veterinario. Lanza ValueError si no es un objeto Veterinario."""
        if isinstance(veterinario, Veterinario):
            self._veterinario = veterinario
        else:
            raise ValueError("El veterinario debe ser un Veterinario válido")

    def set_animal(self, animal):
        """Cambia el animal. Lanza ValueError si no es un objeto Animal."""
        if isinstance(animal, Animal):
            self._animal = animal
        else:
            raise ValueError("El animal debe ser un Animal válido")

    def mostrar_informacion(self):
        """Muestra los datos de la cita, con el nombre del veterinario y del animal."""
        print(f"fecha: {self._fecha} a las {self._hora}")
        print(f"motivo: {self._motivo}")
        print(f"veterinario: {self._veterinario.get_nombre()}")
        print(f"animal: {self._animal.get_nombre()}")