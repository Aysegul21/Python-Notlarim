"""
2. Diamonds DataFrame'den bir veri kümesi okumak ve
varsayılan sütun değerlerini değiştirmek ve ilk 6 satırı yazdırmak için
bir Pandas programı yazın.
"""

import pandas as pd
veri = pd.read_csv("diamonds.csv")
print(veri)

sutunlar = ["carat","cut","table","x","y","z"]
print(veri[sutunlar].head(6))


