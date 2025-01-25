import cv2

resim = cv2.imread("images (3).jfif")
cv2.imshow("Resim",resim)
cv2.imwrite("resim2.jpg",resim)
cv2.waitKey(0)
cv2.destroyAllWindows()