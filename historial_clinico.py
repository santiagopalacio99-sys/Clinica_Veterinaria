class HistorialClinico:
    """Guarda los registros médicos de un animal. Forma parte esencial del animal:
    nace cuando el animal llega a la clínica y no existe sin él."""

    def __init__(self):
        """Crea el historial con la lista de registros vacía."""
        self._registros = []

    def get_registros(self):
        """Devuelve la lista de registros."""
        return self._registros

    def agregar_registro(self, descripcion):
        """Agrega un registro. Lanza ValueError si la descripción está vacía."""
        if descripcion.strip() != "":
            self._registros.append(descripcion)
        else:
            raise ValueError("El registro no puede estar vacío")

    def mostrar_historial(self):
        """Muestra los registros, uno por línea."""
        if len(self._registros) == 0:
            print("El historial está vacío")
        else:
            for numero, registro in enumerate(self._registros, 1):
                print(f"{numero}. {registro}")