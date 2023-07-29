from collections import deque
# Colas : el primero en entrar 
#      es el primero en salir
    
cola = deque(["Jeferson","Dextre","Barrientos"])
cola.append("Antonio")
cola.append(52)
print(cola)
cola.popleft() # Quita el elemento que esta mas a la izquierda
cola.popleft()
print(cola)     