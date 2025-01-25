#Kutuphaneler

import pandas as pd

#data = pd.read_csv("titanic.csv")
liste = ["Aysegul","Fatma","Meryem","Zeynep","Eda","Sedef","Mehmet"]
liste2 = ["SADE","ACIK","DEFSE","DEMIR","KAGAN","TERA","YARDA"]
data = pd.DataFrame({"AD":liste,"SOYAD":liste2})
print(data)
+# print("***********************")
# print(data.head())#ilk 5 veriyi ceker
# print("***********************")
# print(data.info())#tum sutun bilgilerini verir( bazi sutunlarda kac tane eleman oldugunu gosterir)
# print("***********************")
# print(data.columns)#hangi sutunlar oldugunu gpsterir
# print("***********************")
# print(data.index)# kac tane satir oldugunu gosterir
# print("***********************")
# print(data.values)#data nin degerini verir
# print("***********************")
# print(data.dtypes)#data tiplerini gosterir