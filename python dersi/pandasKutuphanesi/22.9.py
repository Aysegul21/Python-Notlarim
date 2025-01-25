"""
12. Elmas Dataframe'in 'kesilmiş' Serisini artan düzende
(bir Seri döndürür) sıralamak için bir Pandas programı yazın.
"""

import pandas as pd

veri = pd.read_csv("diamonds.csv")

print(veri.sort_values(by = "cut",ascending=True))