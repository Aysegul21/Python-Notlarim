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


def plakahesapla(plaka1,artis):
    liste=list(plaka1)
    birincikisim = list(liste[0:2])
    ikincikisim = list(liste[7:9])
    sayi = liste[3:6]
    sayi = int(sayi[0])*100+int(sayi[1])*10+int(sayi[2])
    artis = int(artis)
    for i in range(artis):
        if(sayi  == 999):
            sayi = 0
            if(ikincikisim[1] == "Z"):
                ikincikisim[1] = "A"
                if (ikincikisim[0] == "Z"):
                    ikincikisim[0] = "A"
                    if (birincikisim[1] == "Z"):
                        birincikisim[1] = "A"
                        if (birincikisim[0] == "Z"):
                            birincikisim[0] = "A"
                            sayi = 0
                        else:
                            birincikisim[0] = chr(ord(birincikisim[0])+1)
                    else:
                        birincikisim[1] = chr(ord(birincikisim[1])+1)
                else:
                    ikincikisim[0] = chr(ord(ikincikisim[0])+1)
            else:
                ikincikisim[1]=chr(ord(ikincikisim[1])+1)
        sayi += 1
    print("{}{}-{}-{}{}".format(birincikisim[0],birincikisim[1],str(sayi).zfill(3),ikincikisim[0],ikincikisim[1]))
    return 0
plaka1=input("plaka kodunu giriniz:")
artis=int(input("artis degerini giriniz:"))
plakahesapla(plaka1,artis)




