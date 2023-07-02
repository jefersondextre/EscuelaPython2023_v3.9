squares = [1,4,9,16,25]
print(squares)

print(squares[-1])

datos = ['Alex',25,'Peru']
print(datos[0])
print(datos[-1])
print(datos[1:])
print(datos[:])
# Listas mutables, pueden ser modificables
datos[0]='Roel'
print(datos)

datos[1]=26
print(datos)

# 
# agregar datos 
datos.append(2.55)
print(datos)
print(len(datos))

# sumar listas
print(datos + squares)
# multiplicar
print(datos*3)
# crear una lista en base a 2 ya existentes
todos = datos + squares
print(todos)
print(type(todos))