# Diccionarios : Un conjunto de pares clave:valor y loas claves son unicas.

numeros ={
    'uno'   : 1,
    'dos'   : 2,
    'tres'  : 3,
    'cuatro': 4
}

print(numeros)
print(numeros['dos'])
numeros['cinco']=5
print(numeros)

# Metodos de diccionarios
# Busca un valor por clave, retornandome el valor correspondiente
#  Si no existe retorna el mensaje
print(numeros.get('cuatro','No se encontró'))
# devuelve todas las claves del diccionario
print(numeros.keys())
#  devuelve todos los valores del diccionario
print(numeros.values())

#  Devuelve una lista con clave y valor
print(numeros.items())
print(type(numeros.items()))

print(numeros.pop('cinco','No se encontró'))
print(numeros)

print(numeros.clear())
print(numeros)

# ==============================================
numeros2 ={
    'uno'   : 1,
    'dos'   : 2,
    'tres'  : 3,
    'cuatro': 4
}


# for numero in numeros2:
#     print(numero)

# itera y devuelve valor
for numero in numeros2.values():
    print(numero)
    
# itera clave y valor
for key, value in numeros2.items():
    print(f'clave {key} : valor {value}')