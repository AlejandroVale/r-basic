import numpy as np
import pandas as pan
L1 =[]
L2 = ['a','e','i','o','u'] # Lista con valores iniciales

print(L2[0]) # Las listas comienzan en cero

print(L2[0:5])

L2.append(1) # Agrega un elemento a la lista
print(L2)

L2.remove(1) # elimina la primera ocurrencia
print(L2)
print("Sentencia for")
for p in range(10):
    print(p)


print("Sentencia while")
x = 1
while x < 7:
    print(x)
    x = x+1 

# Trabajando con numpy

L1 = [1,2,3,4,5,6,7,8]
x1 = np.array(L1)

print(L1)
 
print(np.ones((3,4))) #Matriz de unos de 3 x 4

print(np.arange(10))# arreglo de 10 posiciones desde el 0

print(np.arange(4,5,0.1)) #arreglo de 4 a 5 incrementando en 0.1

print(np.linspace(4,10,12)) # arreglo de 12 posiciones de 4 a 10

#Crear array de datos con valores entre 5 y 120

print(np.arange(5,120))

#Crear una matriz de 4x4 con los valores desde 0 hasta 15
x = np.arange(0,16)
print(x.reshape(4,4))

#Crear la identidad 7 x 7

print(np.eye(7,7))

#crear un array de 20 elementos y convertir en matriz
x = np.arange(0,20)
x = x.reshape(5,4)
print(x)

#Propiedades de los Arrays
##########################

print(x.shape) #filas y columnas

print(x.size) #num de elementos

print(x.itemsize) #tamano en byte de cada elemento

print(x[2]) #la fila 2

# Copia de Arreglos

x = np.arange(10)

y = x

y.shape = (2,5) # Modifico x tambien, la asignacion es un apuntador y no or valor

z = x.copy() # Si se hace la copia de valores


# Algebra lineal con Pyhton

M = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(M)

# np.linlg esta libreria de algebra lineal