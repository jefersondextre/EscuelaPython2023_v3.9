
'''
Practica 01: Calcular cociente y el Residuo de dos números enteros
Enunciado: halar el cociente y el residuo (resto) de dos números enteros.

Análisis: para la solución de este problema, se requiere que el usuario 
ingrese dos números enteros y el sistema realice el cálculo respectivo 
para hallar el cociente y residuo, para esto use la siguiente expresión.

'''
print("------- Ingrese los numeros -----")
dividendo=int(input('Ingrese el dividendo: '))
divisor = int(input('Ingrese el divisor: '))
cociente = dividendo // divisor  # division entera.
residuo = dividendo % divisor    # modulo entre los operandos.

print(f'El residuo es {residuo} y el cociente es {cociente}')