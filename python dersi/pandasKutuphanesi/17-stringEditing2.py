import pandas as pd

seri = pd.Series(["x y z","k l m","p r s"])
print(seri)
print(seri[1][0])
seri.str.split(" ")
print(seri[1][2])
seri.str.split(" ",expand = True,n = 0)
print(seri)

seri2 = pd.Series(["Pandas","Ogreniyorum","A","BC"])
print(seri2)

print(seri2.str.contains("P"))#P iceriyor mu
print(seri2.str.upper())#Tum harfleri buyutme