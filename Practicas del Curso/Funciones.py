import math

# Funciones en Python


def suma (x,y):
    return x+y

class Operaciones(object):
    def suma(self, x, y):
        #self.resultado = x+y
        # return self.resultado
        z=x+y
        return z


print(suma(2,3))

operInstance = Operaciones()
print (operInstance.suma(2,3))

# Funciones que devuelven tuplas

def sumaresta(x,y):
    suma = x+y
    resta = x-y
    return (suma, resta)

print(sumaresta(4,2))



# argumentos variable

def suma2(*args):
     return sum(args)


print(suma2(1,2,4))

def cuadrados(*args):
     total = 0
     for d in args:
         total = total + d**2

     return total

print(cuadrados(2,3) )   
     
# Funcion anonima o lambda

doble = lambda x: x*2

print(doble(2))




