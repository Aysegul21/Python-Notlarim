"""

class Araba():

    def __init__(self,model,renk,beygirGucu = 33,silindir= 55):
        print("yapıcı methot çağırıldı...")
        self.model = model
        self.renk = renk
        self.beygirGucu = beygirGucu
        self.silindir = silindir



araba1 = Araba("modell","sari") #Araba veri tipinden bir "araba1" isminde bir obje oluşturduk.


print(araba1.model)
print(araba1.renk)
print(araba1.beygirGucu)
print(araba1.silindir)
"""

class Calisan():
    def __init__(self,isim,maas,departman):
        self.isim = isim
        self.maas = maas
        self.departman = departman

    def bilgileriGoster(self):

        print("Calisan sinifinin bilgileri....")
        print(" Isim : {} \nMaas : {} \nDepartman : {}\n".format(self.isim,self.maas,self.departman))

    def departmanDegistir(self,yeniDepartman):
        print("Deparman degisiyor....\n")
        self.departman = yeniDepartman


class Yonetici(Calisan):
    def __init__(self,isim,maas,departman,kisiSayisi):
        print("Yonetici sinifinin init fonksiyonu")
        super().__init__(isim,maas,departman)
        self.kisiSayisi = kisiSayisi

    def bilgileriGoster(self):
        print("Yonetici sinifinin bilgileri....")
        print("İsim : {} \nMaaş: {} \nDepartman: {}\nSorumlu kişi sayısı: {}".format(self.isim,self.maas,self.departman,self.kisiSayisi))
    def zamYap(self,zamMiktari):
        print("Zam yapiliyor.....")

        self.maas += zamMiktari



yonetici1 = Yonetici("Aysegul" , 2000000,"no",5)

yonetici1.bilgileriGoster()
yonetici1.departmanDegistir("yes")
yonetici1.zamYap(232)
yonetici1.bilgileriGoster()