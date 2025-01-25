def fonksiyon(islem_adi):

    def toplama(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam

    def carpma(*args):
        carpim = 1
        for i in args:
            carpim *= i
        return carpim
    if islem_adi == "toplama":
        return toplama
    else:
        return carpma

deneme1 = fonksiyon("toplama") # toplama fonksiyonuna esit oldu
toplam = deneme1(1,2,3,4,5,6,7,8,9)

print(" deneme1 cagirildi....")
print(toplam)

deneme2 = fonksiyon("cardgv") # carpma  fonksiyonuna esit oldu
carpma = deneme2(1,2,3,4,5)

print(" deneme2 cagirildi....")
print(carpma)


def toplama2(a,b):
    return a + b
def cikarma2(a,b):
    return a-b
def carpma2(a,b):
    return a * b
def bolme2(a,b):
    return a / b


def anafonksiyon(func1,func2,func3,func4,islem_adi):
    if(islem_adi == "toplama"):
        print(func1(3,4))
    elif (islem_adi == "cikarma"):
        print(func2(10,4))
    elif (islem_adi == "carpma"):
        print(func3(10, 2))
    elif (islem_adi == "bolme"):
        print(func4(36, 4))
    else:
        print("Gecersiz islem girildi...")
print("anafonksiyon cagirildi....")
anafonksiyon(toplama2,cikarma2,carpma2,bolme2,"carpma")

