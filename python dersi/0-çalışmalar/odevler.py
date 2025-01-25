"""Problem 1
Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın.
Ekrana yazdırma işlemini *format* metoduyla yapmaya çalışın.
"""
a=int(input("sayi1 giriniz:"))
b=int(input("sayi2 giriniz:"))
c=int(input("sayi3 giriniz:"))
sayilar = [a,b,c,a*b*c]
print("{} * {} * {} = {}".format(sayilar[0],sayilar[1],sayilar[2],sayilar[3]))
