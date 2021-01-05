import math
print (math.pi)
print (math.tau) # 2 veces pi

# print(math.sqrt(-1)) # error de dominio

# print (math.exp(1000)) # error de overflow

print (math.nan) # Not a Number. Esto es la definición a un objeto cualquiera (se define como objeto NAN)

print (math.ceil (3.546)) # Redondea a la alta 4
print (math.floor (3.546)) # Redondea a la baja 3

print(math.trunc(3.45)) # trunca el número arroja 3

print (2**3) # Elevar 2 a la 3  igual 8

print(math.factorial(4)) # factorial de 4 igual 24

print(math.fmod(7,3)) # Resto de 7 entre 3 igual 1

print(7//3) # Cociente de 7 entre 3 igual 2

print(math.modf(4.5)) # Separa la parte entera de la decimalss

print(math.isclose(2.1,2.099999999999)) # true

print(math.isclose(2.1,2.09)) # false

texto = input("Introduce un valor: ")

print ("Hola " + texto)

x = int(input("Escribe un número: "))

if x == 5:
    print(" has escrito el 5")
elif x < 5:
    print ("has escrito un numero menor a 5")
else:
    print ("has escrito un numero mayor a 5")



# Funciones Matematicas

print(math.exp(3)) # Elevar e a la 3

print(math.pow(math.e,3)) # otra forma de elevar e a la 3

print(math.log(12,2)) # Logaritmo de 12 en base 2

print(math.sin(math.pi))
print(math.cos(math.pi))
print(math.radians(60))
print(math.degrees(math.radians(60)))


