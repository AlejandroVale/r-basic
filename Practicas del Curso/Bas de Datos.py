import pandas as pd
import pyodbc


username = 'bi_consulta'
password = 'b1*c0nsult4'

# Driver={SQL Server}
#ODBC Driver 11 for SQL Server
conn = pyodbc.connect('Driver={SQL Server};'
                        'server=172.16.99.2;'
                        'database=caixa;'
                        'uid='+username+';'
                        'pwd='+password+';'
                        'Security=False;')

#cursor = conn.cursor()

df = pd.read_sql_query('SELECT Pais, Cadena, SUM(Uni_Ventas) Unidades , SUM(ROUND(Imp_VentasUSD,0)) Importe\
                       FROM vwVentasRegionalDetalleUSD\
                        where year(Fecha) = year(GETDATE())\
                        GROUP BY Pais, Cadena\
                        ORDER BY Pais;',conn)


    

print(df.head())