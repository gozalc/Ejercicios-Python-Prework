#Crea un programa que calcule el precio final de un artículo después de aplicar un descuento del 20%.
descuento= 0.2
precio_inicial= float(input('Introduce el precio inicial de un artículo: '))
precio_final = precio_inicial*(1-descuento)
print(f'El precio con el descuento del 20% aplicado es de {precio_final} €')