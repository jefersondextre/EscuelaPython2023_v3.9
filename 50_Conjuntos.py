# conjuntos: No se respeta ningun orden
#  No puede almacenar valores repetidos

# conjunto vacio
a = set()
print(type(a))
a={'a','b','c','a'}

print(a)
# un string convertido en set o conjunto
a = set('abracadabra')
print(a)

b = set('Alacazam')
print(b)

# letras de a que no estan en b
print(a - b)

# letras en a o b o ambas
print(a | b)

# Letras tanto en a y en b
print(a & b)

# letras en a o en b pero no en ambas
print(a ^ b)

# METODOS:  
a = {'a','b','c'}
a.add('d')
print(a)
a.add('a') # No se vuelve a agregar ya que no acepta elementos repetidos
print(a)

# ELimina eleemento por valor
a.discard('b')
print(a)

a.clear()
print(a)
