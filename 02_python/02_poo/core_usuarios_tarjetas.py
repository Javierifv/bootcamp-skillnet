class TarjetaCredito:

    todas_las_tarjetas = []

    def __init__(self, limite_credito, intereses, saldo_pagar=0):
        self.limite_credito = limite_credito
        self.intereses = intereses
        self.saldo_pagar = saldo_pagar
        TarjetaCredito.todas_las_tarjetas.append(self)

    @staticmethod
    def puede_comprar(saldo_pagar, limite_credito, monto):
        return saldo_pagar + monto <= limite_credito

    def compra(self, monto):
        if TarjetaCredito.puede_comprar(self.saldo_pagar, self.limite_credito, monto):
            self.saldo_pagar += monto
        else:
            print("Tarjeta Rechazada, has alcanzado tu límite de crédito")
        return self

    def pago(self, monto):
        self.saldo_pagar -= monto
        return self

    def mostrar_info_tarjeta(self):
        print(f"Saldo a Pagar: ${self.saldo_pagar}")

    def cobrar_interes(self):
        self.saldo_pagar += (self.saldo_pagar*self.intereses)
        return self

    @classmethod
    def mostar_tarjetas(cls):
        for tarjeta in cls.todas_las_tarjetas:
            print(f"\nTarjeta {cls.todas_las_tarjetas.index(tarjeta)+1}:")
            print(f"Saldo a Pagar: {tarjeta.saldo_pagar}")
            print(f"Límite de Crédito: {tarjeta.limite_credito}")
            print(f"Porcentaje de Interés: {tarjeta.intereses*100}%")

class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.tarjetas = {
        "visa": TarjetaCredito(limite_credito=1000, intereses=0.02),
        "mastercard": TarjetaCredito(limite_credito=2000, intereses=0.03)
        }


    def hacer_compra(self, monto, nombre_tarjeta):
        self.tarjetas[nombre_tarjeta].compra(monto)
        return self

    def pagar_tarjeta(self, monto, nombre_tarjeta):
        self.tarjetas[nombre_tarjeta].pago(monto)
        return self

    def mostrar_saldo_usuario(self, nombre_tarjeta):
        print(f"Usuario: {self.nombre} {self.apellido}")
        self.tarjetas[nombre_tarjeta].mostrar_info_tarjeta()

usuario1 = Usuario("Nariyoshi", "Miyagi", "miyagi@dojo.com")

usuario1.hacer_compra(100, "visa")
usuario1.hacer_compra(100, "mastercard")
usuario1.pagar_tarjeta(100, "visa")
usuario1.mostrar_saldo_usuario("visa")
usuario1.mostrar_saldo_usuario("mastercard")