import sqlite3
from sqlite3 import Error

#Funcion para establecer conexion con la base de datos
def sql_conexion (fileName = ":memory:"):
    try:
        conn = sqlite3.connect (fileName)
        print ("Conexion realizada,", fileName)
    except Error:
        print (Error)
        conn = None
    finally:
        return conn

#Funcion para establecer cursor
def sql_cursor (conn):
    return conn.cursor()