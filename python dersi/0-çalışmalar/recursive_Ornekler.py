# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 01:53:30 2024

@author: ayseg
"""


#%%Soru 1.
"""
Bir dizi verildiğinde, orijinal dizide bitişik olan
aynı karakterlerin birbirlerinden bir "*" ile ayrıldığı 
yeni bir diziyi yinelemeli olarak hesaplayan kodu yazınız.
"""
def yildizBirlesitr(kelime,index = 0):
    dizi = list()
    if(kelime[index] == None):
        dizi.append(kelime[index])
        return dizi
    
    if(kelime[index-1] == kelime[index]):
        dizi.append(kelime[index])
        dizi.append("*")
    index += 1
    return yildizBirlesitr(kelime,index)


a = yildizBirlesitr("h",0)
print(a)