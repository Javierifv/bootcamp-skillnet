class TarjetaCredito:
    def __init__(self, limite_credito, intereses, saldo_pagar=0):
        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.intereses = intereses
    def compra(self, monto):
        if self.saldo_pagar + monto <= self.limite_credito:
            self.saldo_pagar += monto
        else:
            print("Tarjeta Rechazada, has alcanzado tu límite de crédito")
        return self
    def pago(self, monto):
        self.saldo_pagar -= monto
        return self
    def cobrar_interes(self):
        self.saldo_pagar += self.saldo_pagar * self.intereses
        return self
    def mostrar_info_tarjeta(self):
        print("Saldo a pagar: $", round(self.saldo_pagar, 2))
        return self