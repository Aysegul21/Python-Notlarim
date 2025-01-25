def selamla(isim):
    print("Selam",isim,"!")

selamla("Aysegul")

merhaba = selamla   # Bir tane değişkene atıyoruz.
# merhaba # Obje tipi fonksiyon oldu.

merhaba("Aysegul TEKES")

def fonksiyon1():
    
    def fonksiyon2():
        print("icerdeki fonksiyon !!")

    print("Dis katman fonksiyon")
    fonksiyon2()


print("\n")
fonksiyon1()
