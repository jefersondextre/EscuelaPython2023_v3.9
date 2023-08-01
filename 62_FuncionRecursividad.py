'''
Recursividad:

'''

def factorial(num):
    print('Valor inicial =>',num)
    if  num > 1 :
        num = num * factorial(num-1)
    print('valor final =>',num)
    return num

n=int(input('Ingrese un numero: '))
f= factorial(n)
print('Su factorial es: ',f)