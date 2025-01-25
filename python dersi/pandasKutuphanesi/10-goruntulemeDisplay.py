#Kutuphaneler
import pandas as pd



#maksimum ekranda gorunen sutun sayisi guncelleme
print(pd.get_option("display.max_row"))
pd.set_option("display.max_row",10)
print(pd.get_option("display.max_row"))
seri = pd.Series(index=range(0,20))
print(seri)
#maksimum ekranda gorunen satir sayisi guncelleme
print(pd.get_option("display.max_column"))
pd.set_option("display.max_column",10)
print(pd.get_option("display.max_column"))
liste1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
liste2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
seri2 = pd.Series(index= liste1,data=liste2)
print(seri2)

#maksimum ekranda gorunen  virgulden sonraki basamak sayisi guncelleme
print(pd.get_option("display.precision"))
pd.set_option("display.precision",6)
print(pd.get_option("display.precision"))
seri3 = pd.Series(data=[3.1433371432])
print(seri3)