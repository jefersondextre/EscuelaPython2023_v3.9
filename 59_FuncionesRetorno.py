def saludar():
    global apellido
    apellido='Dextre'
    edad = 25
    return 'Hola desde la funcion saludar',25,apellido

texto,edad,apellido=saludar()
print(saludar())
print(texto)
print(apellido)
print(edad) 
valor = saludar()
print(valor)
# print('Hola desde fuera de la funcion', apellido)