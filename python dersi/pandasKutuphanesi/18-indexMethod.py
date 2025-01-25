#Kutuphaneler
import pandas as pd
import numpy as np

tarih = pd.date_range("20200418",periods=5)
print(tarih)
print("***********************")
veri = pd.DataFrame(np.random.randn(5,3),columns=["X","Y","Z"],index=tarih)
print(veri)
print("***********************")
print(veri.where(veri<0))

veri2 = pd.DataFrame(np.random.rand(20,6),columns = list("ABCDEF"))
print(veri2)
print(veri2.query("(B<E)"))