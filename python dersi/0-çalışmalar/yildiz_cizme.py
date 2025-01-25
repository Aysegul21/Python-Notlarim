
satir = int(input("kac satir olsun?"))

bosluk = satir - 1

for i in range(1,satir+1):
    yildiz = i * 2 - 1
    print(" "*bosluk,end = "")
    print("*"*yildiz)
    bosluk -= 1

yildiz = satir
bosluk = 1

for i in range(0,satir):
    satir -= 1
    yildiz = satir * 2 - 1
    print(" " * bosluk,end = "")
    print("*"*yildiz)
    bosluk += 1

