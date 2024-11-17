#Crea un programa que cuente y muestre la cantidad de números pares e impares en una lista ingresada por el usuario
# Pedir al usuario que introduzca una lista de números separados por comas
entrada = input("Introduce una lista de números separados por comas: ")

# Dividir la cadena de entrada en una lista de cadenas
numeros_str = entrada.split(',')

# Convertir la lista de cadenas en una lista de números
numeros = [int(numero) for numero in numeros_str]

# Inicializar contadores
pares = 0
impares = 0

# Contar números pares e impares
for numero in numeros:
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

# Mostrar los resultados
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
