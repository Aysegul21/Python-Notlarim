# ogrencilerin sinav sonuclarina gore kalanlar kalanlar.txt dosyasina gecenler ise gecenler.txt dosyasına gonderilecektir

file =  open("kalanlar.txt","w")
file.close()
file =  open("gecenler.txt","w")
file.close()

file =  open("kalanlar.txt","a")

liste = [32,43,76,65,12,90,52,39,76,54,78,98,23,100,0,2]

for i in liste:
    if (i < 50):
        file.write( str(i) + "\n")
file.close()
file =  open("gecenler.txt","a")
for i in liste:
    if (i >= 50):
        file.write(str(i) + "\n")
file.close()