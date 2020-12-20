#Si hubiéramos empezado a contar segundos a partir de las 12 campanadas que marcan el inicio de 2018, 
#¿a qué hora de qué día de qué año llegaríamos a los 250 millones de segundos? ¡Cuidado con los años bisiestos!


  
2018 / 4 #no biciesto 365
2019 /4 #no biciesto 365

2020/4 #biciesto 366
2020/100 #biciesto 366 +Sumamos un dia mas

2021/4#no biciesto 365
2022/4#no biciesto 365
2023/4#no biciesto 365
2025/4#no biciesto 365
2026/4 #no biciesto 365

  
seg_dia = 24*60*60

stop_seg =250000000



dias = stop_seg / seg_dia # 2893.51...

anos = dias /365 # 7.92 anos


ANo_final = 2018 + ceiling(anos)

Mes_final = ceiling(12 * (anos - floor(anos)))


var_aux = (31 * (12 * (anos - floor(anos)) - floor(12 * (anos - floor(anos)))) +1) # numero de dias +1 del bisiesto

Dia_final = ceiling (var-aux)

Hora_final = floor(24 * (var_aux - floor(var_aux)))


print (paste("Día:",Dia_final," Mes:",Mes_final," Año:",ANo_final," Hora:",Hora_final))



#Cread una función que os resuelva una ecuación de primer grado (de la forma Ax+B=0). 
#Es decir, vosotros tendréis que introducir como parámetros los coeficientes (en orden) y 
#la función os tiene que devolver la solución. Por ejemplo, si la ecuación es 2x+4=0, 
#vuestra función os tendría que devolver -2.

tarea1 = function (a, b,c) {
  
  x = (c - b) / a
  print(x)
  
}
  
 tarea1 (5,3,0)
 tarea1 (7,4,18)
 tarea1 (1,1,1)
 
 
 #Dad una expresión para calcular 3e-π y a continuación, dad el resultado que habéis obtenido con R redondeado a 3 cifras decimales.
 
 #Dad el módulo del número complejo (2+3i)^2/(5+8i) redondeado a 3 cifras decimales.
 
 round (3*exp(1)-pi,3)
 
 round(Mod((2+3i)^2/(5+8i)),3)
 
 
  
  