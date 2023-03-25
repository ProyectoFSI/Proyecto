import sqlite3
from sqlite3 import Error
from conexion import *
import lectura_csv

#Funcion para inserar datos
def insertarDatos (nombreDB):
    lectura_csv.lecturaCsv()

#Funcion para realizar consulta
def consultarDatos (nombreDB):
    conn = sql_conexion(nombreDB)
    cursor = sql_cursor(conn)

    try:
        cursor.execute("SELECT title, director, release_year FROM netflix WHERE title LIKE '%a%' AND release_year BETWEEN 2015 AND 2017 AND director LIKE 'R%' ORDER BY release_year")
        rows = cursor.fetchall()
        for row in rows:
            print (row)
    except:
        print ("Error en el SELECT WHERE")

#Funcion para actualizar datos de la tabla
def actualizarDatos (nombreDB):
    conn = sql_conexion(nombreDB)
    cursor = sql_cursor(conn)

    try:
        cursor.execute("UPDATE netflix SET country = 'Indeterminado' WHERE country IS ''")
        conn.commit()
    except:
        print ("Error en el UPDATE")

#Funcion para mostrar el pais con mas peliculas
def maximizarDatos (nombreDB):
    conn = sql_conexion(nombreDB)
    cursor = sql_cursor(conn)

    try:
        cursor.execute ("SELECT country, MAX(Count) AS MaxCount FROM ( SELECT country, COUNT(*) AS Count FROM netflix GROUP BY country) AS MaxPelis")
        rows = cursor.fetchall()
        for row in rows:
            print (row)
    except:
        print ("Error en la sentencia")

#Funcion para mostrar el pais con menos peliculas
def minimizarDatos(nombreDB):
    conn = sql_conexion(nombreDB)
    cursor = sql_cursor(conn)

    try:
        cursor.execute ("SELECT country, MIN(Count) AS MaxCount FROM ( SELECT country, COUNT(*) AS Count FROM netflix GROUP BY country) AS MinPelis")
        rows = cursor.fetchall()
        for row in rows:
            print (row)
    except:
        print ("Error en la sentencia")