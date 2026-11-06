from animal import Animal


class Perro(Animal):
    """Perro atendido en la clínica. Hereda de Animal y agrega la raza."""

    def __init__(self, nombre, edad, peso, dueno, raza):
        """Entrega los datos generales a Animal y guarda la raza."""
        super().__init__(nombre, edad, peso, dueno)
        self.set_raza(raza)

    def get_raza(self):
        """Devuelve la raza."""
        return self._raza

    def set_raza(self, raza):
        """Cambia la raza. Lanza ValueError si está vacía."""
        if raza.strip() != "":
            self._raza = raza
        else:
            raise ValueError("La raza no puede estar vacía")

    def mostrar_informacion(self):
        """Muestra los datos generales del animal y la raza."""
        super().mostrar_informacion()
        print(f"raza: {self._raza}")

    def emitir_sonido(self):
        """Implementa el método abstracto: el perro ladra."""
        print(f"{self.get_nombre()} dice: ¡Guau guau!")