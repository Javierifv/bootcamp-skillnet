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

tarjeta1 = TarjetaCredito(limite_credito=1000, intereses=0.02)
tarjeta2 = TarjetaCredito(limite_credito=2000, intereses=0.03)
tarjeta3 = TarjetaCredito(limite_credito=500, intereses=0.01)

tarjeta1.compra(200).compra(300).pago(100).cobrar_interes().mostrar_info_tarjeta()

tarjeta2.compra(100).compra(100).compra(100).pago(50).pago(50).cobrar_interes().mostrar_info_tarjeta()

tarjeta3.compra(100).compra(100).compra(100).compra(100).compra(150).mostrar_info_tarjeta()

TarjetaCredito.mostar_tarjetas()