from animal import Animal


class Ave(Animal):
    """Ave atendida en la clínica. Hereda de Animal y agrega si puede volar."""

    def __init__(self, nombre, edad, peso, dueno, puede_volar):
        """Entrega los datos generales a Animal y guarda si puede volar."""
        super().__init__(nombre, edad, peso, dueno)
        self.set_puede_volar(puede_volar)

    def get_puede_volar(self):
        """Devuelve True si el ave puede volar."""
        return self._puede_volar

    def set_puede_volar(self, puede_volar):
        """Cambia si puede volar. Lanza ValueError si no es True o False."""
        if isinstance(puede_volar, bool):
            self._puede_volar = puede_volar
        else:
            raise ValueError("puede_volar debe ser True o False")

    def mostrar_informacion(self):
        """Muestra los datos generales del animal y si puede volar."""
        super().mostrar_informacion()
        if self._puede_volar:
            print("vuelo: puede volar")
        else:
            print("vuelo: no puede volar")

    def emitir_sonido(self):
        """Implementa el método abstracto: el ave canta."""
        print(f"{self.get_nombre()} dice: ¡Pío pío!")