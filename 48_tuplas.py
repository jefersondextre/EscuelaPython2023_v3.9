# Tuplas : Son datos compuestos que no pueden ser modificadas (Son inmutables).
tupla = ('Alex',25,1.67)
# aunque no se puede modificar si podemos obtener, contar,
print(tupla[0])
print(tupla[-1])
print(tupla[:])

# tupla[0]='Roel'
print(tupla)
print(len(tupla),' elementos')
print(tupla.index(25))
print(tupla.index('Alex'))  
# Si el parámetro no esta en la tupla me indica como valor erroneo:  ValueError: tuple.index(x): x not in tuple