# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 09:43:22 2024

@author: ayseg
"""


##%%1.Ornek
x = int(input("x degerini giriniz:"))

if(x < 0):
    x = x+1
else:
    x = x-1
    
print(x)

print("3 sayi giriniz:")
a,b,c = eval(input())

max = a

if(max <b):
    max = b
if(max < c):
    max = c
    
print("girdiğiniz sayılardan en büyük: "+str(max))


#%% for kullanımı

yukseklik = int(input("Yüksekliği giriniz:"))
for i in range(1,yukseklik+1):
    print("*"*i)
    
for i in range(yukseklik):
    print("")
    for j in range(i+1):
        print("*",end="") 



yukseklik = int(input("Yüksekliği giriniz:"))
for i in range(yukseklik):
    print("")   
    for bosluk in range(yukseklik - i-1):
        print(" ",end="")
    for yıldız in range(2*i+1):
        print("*",end ="")

yukseklik = int(input("Yüksekliği giriniz:"))
for i in range(yukseklik):
    print("")   
    print(" "*(yukseklik - i-1) + "*"*(2*i+1),end ="")
    


#%% zip fonksiyonu

tek = [i for i in range(10) if i%2 == 1]
cift =[i for i in range(10) if i%2 == 0]

for i,j in zip(tek,cift):
    print(i,j)



#%% enumerate 

sayilar = {"a","b","c","d"}
for i,sayi in enumerate(sayilar,1):
    print(f" # {i} :{sayi}")

sayilar = [ i for i in range(10)]
print(sayilar)


