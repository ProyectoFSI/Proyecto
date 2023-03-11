import csv
import db

db.crearTabla("netflix.db")

db.insertarDatos("netflix.db")

db.consultarDatos("netflix.db")

db.maximizarDatos("netflix.db")

db.minimizarDatos("netflix.db")

db.actualizarDatos("netflix.db")