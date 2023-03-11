import csv
from Show import Show

def lecturaCsv():
    listaShow = []
    with open("10_Netflix.csv", encoding="utf8") as csvfile:
        next(csvfile, None)
        reader = csv.reader(csvfile)
        for row in reader:
                show = Show(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])
                listaShow.append(show)
    return listaShow