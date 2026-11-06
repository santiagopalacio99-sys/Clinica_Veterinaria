from animal import Animal


class Veterinario:
    """Profesional que atiende a los animales de la clínica.
    Guarda nombre, especialidad y número de licencia."""

    def __init__(self, nombre, especialidad, licencia):
        """Crea el veterinario. Cada dato pasa por su método set para validarlo."""
        self.set_nombre(nombre)
        self.set_especialidad(especialidad)
        self.set_licencia(licencia)

    def get_nombre(self):
        """Devuelve el nombre."""
        return self._nombre

    def get_especialidad(self):
        """Devuelve la especialidad."""
        return self._especialidad

    def get_licencia(self):
        """Devuelve el número de licencia."""
        return self._licencia

    def set_nombre(self, nombre):
        """Cambia el nombre. Lanza ValueError si está vacío."""
        if nombre.strip() != "":
            self._nombre = nombre
        else:
            raise ValueError("El nombre del veterinario no puede estar vacío")

    def set_especialidad(self, especialidad):
        """Cambia la especialidad. Lanza ValueError si está vacía."""
        if especialidad.strip() != "":
            self._especialidad = especialidad
        else:
            raise ValueError("La especialidad no puede estar vacía")

    def set_licencia(self, licencia):
        """Cambia la licencia. Lanza ValueError si está vacía."""
        if licencia.strip() != "":
            self._licencia = licencia
        else:
            raise ValueError("La licencia no puede estar vacía")

    def atender(self, animal, motivo):
        """Atiende a un animal y agrega el registro a su historial clínico.
        Lanza ValueError si no recibe un objeto Animal o si el motivo está vacío."""
        if not isinstance(animal, Animal):
            raise ValueError("Solo se puede atender a un Animal válido")
        animal.get_historial().agregar_registro(f"{motivo} (atendido por {self._nombre})")

    def mostrar_informacion(self):
        """Muestra los datos del veterinario."""
        print(f"veterinario: {self._nombre}")
        print(f"especialidad: {self._especialidad}")
        print(f"licencia: {self._licencia}")