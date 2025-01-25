"""
Problem 6
Buradaki problemin çözümünü derslerimizde özellikle öğrenmedik.
Burada mantık yürüterek ve list comprehension kullanarak
1'den 100'e kadar olan sayılardan sadece çift sayıları
bir listeye atmayı yapmayı çalışın.
"""

cift_sayilar = [i for i in range(1,101) if (i % 2 == 0) ]

for i in cift_sayilar:
    print("i: {}".format(i))
