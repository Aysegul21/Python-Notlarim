#Kutuphaneler 1
import pandas as pd

data = pd.read_csv("titanic.csv")
data = data.set_index("Name")
print(data.loc["Heikkinen, Miss. Laina"])

print("\n********Sadece kadinlari yazdirmak************")
print(data[data["Sex"] == "female"])#1.yol
print("\n**********************************************")
print((data.set_index("Sex")).loc["female"])#2.yol

print("\n********Yasi 30 dan kucuk olanlar*************")
print(data[data["Age"]<30])

print("\n*************Erkeklerin yas ortalamsi*********")
print(data.loc[data["Sex"] == "male","Age"].mean())#Erkeklerin yas ortalamasi
print("\n*************Kadinlarin yas ortalamsi*********")
print(data.loc[data["Sex"] == "female","Age"].mean())#Kadinlarin yas ortalamasi

print("\n************Yasi 50 den buyuk olanlarin sayisi")
print((data["Age"]>50).sum())