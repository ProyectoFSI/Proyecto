from Almacen import Almacen
from Show import Show
from TV_Show import TV_Show


almacen = Almacen ()
show1 = TV_Show ("s3408", "Stranger Things", "Duffer Brothers", "", "United States", "18/03/2023", "2017", "PG-13", "4 Seasons", "TV Mystery", "")
show2 = TV_Show ("s3408", "Stranger Things", "Duffer Brothers", "", "United States", "18/03/2023", "2017", "PG-13", "4 Seasons", "TV Mystery", "")

almacen.altaShow(show1)
almacen.altaShow(show2)

almacen.bajaShow(show1)
almacen.bajaShow(show2)

print ("Metodo Listado Show")
#almacen.listadoShow()

print ("Metodo Filtrado Show")
listaShow = almacen.filtradoShow(2015, 2016)

print (listaShow)