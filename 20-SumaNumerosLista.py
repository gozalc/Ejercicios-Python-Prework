# Crea un programa que sume todos los números en una lista ingresada por el usuario.

Lista = input('Introduce una lista de numeros separados por ","')
Lista_Separada = Lista.split(',') # Dividir la cadena de entrada en una lista de cadenas
Lista_Numeros = [int(numero) for numero in Lista_Separada] # Convertir la lista de cadenas en una lista de números
suma=0
for numero in Lista_Numeros:
  suma+=int(numero)
print(f'La suma de los numeros introducidos es {suma}')