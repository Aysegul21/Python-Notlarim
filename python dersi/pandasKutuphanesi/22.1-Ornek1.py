"""
1. Belirtilen kaynaktan bir csv dosyasını okuyacak
ve ilk 5 satırı yazdıracak bir Pandas programı yazın.
"""

import pandas as pd
veri = pd.read_csv("diamonds.csv")
print(veri.head())
