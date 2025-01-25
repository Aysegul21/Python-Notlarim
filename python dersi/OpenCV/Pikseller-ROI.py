
import cv2
import matplotlib.pyplot as plt

resim = cv2.imread("resim2.jpg")
print(resim[:2])
kirp = resim[20:100,100:150]
resim[0:80,200:250] = kirp

plt.subplot(121)
plt.imshow(resim)
plt.subplot(122)
plt.imshow(kirp)
plt.show()
