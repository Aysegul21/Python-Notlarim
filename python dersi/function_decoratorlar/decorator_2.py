import time

def zaman_hesaplama(fonksiyon):
    def wrapper(sayilar):
        baslama = time.time()
        sonuc = fonksiyon(sayilar)
        bitis = time.time()
        sonuc = bitis - baslama
        print("{} {:6f} saniye surdu.".format(fonksiyon.__name__ ,sonuc))

        return sonuc
    return wrapper

@zaman_hesaplama
def kareleri_hesapla(sayilar):
    sonuc = list()

    for i in sayilar:
        sonuc.append(i ** 2)

    for i in sonuc:
        print(i)
@zaman_hesaplama
def kupleri_hesapla(sayilar):
    sonuc = list()

    for i in sayilar:
        sonuc.append(i ** 3)

    for i in sonuc:
        print(i)

kareleri_hesapla(range(1000))
kupleri_hesapla(range(1000))


