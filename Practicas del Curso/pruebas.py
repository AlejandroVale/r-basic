import numpy as np
import math


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