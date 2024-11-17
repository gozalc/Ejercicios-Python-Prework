#Crea un programa que realice operaciones aritméticas simples (suma, resta, multiplicación, división) según la elección del usuario.
operador = input('Introduce la operación a realizar: suma, resta, multiplicacion, division')
numero1 = input('Introduce el primer valor')
operador1 = float(numero1)
numero2 = input('Introduce el segundo valor')
operador2 = float(numero2)
print(f'La operacion solicitada es la {operador} entre {operador1} y {operador2}')
if operador=='suma':
  resultado = operador1 + operador2
elif operador == 'resta':
  resultado = operador1 - operador2
elif operador == 'multiplicacion':
  resultado = operador1 * operador2
elif operador == 'division':
  resultado = operador1 / operador2
print(f'El resultado de la operación es: {resultado}') 

#sugerencia solucion
def calcular():
    # Pedir al usuario que elija una operación
    operador = input('Introduce la operación a realizar: suma, resta, multiplicacion, division: ')

    # Validar la operación
    if operador not in ['suma', 'resta', 'multiplicacion', 'division']:
        print("Operación no válida")
        return

    try:
        # Pedir al usuario que introduzca dos números
        numero1 = float(input('Introduce el primer valor: '))
        numero2 = float(input('Introduce el segundo valor: '))

        # Realizar la operación correspondiente
        if operador == 'suma':
            resultado = numero1 + numero2
        elif operador == 'resta':
            resultado = numero1 - numero2
        elif operador == 'multiplicacion':
            resultado = numero1 * numero2
        elif operador == 'division':
            if numero2 != 0:
                resultado = numero1 / numero2
            else:
                print("Error: No se puede dividir por cero")
                return

        print(f'El resultado de la operación es: {resultado}')
    except ValueError:
        print("Error: Por favor, introduce números válidos")

# Llamar a la función para ejecutar el programa
calcular()
