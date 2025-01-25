#Kutuphaneler
import pandas as pd

veri1 = {"AD":["Ahmet","Ayse","Bartu","Cagla","Seda"],"SOYAD":["ALTIN","GUMUS","PARA","ZENGİN","VARDAR"]}
veri = pd.DataFrame(veri1)

print("******Veriler**********")
print(veri)

veri = veri.set_index("AD")
print(veri.loc["Ahmet"])

print("**********************Titanic Verileri****************************")

data = pd.read_csv("titanic.csv")
print(data.iloc[0:10,0:3])#ilk 10 satir ve ilk 3 sutunun verilerini gosterir
