# Multiplica por 2: crea una función que reciba un número y devuelva una lista que contenga los números enteros multiplicados por dos, desde el 0 hasta el número proporcionado como entrada.
# Ejemplo: multiplica_por_2(5) debe regresar [0, 2, 4, 6, 7, 10]

def multiplica_por_dos(num):
    lista = [i*2 for i in range (num+1)]
    return lista

print(multiplica_por_dos(5))

# Suma y resta: crea una función que reciba una lista con dos números. Imprime la suma de los dos números y regresa la resta de los dos números.
# Ejemplo: suma_y_resta([5, 4]) debe de imprimir 9 y regresar 1

def suma_y_resta(lista):
    print(sum(lista))
    return lista[0] - lista[1]

print(suma_y_resta([5,4]))

# Sumatoria menos longitud: crea una función que reciba una lista de números y regresa la sumatoria de estos menos la longitud de la lista.
# Ejemplo: sumatoria_menos_longitud([1, 2, 3, 4]) debe devolver 6 (sumatoria de números: 10 – longitud: 4)

def sumatoria_menos_longitud(lista):
    return sum(lista) - len(lista)

print(sumatoria_menos_longitud([1, 2, 3, 4]))

# Valores multiplicados por el segundo: escribe una función que reciba una lista y crea una nueva lista con todos los valores multiplicados por el segundo número. Imprime la longitud de la lista y regresa la nueva lista. Si la lista tiene menos de 2 elementos, haz que la función regrese una lista vacía.
# Ejemplo: valores_multiplicados_segundo([1, 3, 5, 7]) debe imprimir 4 y devolver [3, 9, 15, 21]
# Ejemplo: valores_multiplicados_segundo([1]) debe imprimir 1 y devolver [ ]

def valores_multiplicados_segundo(lista):
    print(len(lista))
    if len(lista) > 1:
        return [lista[1]*i for i in lista]
    else:
        return []
    
print(valores_multiplicados_segundo([1, 3, 5, 7]))
print(valores_multiplicados_segundo([1]))

# Valor multiplicado y longitud: escribe una función que reciba dos números enteros: valor y longitud. La función debe crear y regresar una lista cuyo tamaño sea igual a la longitud recibida y los valores sean igual a la longitud multiplicada por el valor dado.
# Ejemplo: valor_multiplicado_longitud(5, 2) regresa [10, 10]
# Ejemplo: valor_multiplicado_longitud(7, 5) regresa [35, 35, 35, 35, 35]

def valor_multiplicado_longitud(valor, longitud):
    lista = [valor*longitud for i in range(longitud)]
    return lista

print(valor_multiplicado_longitud(5, 2))
print(valor_multiplicado_longitud(7, 5))