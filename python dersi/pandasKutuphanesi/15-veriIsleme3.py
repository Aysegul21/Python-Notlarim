#Kutuphaneler
import numpy as np
import pandas as pd

x = (np.random.rand(10)*10).round()
y = (np.random.rand(10)*10).round()

veri = pd.DataFrame({"veri1":x,
                     "veri2":y})
print(veri)
print("*************************")
veri3 = veri.assign(toplam=veri["veri1"]*veri["veri2"])
print(veri3)

veri3 = pd.DataFrame([range(5),[3,7,np.nan,8,10],[2,15,17,np.nan,12],range(5)])

print("****************************************")
print(veri3)
print("****************************************")
print(veri3.isnull())
print("****************************************")
print(veri3.isnull().any())

#NAN yerine silindi yazisi ekleme
print(veri3.fillna("silindi"))
