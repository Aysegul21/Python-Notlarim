
import cv2
import numpy as np
#Siyah ekran
resim = np.zeros((512,512,3),np.uint8)
#cv2.imshow("Resim",resim)

#Cizgi cizmek icin
resim2 = cv2.line(resim,(0,0),(512,80),(30,40,200),6)
#cv2.imshow("resim2",resim2)

#Kare yapmak icin
resim3 = cv2.rectangle(resim,(20,20),(450,50),(50,0,50),5)
#cv2.imshow("resim3",resim3)

#Daire cizmek icin
resim4 = cv2.circle(resim,(256,256),200,(200,50,255),70)
#cv2.imshow('resim',resim4)

# Resme yazı yazdırmak için
font = cv2.FONT_HERSHEY_COMPLEX
resim5 = cv2.putText(resim,"Aysegul",(10,150),font, 4,(255,255,255),4,cv2.LINE_AA)
resim6 = cv2.putText(resim,"TEKES",(10,300),font, 4,(255,255,255),4,cv2.LINE_AA)

cv2.imshow("Resim",resim6)
a = cv2.waitKey(0)
if a == ord("s"):
    cv2.destroyAllWindows()


