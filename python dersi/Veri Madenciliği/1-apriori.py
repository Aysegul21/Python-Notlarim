# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 16:00:10 2024

@author: ayseg
"""

# Kütüphaneler
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# Veri seti
dataset = [['Milk', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Dill', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Milk', 'Apple', 'Kidney Beans', 'Eggs'],
           ['Milk', 'Unicorn', 'Corn', 'Kidney Beans', 'Yogurt'],
           ['Corn', 'Onion', 'Onion', 'Kidney Beans', 'Ice cream', 'Eggs']]

# Veri setini TransactionEncoder ile kodlayın
te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)
pd.set_option("display.max_column",20)
print(df)

# Apriori algoritması ile sık öğe kümelerini bulun
frequent_itemsets = apriori(df, min_support=0.6, use_colnames=True)
frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))
print(frequent_itemsets)

# İki öğeden oluşan ve destek değeri 0.8'den büyük olan sık öğe kümelerini filtreleyin
result = frequent_itemsets[(frequent_itemsets['length'] == 2) & (frequent_itemsets['support'] >= 0.8)]
print(result)

# 'Onion' ve 'Eggs' içeren sık öğe kümelerini filtreleyin
result2 = frequent_itemsets[frequent_itemsets['itemsets'] == {'Onion', 'Eggs'}]
print(result2)

# Güvenilirlik (Confidence) ve Lift hesaplamaları
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])

# Daha seyrek bir formatta veri setini gösterin
oht_ary = te.fit(dataset).transform(dataset, sparse=True)
sparse_df = pd.DataFrame.sparse.from_spmatrix(oht_ary, columns=te.columns_)
print(sparse_df)

# Daha seyrek bir formattaki veri seti üzerinde Apriori algoritmasını çalıştırın
result3 = apriori(sparse_df, min_support=0.6, use_colnames=True, verbose=1)
print(result3)
