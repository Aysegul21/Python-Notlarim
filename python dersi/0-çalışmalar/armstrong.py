"""
Problem 2
Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup
olmadığını bulmaya çalışın.

Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan
rakamlardan herbirinin 4. kuvvetinin toplamı
( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse
bu sayıya "Armstrong" sayısı denir.
Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4
"""
sayi = int(input("sayiyi giriniz:"))
sayi2 = sayi
sayac = 0
liste = list()

while( sayi != 0):              #121
    liste.append(sayi % 10)     #1      121    2
    sayi = sayi // 10           #       12
    sayac +=1
sonuc = 0

for i in liste:
    sonuc += i**sayac

if(sonuc == sayi2):
    print("{} sayisi bir armstrong sayisidir.".format(sayi2))




