import sqlite3 # Sqlite'yı dahil ediyoruz

con = sqlite3.connect("kutuphane.db") # Tabloya bağlanıyoruz.
cursor = con.cursor() # cursor isimli değişken veritabanı üzerinde işlem yapmak için kullanacağımız imleç olacak.
def tabloOlustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık(Isim TEXT ,Yazar TEXT ,YayinEvi TEXT ,SayfaSayisi INT)")
    con.commit()# Sorgunun veritabanı üzerinde geçerli olması için commit işlemi gerekli.

def verileriAl():
    cursor.execute("SELECT * FROM kitaplık")
    data = cursor.fetchall()
    print("Kitaplik Tablosunun bilgileri....")
    for i in data:
        print(i)
def verileriAl2():
    cursor.execute("SELECT Isim , Yazar FROM kitaplık")
    data = cursor.fetchall()
    print("Kitaplik Tablosunun bilgileri....")
    for i in data:
        print(i)
def verileriAl3(yayinEvi):
    cursor.execute("SELECT * FROM kitaplık  WHERE YayinEvi = ?",(yayinEvi,))
    data = cursor.fetchall()
    print("Kitaplik Tablosunun bilgileri....")
    for i in data:
        print(i)

def verileriGuncelle(yayinEvi):
    cursor.execute("UPDATE kitaolık set YayinEvi = ? where YayinEvi = ?",("Everest" , yayinEvi))
    con.commit()

def verileriSil(yazar):
    cursor.execute("DELETE FROM kitaplık where Yazar = ?",(yazar,))
    con.commit()

def degerEkle():
    cursor.execute("INSERT INTO kitaplık VALUES('Istanbul Hatirasi' , 'Ahmet UMIT','Everest' , 261 )")
    con.commit()

def degerEkle2(isim,yazar,yayinEvi,sayfaSayisi):
    cursor.execute("INSERT INTO kitaplık VALUES(?,?,?,?)",(isim,yazar,yayinEvi,sayfaSayisi))
    con.commit()


isim = input("İsim:")
yazar = input("Yazar:")
yayinevi = input("Yayinevi:")
sayfaSayisi =  int(input("Sayfa Sayisi:"))

degerEkle2(isim,yazar,yayinevi,sayfaSayisi)
verileriAl()
verileriAl2()
verileriAl3("22")
verileriSil("dfr")
con.close() # Bağlantıyı koparıyoruz.
