# Escribe un programa que solicite la edad de un usuario y determine si es mayor de edad (mayor o igual a 18 años) o no.

edad = input('Por favor, introduce tu edad: ')
print(f'Has introducido {edad}')
años=int(edad)
if años<18:
  print('No es mayor de edad')
else:
  print('Es mayor de edad')
