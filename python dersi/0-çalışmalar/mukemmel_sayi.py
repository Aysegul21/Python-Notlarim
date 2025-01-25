"""
Problem 1
Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını
bulmaya çalışın.
Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu
sayıya "mükemmel sayı" denir. Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)
"""
sayi = int(input("sayiyi giriniz:"))
sayac = 0

for i in range(1,sayi):
    if(sayi % i == 0):
        sayac += i
if(sayi == sayac):
    print("{} sayisi bir mukemmel sayidir.".format(sayi))




