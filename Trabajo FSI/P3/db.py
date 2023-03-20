import sqlite3
from sqlite3 import Error
from conexion import *
import lectura_csv

#Funcion para crear la tabla de datos
def crearTabla (nombreDB):
    conn = sql_conexion(nombreDB)
    cursor = sql_cursor(conn)

    try:
        #En el caso de que no exista se crea
        cursor.execute("CREATE TABLE netflix (show_id text PRIMARY KEY, type text, titulo text, director text, cast text, country text, "
                       "date_added text, reselaed_year integer, calificacion text, duracion text, listed_in text, description texto)")
        conn.commit()
        print ("La tabla se ha creado")
    except sqlite3.OperationalError:
        #Si ya existe se notifica
        print ("La tabla ya existe")

    conn.close()

#Funcion para inserar datos
def insertarDatos (nombreDB):
    conn = sql_conexion(nombreDB)
    cursor = sql_cursor(conn)
    listaShow = lectura_csv.lecturaCsv()

    try:
        #Si no sucede ningun error se insertan los nuevos datos en la tabla
        for show in listaShow:
            cursor.execute("INSERT INTO netflix VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (show.show_id, show.tipo, show.title, show.director, show.cast, show.country, show.date_added,
                                                                                                show.release_year, show.rating, show.duration, show.listed_in, show.description))
            conn.commit()
        print ("Insertado con exito")
    except:
        #Si sucede algun error se notifica
        print ("Error en el INSERT INTO")

    conn.close()

#Funcion para realizar consulta
def consultarDatos (nombreDB):
    conn = sql_conexion(nombreDB)
    cursor = sql_cursor(conn)

    try:
        cursor.execute("SELECT titulo, director, reselaed_year FROM netflix WHERE titulo LIKE '%a%' AND reselaed_year BETWEEN 2015 AND 2017 AND director LIKE 'R%' ORDER BY reselaed_year")
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