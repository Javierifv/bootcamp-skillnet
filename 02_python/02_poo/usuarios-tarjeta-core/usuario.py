from tarjeta_credito import TarjetaCredito

class Usuario:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
        # El usuario puede tener varias tarjetas
        self.tarjetas = {}
    # Agregar una tarjeta
    def agregar_tarjeta(self, nombre_tarjeta, limite_credito, intereses):
        self.tarjetas[nombre_tarjeta] = TarjetaCredito(limite_credito, intereses)
        return self
    # Comprar con una tarjeta
    def hacer_compra(self, nombre_tarjeta, monto):
        self.tarjetas[nombre_tarjeta].compra(monto)
        return self
    # Pagar una tarjeta
    def pagar_tarjeta(self, nombre_tarjeta, monto):
        self.tarjetas[nombre_tarjeta].pago(monto)
        return self
    
    # Cobrar intereses
    def cobrar_intereses(self, nombre_tarjeta):
        self.tarjetas[nombre_tarjeta].cobrar_interes()
        return self
    # Mostrar saldo
    def mostrar_saldo_usuario(self, nombre_tarjeta):
        print("--------------------------")
        print("Usuario:", self.nombre)
        print("Tarjeta:", nombre_tarjeta)
        print("Saldo:", round(self.tarjetas[nombre_tarjeta].saldo_pagar, 2))
        print("--------------------------")
        return self