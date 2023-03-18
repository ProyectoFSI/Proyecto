import Show
from Movie import *
from TV_Show import *
import csv

class Almacen:
    __listaShow = []

    def __init__ (self):
        self.fromCSV("10_Netflix.csv")

    #Metodo para dar de alta
    def altaShow (self, show):
        #Si hay un show con la misma clave se notifica
        if show._show_id in self.__listaShow:
            print ("Duplicado")
        else:
            #Si no lo hay de introduce
            self.__listaShow(show)
            print ("Ok")

    #Metodo para dar de baja un show
    def bajaShow (self, key):
        #Si se encuentra se elimina y se confirma
        if key in self.__listaShow:
            self.__listaShow.remove(key)
            print ("Ok")
        else:
            #En caso contraro se avisa de que no fue encontrado
            print ("No localizado")

    #Metodo para mostrar los elementos de la lista
    def listadoShow (self):
        for show in self.__listaShow:
            print (show)

    #Metodo para buscar shows especificos segun el año de lanzamiento
    def filtradoShow (self, valor1, valor2):
        listaObjetos = [show for show in self.__listaShow if show._release_year >= valor1 or show._release_year <= valor2]
        return listaObjetos

    #Metodo para extraer los elementos del archivo
    def fromCSV (self, nombreFichero):
        with open(nombreFichero, encoding="utf8") as csvfile:
            next(csvfile, None)
            reader = csv.reader(csvfile)
            for row in reader:
                if row[1] == "Movie":
                    movie = Movie (row[0], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])
                    self.__listaShow.append(movie)
                else:
                    tv_show = TV_Show (row[0], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])
                    self.__listaShow.append(tv_show)

    #Metodo para escribir los elementos de la lista en un archivo
    def toCSV (self, nombreFichero):
        with open(nombreFichero, mode = 'w', encoding = "utf8") as csvfile:
            for element in self.__listaShow:
                csvfile.write(element)