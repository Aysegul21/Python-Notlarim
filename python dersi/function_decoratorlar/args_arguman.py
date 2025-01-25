def fonksiyon1(*args):  #istedigimiz sayida arguman gonderebiliyoruz

    print("Gonderilen sayilar:",args)
    sayac = 0

    for i in args:
        sayac += 1
        print("{}. sayi: {}".format(sayac,i))

fonksiyon1(1,2,3)


def fonksiyon2(isim,*args):
    print("Isim:",isim)
    for i in args:
        print(i,end = "")

fonksiyon2("Aysegul TEKES",2,2,0,3,0,3,0,6,0)