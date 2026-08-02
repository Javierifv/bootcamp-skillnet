from tamagotchi import Tamagotchi
from persona import Persona

mi_mascota = Tamagotchi("Mametchi", "Azul")

persona1 = Persona("Elena", "Rojas", mi_mascota)

persona1.jugar_con_tamagotchi().darle_comida().curarlo().mostrar_estado()