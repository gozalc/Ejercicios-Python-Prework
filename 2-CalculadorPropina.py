#Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo una propina del 15% sobre el total de la cuenta.
plato1=10
plato2=12
plato3=3
Cuenta=[plato1,2*plato2,plato3]
Total=0
for plato in Cuenta:
  Total+= plato
Propina=1.15
TotalConPropina= Total*Propina
print(TotalConPropina)