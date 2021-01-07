import numpy as np
import math


def MCD (x,y):
    resto = 0
    while(y > 0):
        resto = y
        y = x % y
        y = resto
    return x
print(MCD (4,2))

print("Hola mundo")