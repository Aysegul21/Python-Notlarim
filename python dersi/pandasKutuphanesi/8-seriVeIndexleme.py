#Kutuphaneler
import pandas as pd

liste = [30,35,45,50,80]
idx = ["a","b","c","d","e"]
seri = pd.Series(data  = liste , index= idx)
print(seri["d"])
#loc ve iloc arasindaki fark
print(seri.loc["c"])
print(seri.iloc[2])

seri2 = seri.copy()
seri2["c"] = 15
print(seri2)

print(seri2.replace(to_replace = 35,value= 17))

print(seri2.index)

seri2.index = ["a","b","x","y","z"]
print(seri2)

seri2.rename(index = {"a":"y"},inplace = True)
print(seri2)

seri3 = pd.Series([70,140],index= ["AA","BB"])
seri2 = seri2._append(seri3)

# #boyle yazilirsa yazilar yerini sayilara birakir
#seri2 = seri2._append(seri3,ignore_index= True)
#Bunun olmamasi icin su sekilde yaizlir
#seri2 = seri2._append(seri3,ignore_index= False)
print(seri2)
del seri3["BB"]
print(seri3)
seri3.drop(["AA"],inplace=True)
print(seri3)

seri4 = pd.concat([seri,seri2],axis=0)
print(seri)
print(seri2)
print(seri4)