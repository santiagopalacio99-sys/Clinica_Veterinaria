from dueno import Dueno
from ave import Ave

dueno3 = Dueno("1002345678", "Ana Torres", "3159876543")
ave1 = Ave("Lora", 5, 0.4, dueno3, True)

ave1.mostrar_informacion()
ave1.emitir_sonido()