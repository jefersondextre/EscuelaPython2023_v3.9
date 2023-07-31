def saludar(nombre):
    # global apellido
    # apellido='Dextre'
    # edad = 25
    return f'Hola, {nombre} desde la funcion saludar',

def sumar(a,b):
    return a+b

def restar(a=None,b=None):
    if a == None or b ==None:
        print("Error: Debes enviar dos numeros a la funcion")
        return 
    return a-b

saludo = saludar('Antonio')
print(saludo)

suma = sumar(5,6)
print('La suma es: ',suma)

resta = restar(b=50,a=20)
print('La resta es:', resta) 