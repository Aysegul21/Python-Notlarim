import sqlite3

import time

class Kitap():

    def __init__(self,isim,yazar,yayin_evi,tur,baski):

        self.isim= isim
        self.yazar = yazar
        self.yayin_evi = yayin_evi
        self.tur = tur
        self.baski = baski


    def __str__(self):

        return "Kitap Ismi: {}\nYazar: {}\nYayin evi: {}\nTur: {}\nBaski:{}".format(self.isim,self.yazar,self.yayin_evi,self.tur,self.baski)

class Kutuphane():

    def __init_(self):

        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.baglanti =sqlite3.connect("kutuphane.db")

        self.cursor = self.baglanti.cursor()

        sorgu = "Create Table If not exists kitaplar (isim TEXT,yazar TEXT,yayin_evi TEXT,tur TEXT,baski INt)"

        self.cursor.execute(sorgu)

        self.baglanti.commit()#bu islemin veri tabani uzerinde etkili olmasi icin bunu yazmaliyiz

    def baglantiyi_kes(self):
        self.baglanti.close()

    def kitaplari_goster(self):

        sorgu = "Select * From kitaplar"

        self.cursor.execute(sorgu) #Bu sorgu çalistigi zaman veri tabani doner

        kitaplar = self.cursor.fetcall()

        if (len(kitaplar) == 0):
            print("Hicbir kitap bulunmamaktadir.")

        else:
             for i in kitaplar:

                 kitap = Kitap(i[0],i[1],i[2],i[3],i[4])
                 print(kitap)

    def kitap_sorgula(self,isim):

        sorgu = "Select * From kitaplar where isim = ?"

        self.cursor.execute(sorgu(isim,))

        kitaplar = self.cursor.fetchall()

        if(len(kitaplar) == 0):
            print("Boyle bir kitap bulunmuyor.......")
        else:
            kitap = Kitap(kitaplar[0][0],kitaplar[0][1],kitaplar[0][2],kitaplar[0][3],kitaplar[0][4])

            print(kitap)


    def kitap_ekle(self,kitap):
        sorgu = "Insert into kitaplar Values(?,?,?,?,?)"
        self.cursor.execute(sorgu,(kitap.isim,kitap.yazar,kitap.yayınevi,kitap.tür,kitap.baskı))

        self.baglanti.commit()#bunun yapmazsak veritabani guncellenmez

    def kitap_sil(self,isim):

        sorgu = "Delete From kitaplar where isim = ?"

        self.cursor.execute(sorgu,(isim,))

        self.baglanti.commit()#bunu yapinca kitap silinmis oluyor.

    def baski_yukselt(self,isim):

        sorgu = "Select * From kitaplar where isim = ?"

        self.cursor.execute(sorgu,(isim,))


        kitaplar = self.cursor.fetchall()

        if(len(kitaplar) == 0):
            print("Boyle bir kitap bulunmuyor.......")
        else:
            baski = kitaplar[0][4]
            baski += 1

            sorgu2 = "Update kitaplar set baski = ? where isim = ?"

            self.cursor.execute(sorgu2,(baski,isim))

            self.baglanti.commmit()




