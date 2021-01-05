# crear vector funcion c
c(1,2,3)
x = c

#crear vector repetido con el valor 1981
y = rep(1981,10)

y

# crear vector y modificar un indice
vec = c(16,0,1,20,1,7,88,5,1,9)
fix(vec)


vec
# vectores en secuencia con saltos(by) de n en n
seq(5, 60, by =3) 
seq(5, 60, by =5)

# vectores en secuencia con saltos(by) de n en n y longitud de 3
seq(5, by = 1.5 ,length.out =3) 

# vectores en secuencia de n a m

1:5

-1:5

#----------------------------------
#Ejercicios

#numeros del 1 al 20
1:20

#los primeros numeros pares
seq(2, by = 2 ,length.out =20)

# los 30 num de 17 a 30
seq(17,98,length.out =30) 

#-----------------------------------

# sapply para aplicar funciones a los vectores
z = 1:4
z
z = sapply(z, FUN = function(elemento){sqrt(elemento)})
z


# Subvector

v = c(14,3,5,7,9)

v[2]

which.min(v) ## posicion del menor

v[v<7] # elementos menores a 7

# Factores

nombre = c("Juan", "Ricardo", "Antonio", "Juan", "Juan","Maria", "Maria")
nombre_factor = factor(nombre)
nombre_factor

# listas

x =c(1,5,-2,6,8,-7)

L = list(nombre = "temperturas", datos = x, media = mean(x), sumas = cumsum(x))

L

L$datos[3] # accede al elemento 3 del vector guardado en datos


str(L) # ver estructura

names(L) # nombre de componentes

# Matrices

M = matrix(1:12, nrow=4)# ordenada por columna

M

M = matrix(1:12, nrow=4, byrow=T) #Ordenada por fila

M

#Ejercicio Matriz

v = c(1:12)
v
matriz = matrix(v,nrow = 3)
matriz


# aplicar funciones a matrices
apply (matriz, MARGIN=1, FUN= function (x){sum(x^2)}) # aplicar por filas

apply (matriz, MARGIN= c(1,2), FUN= function (x){sum(x^2)}) # aplicar por elemento


