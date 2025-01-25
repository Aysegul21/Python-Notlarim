import numpy as np

matris = np.random.randint(1,10,(4,4))
print(matris)
"""ddd

np.arange() fonksiyonu, başlangıç ve bitiş değerleri arasında 
(bitiş değeri dahil değil) eşit aralıklı sayılar içeren 
bir dizi oluşturmak için kullanılır.
"""
matris = np.array([np.arange(0,3),np.arange(3,6)])
print("\n" ,matris)