import csv
import db
#Se insertan los datos
db.insertarDatos("netflix.db")
#Se realiza una consulta
db.consultarDatos("netflix.db")
#Muestra el pais con mas peliculas
db.maximizarDatos("netflix.db")
#Muestra el pais con menos peliculas
db.minimizarDatos("netflix.db")
#Actualiza los datos
db.actualizarDatos("netflix.db")