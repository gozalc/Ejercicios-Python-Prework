#Escribe un programa que convierta un número de minutos en horas y minutos. Por ejemplo, 145 minutos serían 2 horas y 25 minutos.
total_minutos = int(input('Introduce un número de minutos sin decimales  '))
horas = total_minutos //60
minutos = total_minutos % 60
print(f'Equivale a {horas} horas y {minutos} minutos')
