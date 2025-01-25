import sqlite3

con = sqlite3.connect("kutuphane.db")

cursor = con.cursor()

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık(isim TEXT,yazar TEXT,sayfa_sayisi INT)")
    con.commit()

def veri_ekle():
    cursor.execute("INSERT INTO kitaplık ValUES ('Istanbul Hatırası','Ahmet Umit',561)")
    con.commit() #veri tabanini guncellemek istedigimizi bildiriyoruz.

def veri_ekle2(isim,yazar,sayfa_sayisi):
    cursor.execute("INSERT INTO kitaplık VALUES(?,?,?)",(isim,yazar,sayfa_sayisi))


#Select * From kitaplık : Tablodaki tüm bilgileri almamızı sağlar.
def verileri_al():
    cursor.execute("Select * From kitaplık")
    liste = cursor.fetchall()#cursor.execute("Select * From kitaplık") 'da aldigimiz tum verileri bize doner.
    sira_no = 1
    print("         Kitap_adi                          yazar            Sayfa_sayisi")

    for i,j,k in liste:
        print("kitap{} = {:30} {:20}{:4}".format(sira_no,i,j,k))
        sira_no += 1

#Select isim,yazar From kitaplık : Tablodaki bilgilerden sadece isim ve yazar özelliklerini almamizi saglar.
def verileri_al2():
    cursor.execute("Select isim,yazar from kitaplık")
    liste = cursor.fetchall()

    sira_no = 1
    print("         Kitap_adi                          yazar")

    for i,j in liste:
        print("kitap{} = {:30} {:20}".format(sira_no,i,j))
        sira_no += 1

#Select*From kitaplık where sayfa_sayisi = 184 : Sadece sayfa_sayisi ozelligi 184 olanlarii alir
def verileri_al3(sayfa_sayisi):
    cursor.execute("Select * from kitaplık where sayfa_sayisi = ?",(sayfa_sayisi,))
    liste = cursor.fetchall()

    sira_no = 1
    print("         Kitap_adi                          yazar            sayfa sayisi")
    for i,j,k in liste:
        print("kitap{} = {:30} {:20}{:4}".format(sira_no,i,j,k))
        sira_no += 1

"""
Tablodaki Verileri Guncelleme ve sime
Guncelleme
Update kitaplık set sayfa_sayisi = 184 where sayfa_sayisi = 76 -> sayfa sayisi 76 olan kitaplari 184 olarak degistirir
"""
def verileri_guncelle(eski_sayfa_sayisi,yeni_sayfa_sayisi):
    cursor.execute("Update kitaplık set sayfa_sayisi = ? where sayfa_sayisi = ?",(yeni_sayfa_sayisi,eski_sayfa_sayisi))


"""
Verileri Silme
Delete From kitaplik where yazar = "stefen zweig" -> yazar ozelligi stefen zweig olan kitaplari tablodan siler
"""
def verileri_sil(yazar_adi):
    cursor.execute("Delete From kitaplik where yazar = ?",(yazar_adi,))
    con.commit()


yazar_ad = input("Tablodan silinmesini istediginiz yazarin adini giriniz:")
verileri_sil(yazar_ad)

"""
eski_sayfa_sayi = int(input("eski sayfa sayisini giriniz: "))
yeni_sayfa_sayi = int(input("yeni sayfa sayisini giriniz:"))
verileri_guncelle(eski_sayfa_sayi,yeni_sayfa_sayi)#sayfa sayisini gunceller
verileri_al()#guncelledigimiz yeni verileri ekrana yazdirir
"""

"""
sayfa_sayi = int(input("Sayfa sayisini giriniz:"))
verileri_al3(sayfa_sayi) #sadece sayfa_sayisi sayfa_sayi olanlari yazdirir
"""

#verileri_al2() #sadece isim ve yazarlari alir
#verileri_al() #tum verileri almak icin kullanilir

#veri_ekle() #veri eklemek icin cagiriyoruz

""" **veri_ekle2 calistirilmak istenirse**
isim = input("isim:")
yazar = input("yazar:")
sayfa_sayisi = int(input("sayfa sayisi:"))
veri_ekle2(isim,yazar,sayfa_sayisi)
"""

con.close()

