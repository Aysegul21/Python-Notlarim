"""
Problem 5
Kullanıcıdan iki tane sayı isteyin ve
bu sayıların değerlerini birbirleriyle değiştirin.
"""


a=int(input("a degerini giriniz:"))
b=int(input("b degerini giriniz:"))
#yontem1
#a,b=b,a
#print("a={} b={}".format(a,b))
#yontem2
#a b den buyuk girilsin ya da if ile de cozulebilir
"""
a=a-b
b=a+b
a=a+b
print("a={} b={}".format(a,b))
"""
#yontem3
gecici=a
a=b
b=gecici

print("a={} b={}".format(a,b))