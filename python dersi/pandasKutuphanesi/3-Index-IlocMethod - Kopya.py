import pandas as pd


veri_1 = {"Isim":["Ahmet","Ayse","Mehmet"],"Boy":[175,180,190],"Maas":[10000,20000,30000]}
veri = pd.DataFrame(veri_1)
print(veri)
Ahmet = veri.iloc[0]
Ayse = veri.iloc[1]
Mehmet = veri.iloc[2]

print("\n********Ahmet'in Verileri********")
print(Ahmet)

print("\n*********Sadece 0 ve 1. indexlerin verileri*******")
veri2 = veri.iloc[0:2]
print(veri2)
