#Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad actual
try:
  año=int(input('Introduce tu año de nacimiento'))
  diferencia=2024-año
  diferencia2= diferencia-1
  print(f'Tu edad es de {diferencia} o {diferencia2} años')
except ValueError:
 print("Error: Por favor, introduce un número válido")
 
 
"""He buscado y realmente se haria: usando la libredia datetime import date para saber la fecha actual, lo he hecho en el ejemplo suponiendo 2024 simplemente"""