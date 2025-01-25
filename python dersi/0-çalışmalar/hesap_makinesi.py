#  HESAP MAKINASI YAPIMI

a = int(input("Birinci sayiyi giriniz:"))
b = int(input("Ikinci sayiyi giriniz:"))
print("1-Toplama Islemi")
print("2-Cikarma Islemi")
print("3-Carpma Islemi")
print("4-Bolme Islemi")
islem=int(input("islem seciniz:"))
if(islem == 1):
    print("{} + {} = {}".format(a,b,a+b))
elif(islem == 2):
    print("{} - {} = {}".format(a,b,a-b))
elif(islem == 3):
    print("{} * {} = {}".format(a,b,a*b))
elif(islem == 4):
    print("{} / {} = {}".format(a,b,a/b))
else:
    print("Islem secimi bulunamadi")

