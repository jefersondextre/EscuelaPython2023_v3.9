# Puedo usar el asterisco antes de los parametros para pasar argumentos indeterminados por posicion (tupla)
#  y argumentos indeterminados por nombre (diccionarios) por ejemplo

def sumar(*args , **kwargs) :
    suma=0
    for n in args:
        suma +=n
    return suma, kwargs

sumaTotal,datos = sumar(1,2,3,4,5,6,200,nombre="Alex",edad=25)
print('La suma total: ',sumaTotal)
print(datos)