"""
4. Elmas DataFrame'in yeni bir 'Kalite -renk' Serisini
(Seri adını tanımlamak için köşeli parantez gösterimini kullanın)
oluşturmak için bir Pandas programı yazın.
"""
import pandas as pd

veri = pd.read_csv("diamonds.csv")
print(veri)
veri["kalite-renk"] = veri["cut"] + "," + veri["color"]
print("*******************************************")
print(veri)