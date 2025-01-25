#Kutuphaneler

import pandas as pd

veri = pd.read_csv("titanic.csv")
print(veri)
veri2 = veri.pivot_table(index="Pclass",columns="Sex",values="Age")
print(veri2)