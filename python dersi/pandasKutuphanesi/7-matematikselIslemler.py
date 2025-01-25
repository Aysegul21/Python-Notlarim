#Kutuphaneler
import pandas as pd

veri = pd.DataFrame([[5,3,2],[7,2,9]], index= ["1.satir","2.satir"],columns=["1.sutun","2.sutun","3.sutun"])

print("Veriler")
print(veri)
print("sutunlardaki sayi toplamlari")
print(veri.sum())

print("satirlardaki sayi toplamlari")
print(veri.sum(axis = 1))
print("sutunlardaki en buyuk sayilar")
print(veri.max())