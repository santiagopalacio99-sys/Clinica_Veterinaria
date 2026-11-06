from animal import Animal


class Gato(Animal):
    """Gato atendido en la clínica. Hereda de Animal y agrega si vive solo en interiores."""

    def __init__(self, nombre, edad, peso, dueno, es_de_interior):
        """Entrega los datos generales a Animal y guarda si es de interior."""
        super().__init__(nombre, edad, peso, dueno)
        self.set_es_de_interior(es_de_interior)

    def get_es_de_interior(self):
        """Devuelve True si el gato vive solo en interiores."""
        return self._es_de_interior

    def set_es_de_interior(self, es_de_interior):
        """Cambia si es de interior. Lanza ValueError si no es True o False."""
        if isinstance(es_de_interior, bool):
            self._es_de_interior = es_de_interior
        else:
            raise ValueError("es_de_interior debe ser True o False")

    def mostrar_informacion(self):
        """Muestra los datos generales del animal y si es de interior."""
        super().mostrar_informacion()
        if self._es_de_interior:
            print("vive en: solo interiores")
        else:
            print("vive en: interiores y exteriores")

    def emitir_sonido(self):
        """Implementa el método abstracto: el gato maúlla."""
        print(f"{self.get_nombre()} dice: ¡Miau!")
