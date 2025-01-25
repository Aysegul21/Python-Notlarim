import math
"""
#%% Mrhaba Dünya
msg = "hello world.."
print(msg)

#%% Değişkenler ve Methotlar
okul = "Erzurun Teknk Üniversitesi"
bolum = "Bilgisayar mühendisliği"
yil = 2024;
print(okul)
print(okul.upper())
print(okul.lower())
print(okul +" "+ bolum+" " + " "+str(yil))

##½½ whitespace Kullanımı (\n ve \t demek)
print(okul +"\n"+ bolum+" " + "\t"+str(yil))

##½½ whitespace Kullanımı Stripping
prog = " java "
print(prog.lstrip())#soldaki boşlukları siler
print(prog.rstrip())#sağdaki boşlukları siler
print(prog.strip())#tüm boşlukları siler

#½½ tip dönüşümü str, float, int

yil = "2023"
simdikiZaman = int(yil) + 1#str tipindeki yil int tipine çevrildi
print(simdikiZaman)

print("Dairenin yarıçapını giriniz:")
#eval ne girersek onun tipine çevirir yanı özel olarak int vs. girmemize gerek yok
yaricap = eval(input())

alan = 2.0*math.pi*yaricap
cevre = math.pi*yaricap*yaricap

print("Alani: " + str(alan) +"\nCevresi: " + str(cevre))
"""
#½½Listeler

dersler = ["OOP","DBMS" ,"JAVA","OTOMAT"]
print(dersler[0],end = " ")#ilk elemmani verir
print(dersler[1])#1. elemanı verir
print(dersler[-1])#son elemanı verir
print(dersler[0].title())# title methodu ilk karakteri büyük diğerlerini küçük yapar

dersler[-1] = "OTOMATLAR"

dersler.append("Yapay Zeka")#Listenin sonuna eleman ekler.
print(dersler[-1])
print(dersler)
dersler.insert(2,"Veri Bilimi")
print(dersler)

dersler.remove("OOP")#istediğimiz elemanı girerek onu sileriz

dersler.pop()#son elemanı siler
print(dersler)

#Listenin sıralanması

dersler.sort(reverse=True)#tüm elemanları büyükten küçüğe sıralar
print(dersler)

dersler.sort(reverse=False)#tüm elemanları küçükten büyüğe sıralar
print(dersler)

print(sorted(dersler))# dersleri sadece değişik gösterir ama atama yapmaz sort ile sorted farkı

str1 = "ETÜ "
print(str1*3)#ifadeyi 3 kez yazdırır

x = 100
y = 200
print("x: " + str(x) + "y: " + str(y))
x,y = y,x#değiştirme
print("x: " + str(x) + "y: " + str(y))