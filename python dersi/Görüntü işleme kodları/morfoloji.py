import numpy as np
import cv2

def dilate(image, kernel):
    
    height, width = image.shape
    kernel_height, kernel_width = kernel.shape
    dilated_image = np.zeros((height, width), dtype=np.uint8)
    
    # Kenar pikselleri hariç tüm pikselleri dolaş
    for i in range(kernel_height // 2, height - kernel_height // 2):
        for j in range(kernel_width // 2, width - kernel_width // 2):
            max_pixel = 0
            # Kernel içindeki pikselleri dolaşarak maksimum değeri bul
            for ki in range(-kernel_height // 2, kernel_height // 2 + 1):
                for kj in range(-kernel_width // 2, kernel_width // 2 + 1):
                    pixel_value = image[i + ki, j + kj] + kernel[ki + kernel_height // 2, kj + kernel_width // 2]
                    max_pixel = max(max_pixel, pixel_value)
            dilated_image[i, j] = max_pixel
    
    return dilated_image

# Test için bir örnek görüntü ve kernel oluşturalım
image = cv2.imread('jh.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow("winname", image)
# Örnek kernel
kernel = np.array([[0, 1, 0],
                   [1, 1, 1],
                   [0, 1, 0]], dtype=np.uint8)

# Dilate işlemi
dilated_image = dilate(image, kernel)

# Sonuçları görüntüle
print("Original Image:")
print(image)
print("\nDilated Image:")
print(dilated_image)