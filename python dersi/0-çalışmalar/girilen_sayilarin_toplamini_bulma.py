"""
Problem 4
Her bir while döngüsünde kullanıcıdan bir sayı alın ve
kullanıcının girdiği sayıları "toplam" isimli bir değişkene ekleyin.
Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın ve ekrana
"toplam değişkenini" bastırın.
"""

toplam = 0

while True:
    sayi = int(input("sayi giriniz.(Toplami gormek icin 0 ya basiniz.."))
    if (sayi == 0):
        print(toplam)
        break
    else:
        toplam += sayi

