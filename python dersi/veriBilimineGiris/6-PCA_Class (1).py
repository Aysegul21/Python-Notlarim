# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 09:54:09 2024

@author: ETUVR
"""

import seaborn as sns

iris_data = sns.load_dataset("iris")


iris_data.describe().T

# Encode labels
iris_data.species.replace({'setosa':0,'versicolor':1,'virginica':2},inplace=True)

X = iris_data.drop(['species'],axis=1) #data
y = iris_data.species #labels

#pre-processing
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X = scaler.fit_transform(X)

#%% without PCA
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,
                                                    random_state=20, stratify=y)
#supervised algoritma seçimi
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(7)
knn.fit(X_train, y_train)

print("PCA sız eğitim skoru:", knn.score(X_train, y_train),"%")
print("PCA sız test skoru:", knn.score(X_test, y_test),"%")



#%% with PCA
from sklearn.decomposition import PCA
pca = PCA()
X_new = pca.fit_transform(X)

pca.get_covariance()
explained_variance = pca.explained_variance_ratio_
explained_variance

pca = PCA(n_components=4)
X_new = pca.fit_transform(X)

from sklearn.model_selection import train_test_split
X_train_new, X_test_new, y_train, y_test = train_test_split(X_new,y,test_size=0.3,
                                                    random_state=20, stratify=y)


knn_pca = KNeighborsClassifier(7)
knn_pca.fit(X_train_new,y_train)

print("PCA ile eğitim skoru:", knn_pca.score(X_train_new, y_train),"%")
print("PCA ile test skoru:", knn_pca.score(X_test_new, y_test),"%")








