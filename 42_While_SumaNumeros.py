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
suma  = 0
menores_num = 0
while menores_num < num:
        suma += menores_num 
        menores_num +=1
print( f'La suma de los numeros anteriores a {num} es: {suma}')  
