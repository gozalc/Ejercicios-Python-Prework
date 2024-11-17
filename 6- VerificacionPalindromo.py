 #Crea un programa que verifique si una palabra ingresada por el usuario es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
palabra = input('Introduce a continuación una palabra y te diré si es un palíndromo')
palabra_invertida = palabra[::-1]
if palabra_invertida == palabra:
  print('Es un palíndromo')
else: 
  print('No es un palíndromo')
  
