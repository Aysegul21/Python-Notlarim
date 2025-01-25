import pandas as pd

# Örnek bir veri çerçevesi oluşturalım
data = {
    'id': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Math': [85, 90, 75],
    'Science': [88, 82, 78]
}
df = pd.DataFrame(data)
print("Orjinal Veri Çerçevesi:")
print(df)

# melt() fonksiyonunu kullanarak geniş formatlı veri çerçevesini dar formatlı hale dönüştürelim
melted_df = pd.melt(df, id_vars=['id', 'Name'], var_name='Subject', value_name='Score')
print("\nDönüştürülmüş Veri Çerçevesi:")
print(melted_df)
