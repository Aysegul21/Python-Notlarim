"""
8.Elmas Dataframe'in ikinci sütununu kaldıracak bir Pandas programı yazın.

"""
import pandas as pd

veri =  pd.read_csv("diamonds.csv")
print(veri.head())
print("******************")
veri.drop(veri.columns[1],axis=1,inplace=True)
print(veri.head())
