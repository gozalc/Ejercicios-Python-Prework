#Escribe un programa que determine el día de la semana correspondiente a un número ingresado por el usuario (1 para lunes, 2 para martes, etc.)

try:
  NumeroUsuario=int(input('Introduce un nº del 1 al 7, siendo 1 lunes y 7 domingo'))
  dias = { 1: "Lunes", 2: "Martes", 3: "Miércoles", 4: "Jueves", 5: "Viernes", 6: "Sábado", 7: "Domingo" }
  for numero, dia in dias.items(): 
    if numero == NumeroUsuario:
     print(dia)
    
except ValueError:
    print("Error: Por favor, introduce un número válido")
