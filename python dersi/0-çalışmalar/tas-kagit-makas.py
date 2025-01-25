import random

tas = '''taş:
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

kagit = '''kagit:
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

makas = '''makas:
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

oyun_resimleri = [tas, kagit, makas]


secim = "evet"

while(secim == "evet"):

    cevap = int(input("Tas-kagit-makas hangisi?(tas icin 0 giriniz kagit icin 1 giriniz makas icin 2 giriniz..."))

    if ( cevap < 0 or cevap > 2 ):
        print("olmayan deger girdiniz..")
        continue
    else:
        print("seciminiz: \n{}".format(oyun_resimleri[cevap]))

      #tas kagit makas

    bilgisayar_cevabi = random.randint(1, 3)

    if cevap == 0 and bilgisayar_cevabi == 2:
        print("Kazandiniz!")
    elif bilgisayar_cevabi == 0 and cevap == 2:
        print("Kaybettiniz!")
    elif bilgisayar_cevabi > cevap:
        print("Kaybettiniz")
    elif cevap > bilgisayar_cevabi:
        print("Kazandiniz!")
    elif bilgisayar_cevabi == cevap:
        print("Berabere kaldiniz!")



    secim = input("Oyunu oynamak ister misiniz?")
