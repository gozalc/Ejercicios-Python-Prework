# Crea un programa que cuente el número de vocales en una palabra ingresada por el usuario
palabra=input('Introduce una palabra')
print(f'La palabra que has introducido es {palabra}')
vocales='aeiou'
contador_vocales=0
for letra in palabra:
  if letra in vocales:
    contador_vocales += 1
print(f'tiene {contador_vocales} vocales')