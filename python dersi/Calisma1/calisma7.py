# sklearn kütüphanesini yükle
from sklearn.linear_model import LinearRegression
import numpy as np

# Örnek veri setini oluştur
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

# Doğrusal regresyon modelini oluştur
model = LinearRegression()

# Modeli eğit
model.fit(X, y)

# Tahmin yap
X_new = np.array([[6]])
y_pred = model.predict(X_new)

print("Tahmin edilen değer:", y_pred)
