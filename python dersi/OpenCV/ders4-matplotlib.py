

import cv2
from matplotlib import pyplot as plt

resim = cv2.imread('resim.jpg')

plt.imshow(resim,cmap ="gray",interpolation='bicubic')
plt.xticks([])
plt.yticks([])

plt.show()

