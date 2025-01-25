# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 09:36:09 2024

@author: ayseg
"""

#%%Pandas

import pandas as pd
import numpy as np

d = {"a":"1","b":"2","c":"3"}
seri = pd.Series(data = d)

veri = np.genfromtxt("example_data.csv", delimiter=";", names=True, dtype=None, encoding="UTF")

data = pd.Series([11,22,33,44,55,66])

print(data)
print(data.values)
print(data.index)

print(data[1:3])

notData = pd.Series([80,100,40,60],
                    index =["Ali","Veli","Ayşe","Esra"])

print(notData["Ali"])

quiz1 = {"Eslem":65,"Mert":80,"Ezgi:":45,"Nursena":20,
         "Yusuf":30,"Atakan":75,"Ahmet":100}


seriQuiz1 = pd.Series(quiz1)

dfQuiz1 = pd.DataFrame(seriQuiz1,columns=["Not"])
dfQuiz1.index = dfQuiz1.index.set_names(["Öğrenci"])

print(dfQuiz1.index)
print(dfQuiz1.columns)



rassalDizi = pd.DataFrame(np.random.rand(4,2),
             columns = ["Sayı1","Sayı2"],
             index = ["a","b","c","d",])


for item,item2 in seriQuiz1:
    print(item,item2)


