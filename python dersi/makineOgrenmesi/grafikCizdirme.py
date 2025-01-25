#Kutuphaneler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.Series(np.random.randn(4),index=list("xyzt"))
print(data)

fig,axes = plt.subplots(1,2)
data.plot(ax = axes[0],kind= "hist")
data.plot(ax = axes[1],kind= "barh")

veri = pd.DataFrame(np.random.randn(3,2),index =["A","B","C"],columns=pd.Index(["X","Y"]))
veri.plot(kind ="bar")
plt.show()

