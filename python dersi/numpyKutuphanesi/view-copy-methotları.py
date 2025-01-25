import numpy as np

"""
dizi.view() koduyla, dizi değişkeninin bir görünümü oluşturulur.
Görünüm, orijinal dizi ile aynı bellek konumunu paylaşır.
Orijinal dizide yapılan değişiklikler, görünümde de yansıtılır.
"""
print("view method")
matris1 = np.array([1,2,3,4,5,6]).reshape(2,3)
print("matris1\n",matris1)
matris2 = matris1.view()
print("matris2\n",matris2)
print(matris2[0])
matris2[0] = [3,3,3]
print("\nmatris2 nin ilk satırı degistirildikten sonra")
print("matris1\n",matris1)
print("matris2\n",matris2)


print("copy method")
matris3 = matris1.copy()
print("matris1\n",matris1)
print("matris3\n",matris3)
matris3[0] = [8,8,8]
print("\nmatris3 nin ilk satırı degistirildikten sonra")
print("matris1\n",matris1)
print("matris3\n",matris3)

