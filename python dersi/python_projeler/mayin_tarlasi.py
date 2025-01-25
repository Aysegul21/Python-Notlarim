import random

def ekrana_bastir(liste1,sayi,secilen1,secilen2,liste2):
    sayi2 = (sayi * sayi)
    j = 0
    k = -1
    for i in range(0,sayi2):

        if (i % sayi == 0):
            k += 1
            j = 0
        if (secilen1 == k and secilen2 == j):
            secilen = liste1[i]
        j += 1
    for i in range(0,sayi2):
        if(liste1[i] == secilen):
            liste2[i] = secilen

    for i in range(0,sayi2):
        if (i != 0 and i % sayi == 0):
            print("|\n-----------------")
        print("|{:2} ".format(liste2[i]),end = "")
    print("|",end = "")

    if(secilen == -1):
        print("\nKAYBETTINIZ..",end ="")
        return "."
    else:
        while(secilen != -1):
            secilen1 = int(input("\n1- lutfen acilmasini iistediginiz konumun i degerini giriniz "))
            secilen2 = int(input("2- lutfen acilmasini iistediginiz konumun j degerini giriniz "))
            return ekrana_bastir(liste1, sayi, secilen1, secilen2,liste2)

def oyun_yer(sayi,secilen1,secilen2):
    sayi2 = (sayi * sayi)
    liste1 = list()
    ustdeger = (sayi2 // sayi) + 1
    for i in range(0,sayi2):
        liste1.append(random.randint(1,ustdeger))

    for j in range(0,4):
        liste1[random.randint(0,15)] = -1
    for i in range(0,sayi2):
        liste2 = ["X"] * sayi2
    print(ekrana_bastir(liste1,sayi,secilen1,secilen2,liste2))


print("MAYIN TARLASI OYUNUNA HOSGELDINIZ...")
cevap = input("oyunu oynamak ister misiniz?(evet/hayir):")
sayi = int(input("oyun kac carpi kaclik olsun(ornek: 4X4 luk icin 4 girilecek):"))

while(cevap == "evet" ):
    secilen1 = int(input("1- lutfen acilmasini iistediginiz konumun i degerini giriniz(ornek: 4X4 luk icin 0,1,2,3 degerleri girilebilir):"))
    secilen2 = int(input("2- lutfen acilmasini iistediginiz konumun j degerini giriniz(ornek: 4X4 luk icin 0,1,2,3 degerleri girilebilir):"))
    oyun_yer(sayi,secilen1,secilen2)
    cevap = input("\nTekrar oynamak ister misiniz?")




