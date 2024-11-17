#Crea un programa que cuente la cantidad de palabras en una oración ingresada por el usuario.

frase = str(input('Introduce una frase: '))

def contador_palabras(fraseintroducida, caracter): 
  contador = 0 
  for x in fraseintroducida: 
    if x == caracter: 
      contador+= 1 
  return contador 
mi_cadena = "hola mundo" 
print(contador_palabras(frase,' ')+1)  #le pongo un +1 porque siempre habra una palabra mas que el numero de espacios