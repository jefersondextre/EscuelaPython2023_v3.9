datos = ['Jeferson', 25,'Peru']

datos.append('Roel')
print(datos)

# Se extiende 
datos.extend(datos)
print(datos)

datos.insert(2,'Soids')
print(datos)

# Remueve la primera coincidencia de izq a derecha, en funcion del valor pasado como parametro
datos.remove('Peru')
print(datos)

# retorna el ultimo valor y la elimina de la lista
value = datos.pop()
print(datos)
print(value)

datos.clear() #Elimina todos los elementos de la lista
print(datos)

datos2 = [100,100,'Jeferson', 25,'Peru']
datos2.index(25)
print(datos2)

# cuenta el numero de veces que se repite el valor pasado como parametro
datos2.count(100)
print(datos2)

# =================
frutas = ['Sandia','manzana','Palta','aguacate','uva']
print(frutas)
frutas.sort()
print(frutas)

# hace una copia a la lista
frutas_otra=frutas.copy()
print(frutas_otra)

# ===========
numbers = [1,2,3,4,5,6]
numbers.reverse()
print(numbers)

