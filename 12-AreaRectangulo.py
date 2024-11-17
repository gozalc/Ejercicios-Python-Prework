 #Crea un programa que calcule el área de un rectángulo. El usuario debe ingresar la longitud y el ancho del rectángulo
 
try:
  longitud = float(input('Introduce la longitud de un rectángulo en cm'))
  ancho = float(input('Introduce el ancho de un rectángulo en cm'))
  area = longitud*ancho
  print(f'El area para las dimensiones indicadas es de {area} cm^2')
except ValueError:
  print('Introduce un número correcto')