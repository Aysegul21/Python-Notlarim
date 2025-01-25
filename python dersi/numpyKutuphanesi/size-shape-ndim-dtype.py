import numpy as np
#size : matrisin buyuklugunu verir
#shape : matrisin boyutlarını açıklar
#ndim : matrisin kac boyutlu oldugunu soyler
#dtype : tipini gosterir

vektor = np.array([1,2,3,4])
matris = np.array([[1,2,3],[4,5,6]])


print("vektor size: " ,vektor.size)
print("matris size: " , matris.size)

print("vektor shape: " , vektor.shape)
print("matris shape: " , matris.shape)

print("vektor ndim: " , vektor.ndim)
print("matris ndim: " , matris.ndim)

print("vektor dtype: ",vektor.dtype)
print("matris dtype: ",matris.dtype)
