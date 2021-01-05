# 1

Harry = c(-10:27)
Harry[7]

#2

secuencia= sapply((0:200),FUN = function(n){100*2^n-7*3^n})
max(secuencia)

#3
suce=(0:40)
x=sapply(suce,FUN = function(n){3*5^n - 1})
x[x>3.5]

#4
partes = function(x){
       v = c(Re(x),Im(x), Mod(x),Arg(x), Conj(x))
       return(v)
  
}


#5

funcion_x <- function(A, B, C) {
  
    D <- B^2 - 4 * A * C
    
    if (D > 0) {
      raices = (-B + c(1, -1) * sqrt(D))/2 * A
    } else if (D == 0) {
      raices = -B/(2 * A)
    } else {
      raices = (-B + c(1, -1) * (complex(1, 0, sqrt(-D))/2 * A))
    }
  
  return(raices)
}


funcion_x(1, 5, 6)

#6 dad 3 opciones diferentes para calcular el subvector c(9,19,20,16)

vec = c(0,9,98,2,6,7,5,19,88,20,16,0)

Subvector = c(vec[2],vec[8],vec[10],vec[11]) 
Subvector = vec[-c(1,3,4,5,6,7,9,12)]
Subvector = vec[vec>=9 & vec <=20] 
Subvector

#Entradas pares

pares = vec[vec%%2 ==0] 
pares

#Entradas no pares y mayores a 20

pares = vec[vec%%2 !=0 & vec>20] 
pares

#dónde toma vec su valor máximo
which.max(vec)

#dónde toma vec su valor minimo
which.min(vec)


# Ejercicios sobre estructuras de datos

#Ejercicio 1 Dad la entrada (2,2) deA·(A+A)·A

A = matrix(1:4,nrow=2)
A
Result = A%*%(A+A)

Result[2,2]

#Ejercicio 2 Dad los valores propios de la matriz B

B = rbind(c(2,4,-6),c(0,0,3),c(0,-2,5))

eigen (B)[1]

#Ejercicio 3 Dad, redondeando a 3 cifras decimales, los vectores propios de la matriz C

C = rbind(c(-48,35,-12),c(-134,95,-32),c(-194,133,-44))
lista_vec= c(eigen(B)[2])
lista_vec

matrizVec = lista_vec[[1]]
 
round(matrizVec,3)

#Ejercicio 4 Dad el rango de la matriz D

D = rbind(c(-2,-8,-2,3),c(-3,-6,-1,2),c(-9,-22,-3,7),c(-18,-44,-8,15))
D
qr(D)$rank 
