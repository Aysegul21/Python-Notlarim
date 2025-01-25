import time

def kareleri_hesapla(sayilar):
    sonuc = list()
    baslama = time.time()

    for i in sayilar:
        sonuc.append(i ** 2)

    bitis = time.time()

    print("*************************************")
    print("Bu fonksiyon {:.6f} saniye sürdü.".format(bitis - baslama))

    for i in sonuc:
        print(i)

def kupleri_hesapla(sayilar):
    sonuc = list()
    baslama = time.time()

    for i in sayilar:
        sonuc.append(i ** 3)

    bitis = time.time()

    print("*************************************")
    print("Bu fonksiyon {:.6f} saniye sürdü.".format(bitis - baslama))

    for i in sonuc:
        print(i)

kareleri_hesapla(range(10))
kupleri_hesapla(range(10))
