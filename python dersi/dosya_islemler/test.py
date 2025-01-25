

file = open("bilgiler.txt","r",encoding = "utf-8")
#file2 = open("bilgiler.txt","w")

karakterSayaci = -1
satirSayisi = 0

for satir in file:
   karakterSayaci = -1
   satirSayisi += 1
   print()
   for karakter in satir:
       karakterSayaci+=1

       if karakterSayaci%2 == 0:
           if karakter == "1" or karakter == "0" or karakter == " ":
               print(karakter,end="")
           else:
               print("Burada Sorun var",end="")
               print("e"+karakter +"w",end="")
               print(satirSayisi,end="")



file.close()
