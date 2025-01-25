import os
from PIL import Image
size_300 = (300,300)
size_700 = (700,700)
for f in os.listdir((".")):
    if f.endswith(".jpeg"):
        i = Image.open(f)
        fn,fext = os.path.splitext(f)

        i.thumbnail(size_700)
        i.save(("700/{}_700{}").format(fn,fext))
        i.thumbnail(size_300)
        i.save(("300/{}_300{}").format(fn, fext))


image1 = Image.open("resim1.jpeg")
image1.save("resim1.png")
