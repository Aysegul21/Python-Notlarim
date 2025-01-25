import cv2

# 0 resmi gri renk yapar.
resim = cv2.imread("images (3).jfif",0)

cv2.imshow("Resim", resim)#resmi açıyor
cv2.waitKey(0)#sonsuza kadar bekler
cv2.destroyWindow()#bir tuşa basıldığı zaman resim kapanır