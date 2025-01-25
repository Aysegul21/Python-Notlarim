#Kutuphaneler 1
import pandas as pd

veri = {"Meslek":["Muhendis","Doktor","Tekniker"],"Maas":[10000,20000,30000]}

veri1 =pd.DataFrame(veri)#veri tablo haline getirildi

print("\n*******Veri bilgileri**************")
print(veri1.info())

print("\n*******Maas bilgileri**************")
print(veri1["Maas"])

print("\n********Titanic Verileri*************")
data = pd.read_csv("titanic.csv")
print(data)

print("\n********Titanic ilk 5 yas bilgileri********")
yas = data["Age"]
#print(yas.head())#birinci gosterim
print(yas[0:5])#ikinci gosterim

print(yas.values[:10])
print("\n************Verileri cinsiyete göre incele**********")
data = data.set_index("Sex")
print(data)

print("\n*************Verileri yasa gore incele***************")
data = data.set_index("Age")
print(data)
print("\n*************Verileri yasa gore incele***************")
data = data.set_index("Name")#index degeri tek girdi olarak girilebilir
print(data)

print("\n*************Verileri Fare kismini incele***************")
print(data["Fare"][:5])