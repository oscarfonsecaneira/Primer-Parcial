import numpy as np
import math

def funcion (x):
  return math.log(x+2,math.exp(1)) + np.sin(x)

def formula (x1,x2):
  return x1-((funcion(x1)*(x1-x2))/(funcion(x1)-funcion(x2)))

def operacion(x,x1,x2,E):
  if funcion(x) > E or funcion(x) < 0:
    x2 = x1
    x1 = x
    x = formula(x1,x2)
    return operacion(x,x1,x2,E)
  else:
    return x

E = 0.0000001
intervalo = [-1.9,1]
x1 = intervalo[0]
x2 = intervalo[1]
x = formula(x1,x2)
print("El punto de interseccion es:",operacion(x,x1,x2,E))
