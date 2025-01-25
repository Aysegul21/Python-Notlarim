import numpy as np

sayilar = np.array([1,2,3,4,5],dtype = "int8")
print(sayilar.dtype)
sayilar.astype("int64")
print("type degistirildikten sonra:",sayilar.dtype)