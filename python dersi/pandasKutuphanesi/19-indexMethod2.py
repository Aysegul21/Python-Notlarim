#Kutuphaneler
import pandas as pd
import numpy as np

print(np.arange(4)[::-1])

seri = pd.Series(np.arange(10),index=np.arange(10)[::-1])
print(seri)
print("***************************************")
print(seri.isin([3]))
print("***************************************")
print(seri.isin([3,2,8,7,6]))
print("***************************************")
print(seri[seri.isin([3,2,8,7,6])])

seri2 = pd.Series(np.arange(10),index=pd.MultiIndex.from_product([["A","B"],["a","b","c","d","e"]]))
print(seri2)

print("**************************************")
print(seri2.iloc[seri2.index.isin([("A","c"),("B","c")])])
