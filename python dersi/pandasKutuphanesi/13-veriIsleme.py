#kutuphaneler
import pandas as pd

veri = pd.DataFrame({"film":["A","B","C","B","B","A","C","A"],
                     "puan":[5,9,2,5,3,7,6,8]})

print(veri)
#film icin False puan icin True degerini secti
#inplace = True denildigi icin bu koduu isleyecek
veri.sort_values(by = ["film","puan"], ascending=[False,True],inplace= True)

print(veri)

print("************************************")
veri2 = pd.DataFrame({"x":["Elma"]*5 + ["Portakal"]*3,
                      "y":[1,5,7,3,15,6,6,1]})
print(veri2)
print("************************************")
veri2.sort_values(by="x",ascending=[False],inplace=True)
print(veri2)