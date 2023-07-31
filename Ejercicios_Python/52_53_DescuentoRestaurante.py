''' 52)
Practica 01: Descuentos de un restaurante
Enunciado: un restaurante ofrece un descuento del 10% para consumo de
hasta s/. 100.00 y un descuento del 20 % para consumos mayores, para 
ambos casos se aplica un impuesto del 19%. Determinar el monto del descuento,
el impuesto y el importe a pagar.

Análisis: para la solución de este problema, se requiere que el usuario 
ingrese el consumo y el sistema verifica y calcula el monto del descuento, 
el impuesto y el importe a pagar.

monto del descuento

impuesto

importe a pagar
'''

# consumo = float(input('Ingrese el consumo total: '))

# if consumo <= 100:
#     valor_desc ='10 %'
#     descuento = 0.10*consumo
# elif consumo>100:
#     valor_desc = '20 %'
#     descuento = 0.20*consumo
    
# monto_descuento = consumo - descuento
# impuesto =  monto_descuento * 0.19
# importeApagar =  impuesto + monto_descuento

# print('*'*38)
# print('********** FACTURA DE CONSUMO ********')
# print(f'****** El descuento es de {valor_desc} ******* ')
# print('*'*38)
# print(f'El consumo: {consumo} S/.')
# print(f'Descuento : {descuento} S/.')
# print(f'Monto con Descuento : {monto_descuento} S/.')
# print(f'El impuesto IGV es de: {impuesto} S/.')
# print(f'El importe a pagar es de: {importeApagar} S/.')

''' 53)
Practica 02: Descuentos de un restaurante Parte 02
Enunciado: debido a los excelentes resultados, el restaurante decide 
ampliar sus ofertas de acuerdo a la siguiente escala de consumo, ver
la tabla. Determinar el monto del descuento, el importe del impuesto 
y el importe a pagar.

Consumo (S/.)       Descuento (%)

Hasta 100                 10

Mayor a 100             20

Mayor a 200             30

Análisis: para la solución de este problema, se requiere que el usuario ingrese
el consumo y el sistema verifica y calcula el monto del descuento, el impuesto 
y el importe a pagar.
'''

consumo = float(input('Ingrese el consumo total: '))

if consumo <= 100:
    valor_desc ='10 %'
    descuento = 0.10*consumo
elif consumo>100 and consumo<=200:
    valor_desc = '20 %'
    descuento = 0.20*consumo
elif consumo>200:
    valor_desc = '30 %'
    descuento = 0.30*consumo
    
monto_descuento = consumo - descuento
impuesto =  monto_descuento * 0.19
importeApagar =  impuesto + monto_descuento

print('*'*38)
print('********** FACTURA DE CONSUMO ********')
print(f'****** El descuento es de {valor_desc} ******* ')
print('*'*38)
print(f'El consumo: {consumo} S/.')
print(f'Descuento : {descuento} S/.')
print(f'Monto con Descuento : {monto_descuento} S/.')
print(f'El impuesto IGV es de: {impuesto} S/.')
print(f'El importe a pagar es de: {importeApagar} S/.')