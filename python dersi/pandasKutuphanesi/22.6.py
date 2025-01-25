"""
6. Elmas Veri Çerçevesinin yalnızca 'nesne' sütunlarını özetlemek için
bir Pandas programı yazın.
"""
import pandas as pd

veri = pd.read_csv("diamonds.csv")
print(veri.describe(include=["object"]))