import pandas as pd

pdf=pd.read_csv("10_Netflix.csv")

print(pdf[pdf.release_year>=2017])