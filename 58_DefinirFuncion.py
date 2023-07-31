def saludar():
    global apellido
    apellido='Dextre' 
    nombre = 'Jeferson'
    print('Hola desde la funcion saludar')
    print('hola',nombre)

saludar()
print('Hola desde fuera de la funcion', apellido)