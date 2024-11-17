#Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que 1 dólar es igual a 0.85 euros.
try:
  dolares= float(input('Introduce un nº de dolares para convertir a euros'))
  euros = 0.85*dolares
  print(f'{dolares} $ equivalen a {euros} €')
except ValueError:
  print("Error: Por favor, introduce un número válido")
except ZeroDivisionError:
  print("Error: No se puede dividir por cero")