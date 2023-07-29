'''
Aplicación 01: Crear un sistema que detecte si número es par positivos o par negativo
y también si es impar positivo o negativos y si el numero ingresado es 0 que detecte si es neutro.
Enunciado: determinar si un número entero es par positivo, impar positivo, par negativo,
impar negativo o neutro.
Análisis: para la solución de este problema, se requiere que el usuario ingrese un número
entero y el sistema verifique si es par positivo, impar positivo, par negativo, impar negativo o neutro.

'''

# ENTRADA
numero = int(input("Ingrese el número a analizar: "))
# PROCESO
signo='negativo'
if (numero < 0):
  if (numero % 2)== 0 :
    print(f"El numero {numero} es par {signo}")
  else:
    print(f"El numero {numero} es impar {signo}")
elif (numero > 0):
  signo = 'positivo'
  if (numero % 2)== 0 :
    print(f"El numero {numero} es par {signo}")
  else:
    print(f"El numero {numero} es impar {signo}")
elif numero == 0 :
  print('El numero es neutro sin signo')
  
# 40 ======================
n = int(input("Ingrese el número a analizar: "))
if n != 0:
  if n > 0 : 
    if n % 2 == 0 :
      print(f'El numero {n} es PAR POSITIVO')
    else:
      print(f'El numero {n} es IMPAR POSITIVO')
  else:
    if n % 2 == 0 :
      print(f'El numero {n} es PAR NEGATIVO')
    else:
      print(f'El numero {n} es IMPAR NEGATIVO')
else:
  print(f'El numero {n} es neutro')
