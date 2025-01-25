"""
Problem 3
Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol
yaptığı bilgilerini alın ve sürücünü toplam ne kadar ödemesini
gerektiğini hesaplayın.
"""
Km_ucret=int(input("lutfen km basına kac tl yaktıgını giriniz:"))
toplam_km=int(input("lutfen kac km yol aldiginizi giriniz:"))
print("{} TL odeme yapılacaktır.".format(Km_ucret*toplam_km))