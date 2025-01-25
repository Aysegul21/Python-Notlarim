from PIL import Image,ImageFilter
import os

os.chdir("C:\Users\ayseg\OneDrive\Belgeler\python dersi\PillowKutuphanesi")
image1 = Image.open("sıfırbir-kopya")
image1.rotate(180).save("sıfırbir2.jpeg")#180 derece çevirdi

image2 = Image.open("sıfırbir2.jpeg")
image2.convert(mode="L").save("sfırbir21.jpeg")#siyah beyaz yaptı
image2.filter(ImageFilter.CONTOUR).save("resim2222_filtre.jpeg")