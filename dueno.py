class Dueno:
    """Representa al dueño de un animal, con documento, nombre y teléfono."""

    def __init__(self, documento, nombre, telefono):
        """Crea el dueño. Cada dato pasa por su método set para validarlo."""
        self.set_documento(documento)
        self.set_nombre(nombre)
        self.set_telefono(telefono)

    def get_documento(self):
        """Devuelve el documento."""
        return self._documento

    def get_nombre(self):
        """Devuelve el nombre."""
        return self._nombre

    def get_telefono(self):
        """Devuelve el teléfono."""
        return self._telefono

    def set_documento(self, documento):
        """Cambia el documento. Lanza ValueError si está vacío."""
        if documento.strip() != "":
            self._documento = documento
        else:
            raise ValueError("El documento no puede estar vacío")

    def set_nombre(self, nombre):
        """Cambia el nombre. Lanza ValueError si está vacío."""
        if nombre.strip() != "":
            self._nombre = nombre
        else:
            raise ValueError("El nombre no puede estar vacío")

    def set_telefono(self, telefono):
        """Cambia el teléfono. Lanza ValueError si está vacío."""
        if telefono.strip() != "":
            self._telefono = telefono
        else:
            raise ValueError("El teléfono no puede estar vacío")

    def mostrar_informacion(self):
        """Muestra los datos del dueño."""
        print(f"documento: {self._documento}")
        print(f"nombre: {self._nombre}")
        print(f"telefono: {self._telefono}")