## Ejercicio 1. Básico

for i in range(101):
    print(i)

################################################################################

## Ejercicio 2. Múltiples de 2

for i in range(2,501):
    if i%2 == 0:
        print(i)

################################################################################

## Ejercicio 3. Contando Vanilla Ice

for i in range(1,101):
    if i%10 == 0:
        print("baby")
    elif i%5 == 0:
        print("ice ice")
    else:
        print(i)

################################################################################

## Ejercicio 4. Wow. Número gigante a la vista

suma = 0

for i in range (500001):
    if i%2 == 0:
        suma += i

print(suma)

################################################################################

## Ejercicio 5. Regrésame al 3

for i in range(2024, 0, -3):
    print(i)

################################################################################

## Ejercicio 6. Contador dinámico

numInicial = 3
numFinal = 10
multiplo = 2

for i in range(numInicial,numFinal+1):
    if i%multiplo == 0:
        print(i)

lista_prueba = [2, 3, 4]

lista_prueba += [7]

print(lista_prueba)