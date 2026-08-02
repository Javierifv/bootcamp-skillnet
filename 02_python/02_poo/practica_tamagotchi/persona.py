from tamagotchi import Tamagotchi

class Persona:

    def __init__(self, nombre, apellido, tamagotchi):
        self.nombre = nombre
        self.apellido = apellido
        self.tamagotchi = tamagotchi

    def jugar_con_tamagotchi(self):
        self.tamagotchi.jugar()
        return self

    def darle_comida(self):
        self.tamagotchi.comer()
        return self

    def curarlo(self):
        self.tamagotchi.curar()
        return self

    def mostrar_estado(self):
        print(f"Persona: {self.nombre}")
        self.tamagotchi.mostrar_estado()
        return self