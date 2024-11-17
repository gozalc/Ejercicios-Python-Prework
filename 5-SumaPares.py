# Escribe un programa que calcule la suma de todos los números pares del 1 al 100.
numeros = range(101)
suma=0
for numero in numeros:
  if numero % 2 == 0:
    suma+=numero
print(suma)