def multiplica_por_dos(num):
    # Sumamos 1 para incluir el número 'num' en la secuencia
    lista = [i * 2 for i in range(num + 1)]
    return lista

print(multiplica_por_dos(5))