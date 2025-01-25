"""
         AA-000-AA
         AA-001-AA
            ...
         AA-999-AA
         AA-001-AB
            ...
         AA-999-ZZ
         AB-001-AA
i=65 j=67 sayac1=4 sayac2=2 sayac3=3 a=68 b=70
plaka AC-423-DF den 1 milyon sonra plaka ne olur
#  chr(ascidegeri)
"""


a = input("plaka:")
liste = list(a)
liste2 = a[3:6]
a1 = ord(liste[0])
a2 = ord(liste[1])
sayac = -1
sayac1 = int(liste2[0])
sayac2 = int(liste2[1])
sayac3 = int(liste2[2])
a = ord(liste[7]) - 1
b = ord(liste[8]) - 2
artis = int(input("artis degerini giriniz:"))
while (sayac < artis):
    for i in range(a1, 91):
        for j in range(a2, 91):
            while (a != 90):
                a += 1
                if (sayac == artis):
                    break
                while (b != 90):
                    b += 1
                    if (sayac == artis):
                        break
                    while (sayac1 != 10):
                        sayac += 1
                        if (sayac == artis):
                            if (i == 90 and j == 90 and a == 90 and b == 90):
                                print("ZZ-{}{}{}-ZZ".format(sayac1, sayac2, sayac3, ))
                            else:
                                print("{}{}-{}{}{}-{}{}".format(chr(i), chr(j), sayac1, sayac2, sayac3, chr(a), chr(b)))
                            break
                        if (sayac3 != 9):
                            sayac3 += 1
                        elif (sayac3 == 9):
                            if (i == 65 and j == 65 and a == 65 and b == 65 and sayac1 == 0 and sayac2 == 0):
                                sayac3 = 0
                            elif (not (i == 65 and j == 65 and a == 65 and b == 65 and sayac1 == 0 and sayac2 == 1)):
                                sayac3 = 1
                            if (sayac2 != 9):
                                sayac2 += 1
                            elif (sayac2 == 9):
                                sayac2 = 0
                                if (sayac1 != 10):
                                    sayac1 += 1
                    if (sayac1 == 10):
                        sayac1 == 0
                    if (b != 90):
                        b += 1
                    sayac1 = 0
                if (b == 90):
                    b = 64
            if (a == 90):
                a = 64
        a2 = 65
    a1 = 65









