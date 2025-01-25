#Kutuphaneler
import pandas as pd
import numpy as np
#4 satir 2 sutundan olusan
x = (np.random.randn(4,2)*10).round()
print(x)

veri = pd.DataFrame(x,columns =["A 1","B 1"],index = range(4))
print("********************************")
print(veri)
veri.columns.str.replace(" ","_")
print("********************************")
print(veri)

