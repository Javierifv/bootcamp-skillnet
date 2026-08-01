from usuario import Usuario

# Crear un usuario
usuario1 = Usuario("Javier Flores", "javier@gmail.com")
# Agregar tarjetas
usuario1.agregar_tarjeta("Visa", 1000, 0.02)
usuario1.agregar_tarjeta("Mastercard", 2000, 0.03)
usuario1.agregar_tarjeta("American Express", 5000, 0.05)
# ===========================
# Tarjeta Visa
# ===========================
usuario1.hacer_compra("Visa", 200)\
        .hacer_compra("Visa", 300)\
        .pagar_tarjeta("Visa", 100)\
        .cobrar_intereses("Visa")\
        .mostrar_saldo_usuario("Visa")

# ===========================
# Tarjeta Mastercard
# ===========================
usuario1.hacer_compra("Mastercard", 500)\
        .hacer_compra("Mastercard", 400)\
        .hacer_compra("Mastercard", 300)\
        .pagar_tarjeta("Mastercard", 200)\
        .pagar_tarjeta("Mastercard", 100)\
        .cobrar_intereses("Mastercard")\
        .mostrar_saldo_usuario("Mastercard")

# ===========================
# Tarjeta American Express
# ===========================
usuario1.hacer_compra("American Express", 1500)\
        .hacer_compra("American Express", 1800)\
        .hacer_compra("American Express", 1200)\
        .hacer_compra("American Express", 700)\
        .hacer_compra("American Express", 1000)\
        .mostrar_saldo_usuario("American Express")