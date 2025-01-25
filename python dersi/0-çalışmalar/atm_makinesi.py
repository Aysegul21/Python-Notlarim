print("1-Bakiye sorgulama")
print("2-Para yatirma")
print("3-Para cekme")
print("Programdan cikmak icin 'q' ya basiniz..")
para = 1000
secim =input("seciminizi giriniz:")

while True:
    if (secim == "q"):
        print("yine bekleriz..")
        break
    elif (secim == "1"):
        print("{} TL bakiyeniz bulunmaktadır.".format(para))
    elif (secim == "2"):
        yatirilacak=int(input("Yatiracaginiz miktari giriniz:"))
        para +=yatirilacak
        print("Hesabinizda {} TL para bulunmaktadir.".format(para))
    elif (secim == "3"):
        cekilecek = int(input("Cekilecek para miktarini giriniz:"))
        para -= cekilecek
        print("Hesabinizda {} TL para bulunmaktadir.".format(para))
    secim = input("seciminizi giriniz:")
