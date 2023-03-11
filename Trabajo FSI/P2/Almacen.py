import Show
from Movie import *
from TV_Show import *
import csv

class Almacen:
    __listaShow = []

    def __init__ (self):
        self.fromCSV("10_Netflix.csv")

    def altaShow (self, show):
        if show._show_id in self.__listaShow:
            print ("Duplicado")
        else:
            self.__listaShow(show)
            print ("Ok")

    def bajaShow (self, key):
        if key in self.__listaShow:
            self.__listaShow.remove(key)
            print ("Ok")
        else:
            print ("No localizado")

    def listadoShow (self):
        for show in self.__listaShow:
            print (show)

    def filtradoShow (self, valor1, valor2):
        listaObjetos = [show for show in self.__listaShow if show._release_year >= valor1 or show._release_year <= valor2]
        return listaObjetos

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

    def toCSV (self, nombreFichero):
        with open(nombreFichero, mode = 'w', encoding = "utf8") as csvfile:
            for element in self.__listaShow:
                csvfile.write(element)