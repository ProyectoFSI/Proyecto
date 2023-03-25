import Show
from Movie import *
from TV_Show import *
import csv
import pandas as pd

class Almacen:
    __listaShow = []

    def __init__ (self):
        self.fromCSV("10_Netflix.csv")

    #Metodo para dar de alta
    def altaShow (self, show):
        #Si hay un show con la misma clave se notifica
        if show in self.__listaShow:
            print ("Duplicado")
        else:
            #Si no lo hay de introduce
            self.__listaShow.append(show)
            print ("Ok")

    #Metodo para dar de baja un show
    def bajaShow (self, show):
        #Si se encuentra se elimina y se confirma
        if show in self.__listaShow:
            self.__listaShow.remove(show)
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
        listaObjetos = [show for show in self.__listaShow if show.release_year >= valor1 and show.release_year <= valor2]
        return listaObjetos

    #Metodo para extraer los elementos del archivo
    def fromCSV (self, nombreFichero):

        df = pd.read_csv("10_Netflix.csv")
        d1 = df.set_index("show_id").T.to_dict()
        for diccionario_interno in d1.items():  # recorremos los valores del principal
            if diccionario_interno[1]["type"] == "Movie":
                movie = Movie(diccionario_interno[0], diccionario_interno[1]["title"], diccionario_interno[1]["director"], diccionario_interno[1]["cast"], diccionario_interno[1]["country"], diccionario_interno[1]["date_added"], diccionario_interno[1]["release_year"], diccionario_interno[1]["rating"], diccionario_interno[1]["duration"], diccionario_interno[1]["listed_in"], diccionario_interno[1]["description"])
                self.__listaShow.append(movie)
            else:
                tv_show = TV_Show(diccionario_interno[0], diccionario_interno[1]["title"], diccionario_interno[1]["director"], diccionario_interno[1]["cast"], diccionario_interno[1]["country"], diccionario_interno[1]["date_added"], diccionario_interno[1]["release_year"], diccionario_interno[1]["rating"], diccionario_interno[1]["duration"], diccionario_interno[1]["listed_in"], diccionario_interno[1]["description"])
                self.__listaShow.append(tv_show)


    #Metodo para escribir los elementos de la lista en un archivo
    def toCSV (self, nombreFichero):
        with open(nombreFichero, mode = 'w', encoding = "utf8") as csvfile:
            for element in self.__listaShow:
                csvfile.write(element)