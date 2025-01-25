#kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

veriler = pd.read_csv("eksikVeriler.csv")

print(veriler)

boy = veriler[["boy"]]
print(boy)

boykilo = veriler[["boy","kilo"]]
print(boykilo)
"""
#Yas verilerindeki eksik değerlere 0 degerini atar
veriler["yas"] = veriler["yas"].fillna(0)
yas = veriler[["yas"]]
print(yas)
"""

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values = np.nan , strategy='mean')

yas = veriler.iloc[:,3:4].values
print(yas)
print("***********************************")
imputer = imputer.fit(yas)#makine ogrenmesinin ogrendigi surec
yas = imputer.transform(yas)#makine ogrenmesinin uygulandigi surec
print(yas)
