#import numpy as np
#import math

def cifrado_cesar(palabra):# trabajamos todo con minusculas
    letras = list(map(chr, range(97, 123)))
    abc = dict(zip(letras,range(0,len(letras))))
    palabra = palabra.lower()
    codigo=""
    print("Diccionario:",abc)
    print("Frase a codificar:",palabra)
    for letra in range(0,len(palabra)):
        if palabra[letra] in range(0,9) or palabra[letra] == " ":
            codigo += palabra[letra]
        else:
            posi = abc.get(palabra[letra]) + 3
            if (posi > 25):
                posi = posi - 26
            codigo += letras[posi]
   
    return(codigo)


print("Frase codificada: ",cifrado_cesar("Hola"))
