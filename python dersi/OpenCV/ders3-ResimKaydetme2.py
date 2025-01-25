import cv2

resim = cv2.imread("resim.jpg")
cv2.imshow("Resim",resim)

a = cv2.waitKey(0)

if a == 27:
    cv2.destroyAllWindows()
elif a == ord("s"):
    cv2.imwrite("resim2.jpeg",resim)
