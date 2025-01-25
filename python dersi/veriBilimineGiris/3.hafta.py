import numpy as np

#%%Cok Boyutlu Diziler
def tanımmla(mesafeler):
    for satir in range(len(mesafeler)):
        for sutun in range(len(mesafeler[satir])):
            if mesafeler[satir][sutun]<10:
                print(mesafeler[satir][sutun],end="    ")
            elif mesafeler[satir][sutun]>1000:
                print(mesafeler[satir][sutun],end=" ")
            elif mesafeler[satir][sutun]>100:
                print(mesafeler[satir][sutun],end="  ")
        print()
    print("**************************************************************")

def diziyeCevirme(liste):
    dizi = np.array(mesafeler)
    print(dizi)
    return dizi
def diziyiGeriCevir(dizi):
    dizigeri = dizi.tolist()
    print(dizigeri)
    return dizigeri
def diziElemanToplami(dizi):
    print("Toplam:",dizi.sum())
    print("axis=0",dizi.sum(axis=0))
    print("axis=1",dizi.sum(axis=1))

def enKucukElemanBul(dizi):
    print("KucukElemanBul:",dizi.min())
def enBuyukElemanBul(dizi):
    print("BuyukElemanBul:",dizi.max())
#mesafeler = [[0,1,2,3,4,5],[0,0,0,0,0,0]]
mesafeler=[[0,1,2,3,4,5,6],[1,0,872,1,2,3,4],[2,872,0,1,1234,2,3],[3,1,1,0,1,2,3],[4,2,1234,1,0,1,2],[5,3,2,2,1,0,1779],[6,4,3,3,2,1779,0]]
tanımmla(mesafeler)

print(mesafeler)
dizi=diziyeCevirme(mesafeler)
diziElemanToplami(dizi)
enKucukElemanBul(dizi)
enBuyukElemanBul(dizi)
diziGeri = diziyiGeriCevir(dizi)

#%%Numpy Array vs. Python List

a = [1,2,3]
print([q*2 for q in a])

a = np.array([1,2,3])
print(a*2)


a = [1,2,3]
b = [4,5,6]
toplam = [q+r for q,r in zip(a,b)]
print(toplam)

a = np.array([1,2,3])
b = np.array([4,5,6])
toplam = a+b
print(toplam)

#&&array-zeros zeros_like
a = np.array([1.,2.,3.])
print(a)
print(a.dtype)
print(a.shape)

b = np.zeros(3,int)#int türünde 3 adet sıfır üretimi sağlar.
print(b)

c = np.zeros_like(a)# anın matrisi büyüklüğündeki bir matrisi 0 ile doldurur.
print(c)
print(c.dtype)

d = np.ones(3)
print(d)

e = np.empty(3)
print(e)

f = np.full((2,2), 7)# 2x2 lik bir matrisi 7 sayısı ile doldurur.
print(f)

#%%Linspace Logspace

a = np.linspace(0,13,5) #(başlangıç, bitiş, değersayısı)
#0 ve 13 dahil 5 sayı üretir
print(a)

b = np.logspace(0,3,5)
#10^0 ve 10^3 e kadar 5 sayı üretir
print(b)

#%%Arange
#arange ile linspace arasındaki fark arange son elemandan öncesini yazdırır.
#linspace son elemanı da ele alır.
#np.arange(start,stop,step)
a = np.arange(6)# sadece stop değerini girersek o değere kadar olanı yazar
print(a)

b = np.arange(2,6)
#start,stop değerini tek girersek ardışık ikisi arasındaki sayıları yazar
print(b)

c = np.arange(1,6,2)
print(c)

#%%Random

a = np.random.randint(0,10,3)#int sayılar üretir
print(a)

b = np.random.rand(3)#üretilen sayılar [0,1] arsında olur.
print(b)

c = np.random.uniform(1,10,3)#üretilen sayılar [0,10] arasında devirli sayılar oluşur.
print(c)

d= np.random.normal(5,2,3)
print(d)

#%%indexleme

a = np.array([1,2,3,4,5,6,77,8,9,10])
print(np.any(a>5))#Dizide 5 ten büyük eleman var ise True değilse False döndürür.

print(a[a>5])#dizideki 5 ten büyük elemanları listeler

print(np.all(a>5))#Dizide tüm elemanlar 5 ten büyük ise True değilse False döndürür.

print(np.where(a>5))

print(np.nonzero(a>5))#Dizide 5 ten büyük olanalrın indexlerini verir.

#%%Reshape Ravel
d1 = np.arange(24)
d2 = d1.reshape((2, 12))
d3 = np.array([2,3,4]) 
print(d3)
d3_sutun = d3[:, np.newaxis]
print(d3_sutun)
d3_T = d3_sutun.T
print(d3_T)


