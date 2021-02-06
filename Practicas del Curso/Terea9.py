import pandas as pd

#Leemos archivo

df = pd.read_csv("run.csv")

print(df)

# 1.Indica cuantos estudiantes formaron parte del estudio de deporte
import pandas as pd
df = pd.read_csv("run.csv")
print("Numero de estudiantes del estudio: ",len(df))

# 2.Indica cuantos individuos son hombres y cuantos son mujeres
import pandas as pd
df = pd.read_csv("run.csv")
df = df.groupby('genero').count()
print (df.iloc[:,[0]])

# 3. Calcula el porcentaje medio de variación del pulso por minuto entre antes y 
#    después de hacer ejercicio y compara el valor de los que hacen ejercicio habitualmente y los que no. 
#    ¿Observas mucha diferencia?
import pandas as pd
import numpy as np
df = pd.read_csv("run.csv")

def por_medio(x):# Aplico el coeficiente de variacion
    return np.std(x) / np.mean(x) *100

df = df.groupby('hace.deporte').aggregate(por_medio)

print(df.iloc[:,[1,2]])

#Varia mas en los que hacen ejercicio

#4

import pandas as pd
import numpy as np
df = pd.read_csv("run.csv")

def por_medio2(x): # Aplico el coeficiente de variacion
    return np.std(x) / np.mean(x) *100

df = df[df['hace.deporte'] == 'si'].groupby('genero').aggregate(por_medio2)

print(df.iloc[:,[1,2]])

# Varia mas en mujeres

#5

import pandas as pd
import numpy as np
df = pd.read_csv("run.csv")

def por_medio3(x): # Aplico el coeficiente de variacion
    return np.std(x) / np.mean(x) *100

df = df[df['hace.deporte'] == 'no'].groupby('fuma').aggregate(por_medio3)

print(df.iloc[:,[1,2]])

# Varia mas en fumadores

#6

import pandas as pd
import numpy as np
df = pd.read_csv("run.csv")

def por_medio4(x): # Aplico el coeficiente de variacion
    return np.std(x) / np.mean(x) *100

df = df.groupby('tipo.actividad').aggregate(por_medio4)

print(df.iloc[:,[1,2]])

# Varia mucho en tipos de actividad moderado