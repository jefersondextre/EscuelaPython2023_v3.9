'''
Practica 02: Calcular el Precio de Venta
Enunciado: dado el valor de venta de productos, hallar el IGV (18%) y el
precio de venta.

Análisis: para la solución de este problema, se requiere que el usuario
ingrese el valor de venta del producto y el sistema realice el cálculo 
respectivo para hallar el IGV y el precio de venta, para esto use 
la siguiente expresión.

igv = vv * 0.18

pv = vv + igv

'''


precProducto = float(input("Ingrese el precio del producto S/.: "))
IGV = 0.18 * precProducto
# IGV= round(IGV)
precVenta = precProducto + IGV

# Salida
print(f'''El precio de venta es: {precVenta} S/. ,
      incluye el IGV con un valor de {IGV} S/.
      
      ''')