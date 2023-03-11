import csv


# Lectura del CSV
def lecturaCsv():
    with open('10_Netflix.csv', encoding="utf8") as csvfile:
        diccionario = {}
        next(csvfile, None)
        reader = csv.reader(csvfile)
        for row in reader:
            diccionario[row[0]] = tuple(row[1:])
    return diccionario

# Función Opción 1:
def agregarRegistro(diccionario):
    clave = input("Introduzca registro a añadir: ")
    enElDiccionario = False
    while enElDiccionario == False:
        if clave in diccionario:
            clave = input("Introduzca una clave válida: ")
        else:
            tipo = input("Introduzca el tipo: ")
            director = input("Introduzca director: ")
            cast = input ("Introduzca elenco: ")
            pais = input ("Introduzca el país: ")
            fechaAnyadida = input("Introduzca la fecha (Formato dd/mm/yyyy): ")
            anyoEstreno = input ("Introduzca el año de estreno: ")
            clasificacion = input("Introduzca la calificación: ")
            duracion = input ("Introduzca la duración (en minutos): ")
            incluidoEn = input ("Introduzca las categorias: ")
            descripcion = input ("Introduzca la descripción: ")
            registro = (tipo, director, cast, pais, fechaAnyadida, anyoEstreno, clasificacion, duracion, incluidoEn, descripcion)
            diccionario [clave] = registro
            print ("Registro añadido correctamente")
            enElDiccionario = True


# Función Opción 2:
def buscarRegistro(diccionario):
    clave = input("Introduzca la clave del registro: ")
    try:
        print("show id: ", clave)
        for fila1, filaBuscada in zip(diccionario["show_id"], diccionario[clave]):
            print("{}: {}".format(fila1, filaBuscada))
    except:
        print ("No existe un registro con esa clave")


# Función Opción 3:
def eliminarRegistro(diccionario):
    clave = input("Introduzca la clave del registro: ")
    longitud = len(diccionario)
    diccionario.pop(clave)
    if (longitud == len(diccionario)):
        print("No se ha podido eliminar el registro")
    else:
        print("Se ha eliminado el registro")


# Función Opción 4
def listarRegistros(diccionario):
    for valor in diccionario:
        print(valor, diccionario[valor])

if __name__ == '__main__':
    opcion = -1
    diccionario = lecturaCsv()
    while opcion != 5:
        print(
            "\nMenu: \n\t1. Agregar un nuevo registro \n\t2. Buscar un registro por su clave y mostrar sus valores \n\t3. Borrar un registro a partir de su clase "
            "\n\t4. Listar todos los registros en formato de tabla \n\t5. Salir")
        opcion = int(input("\nIntroduzca la opcion a realizar: "))

        if opcion == 1:
            agregarRegistro(diccionario)
        elif opcion == 2:
            buscarRegistro(diccionario)
        elif opcion == 3:
            eliminarRegistro(diccionario)
        elif opcion == 4:
            listarRegistros(diccionario)
