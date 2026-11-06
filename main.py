"""Programa principal de la clínica veterinaria.
Crea dueños, animales, veterinarios y citas, y demuestra la clase abstracta,
la herencia, la sobreescritura, el polimorfismo, la composición y las
excepciones personalizadas."""

from animal import Animal
from dueno import Dueno
from perro import Perro
from gato import Gato
from ave import Ave
from veterinario import Veterinario
from cita import Cita
from clinica import Clinica
from excepciones import (
    AnimalYaRegistradoError,
    AnimalNoEncontradoError,
    VeterinarioOcupadoError,
)

# ===================== CREACIÓN DE OBJETOS =====================

clinica = Clinica("Clínica Huellitas")

dueno1 = Dueno("1053123456", "Laura Gómez", "3101234567")
dueno2 = Dueno("1088765432", "Carlos Ruiz", "3207654321")
dueno3 = Dueno("1002345678", "Ana Torres", "3159876543")

perro1 = Perro("Rocky", 3, 12.5, dueno1, "Labrador")
perro2 = Perro("Max", 5, 20.0, dueno2, "Pastor alemán")
gato1 = Gato("Michi", 2, 4.2, dueno2, True)
gato2 = Gato("Luna", 4, 3.8, dueno3, False)
ave1 = Ave("Lora", 5, 0.4, dueno3, True)

vet1 = Veterinario("Dra. Marta Ríos", "Medicina general", "MV-1234")
vet2 = Veterinario("Dr. Pablo Herrera", "Cirugía", "MV-5678")

# ===================== CASOS NORMALES =====================

print("--- Registro de animales ---")
for animal in (perro1, perro2, gato1, gato2, ave1):
    clinica.registrar_animal(animal)
clinica.mostrar_animales()

print("\n--- Polimorfismo: una sola colección y un solo ciclo ---")
for animal in clinica.get_animales():
    animal.mostrar_informacion()
    animal.emitir_sonido()
    print()

print("--- Composición: el historial clínico de cada animal ---")
vet1.atender(perro1, "Vacuna antirrábica aplicada")
vet1.atender(perro1, "Control de peso: 12.5 kg")
vet2.atender(gato1, "Esterilización realizada")
print("Historial de Rocky:")
perro1.get_historial().mostrar_historial()
print("Historial de Michi:")
gato1.get_historial().mostrar_historial()

print("\n--- Citas agendadas correctamente ---")
cita1 = Cita("2026-11-10", "10:00", "Control anual", vet1, perro1)
cita2 = Cita("2026-11-10", "10:00", "Vacunación", vet2, gato1)
clinica.agendar_cita(cita1)
clinica.agendar_cita(cita2)
cita1.mostrar_informacion()
cita2.mostrar_informacion()

print("\n--- Búsqueda de un animal que sí existe ---")
encontrado = clinica.buscar_animal("Michi")
print(f"Encontrado: {encontrado.get_nombre()}")

# ===================== CASOS EXCEPCIONALES =====================

print("\n--- Prueba 1: crear un Animal directamente ---")
try:
    animal_general = Animal("Toby", 2, 5.0, dueno1)
except TypeError:
    print("Error: no se puede crear un Animal directamente, debe ser Perro, Gato o Ave")

print("\n--- Prueba 2: valor inválido ---")
try:
    perro1.set_edad(-1)
except ValueError as error:
    print("Error:", error)
print("Edad actual de Rocky:", perro1.get_edad())

print("\n--- Excepción 1: animal ya registrado ---")
try:
    clinica.registrar_animal(perro1)
except AnimalYaRegistradoError as error:
    print("Error:", error)

print("\n--- Excepción 2: animal no encontrado ---")
try:
    clinica.buscar_animal("Firulais")
except AnimalNoEncontradoError as error:
    print("Error:", error)

print("\n--- Excepción 3: veterinario ocupado ---")
cita3 = Cita("2026-11-10", "10:00", "Revisión dental", vet1, perro2)
try:
    clinica.agendar_cita(cita3)
except VeterinarioOcupadoError as error:
    print("Error:", error)

print("\nEl programa continuó su ejecución después de controlar todas las excepciones.")