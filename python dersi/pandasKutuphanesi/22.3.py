"""
3. Elmas DataFrame'den bir dizi seçmek için bir Pandas programı yazın.
Serinin içeriğini yazdırın.
"""
import pandas as pd

veri = pd.read_csv("diamonds.csv")
print(veri)
print(veri["x"])

