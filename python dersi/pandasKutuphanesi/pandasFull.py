# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 15:52:54 2024

@author: ayseg
""" 

import pandas as pd
#%%Dosya bilgilerini verir

idx = [1,3,4,2]
price = [10,20,15,15]
weight = [100,314,213,432]
data = pd.DataFrame({"id":idx,"price":price,"weight":weight})

print(data)
data.sort_values(["price","weight"])
#%%index değiştirme
data.set_index("id")
data.reset_index()
#%%loc
#data.loc[data.id == 213 , "weight"].item()
d