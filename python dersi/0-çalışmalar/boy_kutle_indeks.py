"""Problem 2
Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.

Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)
"""
boy=float(input("boy:"))
kilo=int(input("kutle"))
print("Boy Kutle Indeks: {}".format(kilo/(boy*boy)))