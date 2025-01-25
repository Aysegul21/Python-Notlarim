# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 16:19:28 2024

@author: ayseg
"""
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import eclat
import pandas as pd

# Veri seti örneği
dataset = [['Milk', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Dill', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Milk', 'Apple', 'Kidney Beans', 'Eggs'],
           ['Milk', 'Unicorn', 'Corn', 'Kidney Beans', 'Yogurt'],
           ['Corn', 'Onion', 'Onion', 'Kidney Beans', 'Ice cream', 'Eggs']]

# TransactionEncoder ile veri setini kodla
te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)
pd.set_option("display.max_column",20)
print(df)

# Eclat algoritması ile sık öğe kümelerini bul
frequent_itemsets = eclat(df, min_support=0.6, use_colnames=True)
print(frequent_itemsets)

