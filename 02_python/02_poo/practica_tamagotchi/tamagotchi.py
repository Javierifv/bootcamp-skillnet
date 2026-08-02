class Tamagotchi:

    def __init__(self, nombre, color, salud=100, felicidad=100, energia=100):
        self.nombre = nombre
        self.color = color
        self.salud = salud
        self.felicidad = felicidad
        self.energia = energia

    def jugar(self):
        self.felicidad += 10
        self.salud -= 5
        return self

    def comer(self):
        self.felicidad += 5
        self.salud += 10
        return self

    def curar(self):
        self.felicidad -= 5
        self.salud += 20
        return self

    def mostrar_estado(self):
        print(f"Mascota: {self.nombre}")
        print(f"Salud: {self.salud}")
        print(f"Felicidad: {self.felicidad}")
        print(f"Energía: {self.energia}")
        return self
