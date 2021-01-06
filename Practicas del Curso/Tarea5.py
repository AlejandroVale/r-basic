import numpy as np
import math

#1

def ecuacion (a,b,c):
    if ((b**2)-4*a*c) < 0:
        print("La solución  es con numeros complejos")
        return
    else:
           x1 = (-b+math.sqrt(b**2-(4*a*c)))/(2*a)  
           x2 = (-b-math.sqrt(b**2-(4*a*c)))/(2*a)
           return (x1,x2)   
    
    

x = input("Introduzca los valores de A, B y C separados por coma :")
y = x.split(',')
print(ecuacion (float(y[0]),float(y[1]),float(y[2])))

#2

def palindrome(texto): ##no identifica las tildes
    cont = 0
    frase = texto.replace(" ","")
    for x in reversed(range(0,len(frase))):
        if frase[x].upper() != frase[cont].upper():
            igual = "No es una frase palindrome"
            return igual
        cont +=1

    return "Es una frase palindrome"

print (palindrome('La ruta nos aporto otro paso natural'))


#3 Crea un diccionario que tenga por claves los números del 1 al 10 y como valores sus raíces cuadradas

claves = np.arange(1,11)
valores = np.sqrt(claves)
dic = dict(zip(valores,claves))


#4
codigo_morse = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", 
    "g": "--.", "h": "....", "i": "..", "j": "·---", "k": "-.-", "l": ".-..", 
    "m": "--", "n": "-.", "ñ": "--.--", "o": "---", "p": ".__.", "q": "--.-",
    "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--",
    "x": "-..-", "y": "-.--", "z": "--..",}

texto = input("Ingrese  texto a codificar: ")
codigo =""
for c in texto:
    if c != " " and c.lower() in codigo_morse:
        codigo += codigo_morse[c.lower()]
    else:
        codigo += c
    
print("El codigo es: {}".format(codigo))

#5