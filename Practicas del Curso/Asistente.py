import speech_recognition as sr
import pyttsx3
import pywhatkit

import pandas as pd
import pyodbc


listener = sr.Recognizer()
engine = pyttsx3.init()


""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 140)     # setting up new voice rate

""" VOICE"""
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


""" TALK"""

def talk(text):
    engine.say(text)
    engine.runAndWait()


"""  DB CONNECT """
def dbConneect():
    username = 'bi_consulta'
    password = 'b1*c0nsult4'
    conn = pyodbc.connect('Driver={SQL Server};'
                        'server=172.16.99.2;'
                        'database=caixa;'
                        'uid='+username+';'
                        'pwd='+password+';'
                        'Security=False;')
    return conn



#talk("Hola soy Alexa, tu asistente virtual")
#talk("En que puedo ayudarte ?")

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening.....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
    except:
        pass
    return command



def tell_ventas_detalles():
    df = pd.read_sql_query('SELECT Pais, Cadena, SUM(ROUND(Imp_VentasUSD,0)) Importe\
                       FROM vwVentasRegionalDetalleUSD\
                        where year(Fecha) = year(GETDATE())\
                        GROUP BY Pais, Cadena\
                        ORDER BY Pais;',dbConneect())
    print(df.head())
    print(len(df))
    for i in range(len(df)):
        print(df.iloc[i])
        talk(df.iloc[i,0] + df.iloc[i,1] )
        talk(df.iloc[i,2])



def tell_cumplimiento_ventas_pais():
    talk('buscando las ventas acumuladas por pais')
    df = pd.read_sql_query('SELECT Pais, SUM(ROUND(Imp_VentasUSD,0)) Importe\
                       FROM vwVentasRegionalDetalleUSD\
                        where year(Fecha) = year(GETDATE())\
                        GROUP BY Pais\
                        ORDER BY Pais;',dbConneect())
    #print(df.head())
    #print(len(df))
    talk('a continuacion las ventas acumuladas en dólares por pais')
    for i in range(len(df)):
       # print(df.iloc[i])
        talk(df.iloc[i,0])
        talk(df.iloc[i,1])
        



def tell_cumplimiento_ventas_marcas():
    talk('buscando las ventas acumuladas por marca')
    df = pd.read_sql_query('SELECT Cadena, SUM(ROUND(Imp_VentasUSD,0)) Importe\
                       FROM vwVentasRegionalDetalleUSD\
                        where year(Fecha) = year(GETDATE())\
                        GROUP BY Cadena\
                        ORDER BY Cadena;',dbConneect())
    talk('a continuacion las ventas acumuladas en dólares por marca')
    for i in range(len(df)):
        #print(df.iloc[i])
        #talk(df.iloc[i,0])
        if df.iloc[i,0] == 'Bershka':
            talk('Berchka')
        elif  df.iloc[i,0] == 'Massimo':
            talk('másimo duti')
        elif  df.iloc[i,0] == 'Oysho':
            talk('oícho')
        elif  df.iloc[i,0] == 'Pull&bear':
            talk('pul an ber')
        elif  df.iloc[i,0] == 'Stradivarius' :
            talk('estradivarius')
        elif  df.iloc[i,0] == 'Zara' :
            talk('sara')
        elif  df.iloc[i,0] == 'Zara Home':
            talk('sara jom')
        talk(df.iloc[i,1])
       


def run_alexa():
    command = take_command()
    
    if 'stop' in command:
            talk('hasta luego corazón de melón... un placer ayudarte')
            return (False)
   
    if 'alexa' in command:
        talk('enseguida te ayudo')
        command = command.replace('alexa','')
        if 'play' in command:
            song = command.replace('play','')
            talk('playing'+ song)
            pywhatkit.playonyt(song)
        elif 'ventas' in command and 'detalle' not in command:
            tell_cumplimiento_ventas_pais()
            tell_cumplimiento_ventas_marcas()
        elif 'ventas detalle' in command:
            tell_ventas_detalles()
        else:
            talk('por favor inténtalo de nuevo')

    return True
    



while True:

    if run_alexa():
        pass
    else:
        break


