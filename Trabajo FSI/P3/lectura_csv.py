import pandas as pd
from Show import Show
import conexion

#Lectura de datos
def lecturaCsv ():
    con = conexion.sql_conexion("netflix.db")
    df = pd.read_csv("10_Netflix.csv")
    df.fillna("No", inplace=True)
    try:
        df.to_sql("netflix", con)
        con.commit()
        print ("La tabla se ha creado y se han insertado los datos")
    except:
        print ("La tabla ya estaba creada")
    con.close()