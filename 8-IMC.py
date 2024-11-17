#Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.
try:
  peso = float(input('Introduce tu peso en kg'))
  altura = float(input('Introduce tu altura en cm'))/100
  IMC = peso/(altura*altura)
  print (f'El IMC para los datos introducidos es {IMC}')
except ValueError:
    print("Error: Por favor, introduce un número válido")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero")
