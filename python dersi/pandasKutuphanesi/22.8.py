"""
11. Elmas veri çerçevesinden birden fazla satırı (eksen=0, satırları belirtir)
aynı anda kaldırmak için bir Pandas programı yazın.

"""
import pandas as pd

veri = pd.read_csv("diamonds.csv")
print(veri.head())
print("*************************************")
veri.drop(veri.index[0],axis=0,inplace=True)


print(veri.head())

