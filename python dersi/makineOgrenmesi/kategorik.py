#kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

veriler = pd.read_csv("eksikVeriler.csv")

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values = np.nan , strategy='mean')

ulke = veriler.iloc[:,0:1].values

print(ulke)

from sklearn import preprocessing
le = preprocessing.LabelEncoder()
ulke = le.fit_transform(veriler.iloc[:,0])
print("********************")
print(ulke)

ohe = preprocessing.OneHotEncoder()
ulke = ohe.fit_transform(ulke.reshape(-1,1)).toarray()
print(ulke)
