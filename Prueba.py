y = [4,15,24,56]
print "El primero es ", y[0], "y el ultimo es ", y[3]

print range(7)

for i in range(3):
    print "Hola"
    print "Adios xd"
print "Hasta Luego"

y.append("Bye")
print y

x=[100]
for i in range(100):
    x.append(1.01*x[i])
print x

# x=[1,1]
# for i in range(15):
#     x.append(x[i]+x[i+1])
# print x

import matplotlib.pyplot as plt
plt.plot(x)
plt.show(x)

def suma(x,y):
    return x+y

suma(2,3)

def producto(x,y):
    return x*y

producto(2,2.5)

def operacion(x,y,f):
    return f(x,y)

operacion(2,3,producto)

def funcion(x):
    return 1.01*x

def pordos(x):
    return 2*x

import math

def iteracion(inicial,iteraciones,f):
    x=[inicial]
    for i in range(iteraciones):
        x.append(f(x[i]))
    return x

import math

valores=iteracion(0,30,math.cos)
print valores
plt.plot(valores)
plt.show(valores)


import numpy as np

def diagrama(f, x0, it):
    x = [x0]
    y = [x0]
    s = np.arange(0, 1, 0.01 )
    for i in range(it):
        x.append(x[2*i])
        x.append(f(x[2*i]))
        y.append(f(y[2*i]))
        y.append(f(y[2*i]))
    plt.plot(x, y, color= 'red')
    plt.plot(s, f(s))
    plt.plot(s, s, color='black')
    plt.show()

def logistica(x):
    return 3.8*x*(1-x)
    
diagrama(logistica,0.1,50000)
