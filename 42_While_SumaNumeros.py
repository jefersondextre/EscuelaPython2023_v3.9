'''
Aplicación 03: Suma de n números anteriores
Enunciado: obtener la suma de los primeros 
N número natural positivo.

Análisis: Para la solución de este problema, 
se requiere que el usuario ingrese un número y 
el sistema realice el proceso para devolver la
suma de los N primeros números.

'''
# Entrada
num = int(input('Ingrese un numero:'))
c=0
while num > 0:
  suma=0
  num -=1
suma += num 
print( f'La suma de los numeros anteriores a {num} es: {suma}')  
