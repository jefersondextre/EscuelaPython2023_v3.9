'''

'''
cadena ="Hola mundo"
print(cadena.upper())
print(cadena.lower())
print(cadena.capitalize())
print(cadena.title())
print(cadena.count('o'))
print(cadena.upper())
palabra = 'Python'
palabra = palabra.replace('P','S')
print(palabra)
print('P y t h  o      n '.replace(' ',''))
print('  Ho la mundo  s    '.strip())
print('------ Hola - Mundo -----'.strip('-'))
# separa elementos de cadena en elementos de lista por el espacio vacio
print('Hola Mundo'.split())
print('Hola, mundo , de python , hoy'.split(','))
# verifica si cadena esta en minuscula o mayuscula todos , devuelve booleano
print('hola '. islower())
print('Hola '. islower())
print('hola '. isupper())
print('HOLA '. isupper())
# evalua si es un titulo o no devuelve booleano
print('Hola Mundo'.istitle())
# Devuelve booleano si la cadena esta compuesta de puros espacios vacios o tiene algun caracter.
print('             '.isspace())
print('       sdf      '.isspace())
