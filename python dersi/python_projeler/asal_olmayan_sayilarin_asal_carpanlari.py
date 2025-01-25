def asal_carpan_ekrana_yazdirma(asal1):
    print("\n{}:".format(asal1),end="")

    for i in range(2, asal1):
        sayac = 0
        if (asal1 % i == 0):
            if (i == 2):
                print("{} ".format(2),end = "")
            for j in range(2, i):
                if (i % j != 0):
                    sayac = 1
                else:
                    sayac = 0
                    break
            if(sayac == 1):
                print("{} ".format(i), end="")

def asal_olmayan_sayilar(asal1,asal2):
    for i in range(asal1,asal2+1):
        sayac = 1
        for j in range(2,i):
            if(i % j != 0):
                sayac = 1
            else:
                asal_carpan_ekrana_yazdirma(i)
                break

asal1 = int(input("alt degeri giriniz:"))
asal2 = int(input("ust degeri giriniz:"))
asal_olmayan_sayilar(asal1,asal2)

