'''
Aplicación 02: Crear un sistema que detecte si un carácter es vocal o no
Enunciado: dado un carácter determinar si es una vocal.

Análisis: para la solución de este problema, se requiere que el usuario ingrese un carácter 
y el sistema verifique si es una vocal.
'''
caract = input("Ingrese su caracter: ").upper()

# if caract == "A":
#   print(f"El caracter {caract} ingresado es una vocal")
# elif caract == "E":
#   print(f"El caracter {caract} ingresado es una vocal")
# elif caract == "I":
#   print(f"El caracter {caract} ingresado es una vocal")
# elif caract == "O":
#   print(f"El caracter {caract} ingresado es una vocal")
# elif caract =="U":
#   print(f"El caracter {caract} ingresado es una vocal")
# else:
#   print(f'el caracter ingresado {caract} no es una vocal') 

# =========================================================

if caract == "A" or caract =="E" or caract =="I" or caract =="O" or caract =="U":
  print(f"El caracter {caract} ingresado es una vocal")
else:
  print('No es un caracter válido')  
