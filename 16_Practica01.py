
'''
Practica 01: Calcular cociente y el Residuo de dos números enteros
Enunciado: halar el cociente y el residuo (resto) de dos números enteros.

Análisis: para la solución de este problema, se requiere que el usuario 
ingrese dos números enteros y el sistema realice el cálculo respectivo 
para hallar el cociente y residuo, para esto use la siguiente expresión.

'''
print("------- Ingrese los numeros -----")
div=int(input('Ingrese el dividendo: '))
divis = int(input('Ingrese el divisor: '))
residuo = div % divis
cociente = div // divis

print(f'El residuo es {residuo} y el cociente es {cociente}')