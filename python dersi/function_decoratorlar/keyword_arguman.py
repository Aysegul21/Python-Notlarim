def fonksiyon1(**kwargs): # sozluk olusturma
    print("FONKSIYON 1")
    print(kwargs)

fonksiyon1(isim = "Aysegul", soyad = "TEKES",numara = 220303060)


def fonksiyon2(**kwargs):
    print("FONKSIYON 2",end = "")
    for i,j in kwargs.items():
        print("")
        print("Argüman İsmi:",i,"Argüman Değeri:", j,end = " ")

print("\n")
fonksiyon2(isim = "Aysegul", soyad = "TEKES",numara = 220303060)


def fonksiyon3(*args,**kwargs):
    print("FONKSIYON 3")
    sayac = 0
    for i in args:
        sayac += 1
        print("{:2}.arguman: {:2}".format(sayac,i))

    for i,j in kwargs.items():
        print("Arguman ismi:",i,"Arguman degeri:",j)

print("\n")
fonksiyon3(1,3,5,2,4,7,8,6,0,9 ,isim = "Aysegul", soyisim = "TEKES",numara = 220303060)

