#Kutuphaneler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

seri = pd.Series(np.random.randn(10)*10,index = np.arange(0,100,10))
seri.plot()
plt.show()
data = pd.DataFrame(np.random.randn(10,2),index=np.arange(0,100,10),columns=["A","B"])

print(data)
data.plot
