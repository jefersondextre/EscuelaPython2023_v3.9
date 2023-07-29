c= 0
while c < 10:
    c +=1
    if c == 3:
        print('Salta a la siguiente iteración')
        continue
    
    print(c)
    if c is 5:
        print('--- Termina el bucle ---')
        break
else:
    print('Fin de While')