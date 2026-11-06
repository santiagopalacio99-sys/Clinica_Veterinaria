class AnimalYaRegistradoError(Exception):
    """Se lanza cuando se intenta registrar un animal que ya está registrado en la clínica."""
    pass


class AnimalNoEncontradoError(Exception):
    """Se lanza cuando se busca un animal que no está registrado en la clínica."""
    pass


class VeterinarioOcupadoError(Exception):
    """Se lanza cuando el veterinario ya tiene una cita a esa misma fecha y hora."""
    pass