"""
5. Elmas Dataframe'in satır ve sütun sayısını
ve her sütunun veri türünü bulan bir Pandas programı yazın.
"""
import pandas as pd

veri = pd.read_csv("diamonds.csv")
print("\n*****Satir ve sutun sayilari*************")
print(veri.shape)
print("\n**********Her sutunun veri turu**********")
print(veri.dtypes)

