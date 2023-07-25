import os 

lista = [3, 1, 4, 6, 2, 5]

mendict = {}
    
for i in range(4):
    for j in range(4):
        mendict[(i, j)] = 0
    

mendict[(3, 1)] = lista[0]
mendict[(1, 2)] = lista[1]
mendict[(0, 0)] = lista[2]
mendict[(0, 3)] = lista[3]
mendict[(2, 2)] = lista[4]
mendict[(3, 3)] = lista[5]

for i in range(4):
    for j in range(4):
        print(mendict[(i, j)], end=" ")
    print()
