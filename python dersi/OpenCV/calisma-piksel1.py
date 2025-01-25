import cv2
import numpy as np
import matplotlib.pyplot as plt





resim = cv2.imread("resim2.jpg")
plt.imshow(resim)
plt.show()
height, width = resim.shape[:2]


for i in range(height):
    for j in range(width):
        plt.imshow(resim[i:i+1 ,j:j+1])
        plt.show()

