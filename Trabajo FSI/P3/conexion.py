import sqlite3
from sqlite3 import Error

def sql_conexion (fileName = ":memory:"):
    try:
        conn = sqlite3.connect (fileName)
        print ("Conexion realizada,", fileName)
    except Error:
        print (Error)
        conn = None
    finally:
        return conn

def sql_cursor (conn):
    return conn.cursor()