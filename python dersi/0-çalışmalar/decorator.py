def ekstra(fonk):
    def wrapper(sayilar):
        ciftler_toplami = 0
        cift_sayilar = 0
        tekler_toplami = 0
        tek_sayilar = 0

        for i in sayilar:
              if (i % 2 == 0):
                  ciftler_toplami += i
                  cift_sayilar += 1
              else:
                  tekler_toplami += i
                  tek_sayilar += 1
        print("Tek sayilar toplami = {}'dir. \n Tek sayilar ortalamasi = {}' dir.".format(tekler_toplami, tekler_toplami/tek_sayilar))
        print("Cift sayilar toplami = {}'dir. \n Cift sayilar ortalamasi = {}' dir.".format(ciftler_toplami,ciftler_toplami / cift_sayilar))

        fonk(sayilar)
    return wrapper


@ekstra
def ortalamayi_bul(sayilar):
    toplam = 0

    for sayi in sayilar:
        toplam += sayi

    print("Tum sayilarin ortalamasi {}'dir".format(toplam / len(sayilar)))


ortalamayi_bul([1, 2, 3, 4, 5, 6, 7, 8, 9])

