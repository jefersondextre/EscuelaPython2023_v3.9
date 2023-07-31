def saludar():
    global apellido
    apellido='Dextre' 
    edad = 25
    return 'Hola desde la funcion saludar'

saludar()
print(saludar())
valor = saludar()
print(valor)
# print('Hola desde fuera de la funcion', apellido)