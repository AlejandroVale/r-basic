
import math

def what_num ():

    num_real = float(input("Introduce un numero real: "))

    if num_real < 0:
        print("Numero menor a cero...!")
    elif num_real > 0:
        print("Numero mayor a cero...!")

    else: 
        print("Es un cero..!")


def interva_num ():

    num_real = float(input("Introduce un numero real: "))

    if num_real < 5 and num_real > -5:
        print("Esta en el rango entre -5 y 5")
    elif num_real > 0:
        print("No esta en el rango entre -5 y 5!")

    
def cuadrante (x,y):
    
    if x > 0 and y >0 :
        print("Primer cuadrante")
    elif x < 0 and y >0 :
        print("Segundo cuadrante")
    elif x < 0 and y < 0 :
        print("Tercer cuadrante")
    elif x > 0 and y < 0 :
        print("Cuarto cuadrante")
    else:
        print("sobre cero")


def cociente_resto (x,y):
    print("Dividendo: " + str(x) + " Divisor: " + str(y)) # Cociente
    print("Cociente: " + str(x//y)) # Cociente
    print("Resto: " + str(math.fmod(x,y))) # Resto
    

def cuadrado_perfecto():

    num_real = float(input("Introduce un numero : "))

    if math.sqrt(num_real) * math.sqrt(num_real) == num_real:
        print("Cuadrado perfecto")
    else:
        print("No es cuadrado perfecto")


def Ano_bisiesto():

    ano = float(input("Introduce un ano : "))

    if math.fmod(ano,4) == 0:
        if math.fmod(ano,100) == 0:
          if math.fmod(ano,400) == 0:
            print("Ano bisiesto")
          else:
            print("Ano no bisiesto")
        else:
            print("Ano bisiesto")
   
    else:
        print("Ano no bisiesto")


def casilla_ajedrez():
    
    fila =["A","B","C","D","E","F","G","H"]
    letra = str.upper(input("Introduce una letra : "))
    num = int(input("Introduce un numero : "))
    

    if letra not in fila or num > 5 or num < 0 :
        print ("Casilla fuera de rango..!")
        return

    if num == fila.index(letra) + 1 or  math.fmod(fila.index(letra) + 1+ num,2) == 0:
        print("Casilla negra ..!")
    else:
        print("Casilla blanca")
    
    


what_num ()

interva_num ()

cuadrante(0,2)

cociente_resto (7,3)

cuadrado_perfecto()

Ano_bisiesto()

casilla_ajedrez()


