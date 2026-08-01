class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = 30000
        self.saldo_pagar = 0

    def hacer_compra(self, monto):
        self.saldo_pagar += monto

    def pagar_tarjeta(self, monto):
        self.saldo_pagar -= monto

    def mostrar_saldo_usuario(self):
        print(f"Usuario: {self.nombre} {self.apellido}, Saldo a Pagar: ${self.saldo_pagar}")

    def transferir_deuda (self, otro_usuario, monto):
        self.saldo_pagar -= monto
        otro_usuario.saldo_pagar += monto

usuario1 = Usuario("Nariyoshi", "Miyagi", "miyagi@dojo.com")
usuario2 = Usuario("Daniel", "LaRusso", "daniel@dojo.com")
usuario3 = Usuario("Johnny", "Lawrence", "johnny@cobra.com")

usuario1.hacer_compra(100)
usuario1.hacer_compra(100)
usuario1.pagar_tarjeta(100)
usuario1.mostrar_saldo_usuario()

usuario2.hacer_compra(250)
usuario2.pagar_tarjeta(50)
usuario2.pagar_tarjeta(50)
usuario2.mostrar_saldo_usuario()

usuario3.hacer_compra(300)
usuario3.hacer_compra(300)
usuario3.hacer_compra(300)
usuario3.pagar_tarjeta(150)
usuario3.pagar_tarjeta(150)
usuario3.pagar_tarjeta(150)
usuario3.pagar_tarjeta(150)
usuario3.mostrar_saldo_usuario()

usuario1.transferir_deuda(usuario2, 100)
usuario1.mostrar_saldo_usuario()
usuario2.mostrar_saldo_usuario()