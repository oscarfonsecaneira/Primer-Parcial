def suma(matriz):
  print (matriz)
  suma = 0
  for i in range (0,len(matriz)):
    for j in range (0,len(matriz[i])):
      suma = suma + matriz[i][j]
  return suma

import numpy as np
matriz = np.array([[1,2,4],[10,11,14],[10,12,10]])
print("Con n=3, la suma de la matriz es:",suma(matriz))
matriz = np.array([[1,20],[13,3,]])
print("Con n=2, la suma de la matriz es:",suma(matriz))
matriz = np.array([[1,2,4,9],[10,11,14,20],[10,12,10,12],[1,2,3,4]])
print("Con n=4, la suma de la matriz es:",suma(matriz))
