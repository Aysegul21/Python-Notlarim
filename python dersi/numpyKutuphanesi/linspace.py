# Gerekli kütüphaneleri içe aktarıyoruz
import numpy as np
import torch
from transformers import BertTokenizer, BertModel
from sentence_transformers import SentenceTransformer
from scipy.spatial.distance import cosine

# Örnek cümleler
sentences = [
    "Kedi minderin üzerinde oturuyor.",
    "Bir kedi halının üstünde dinleniyor.",
    "Araba yolda ilerliyor.",
    "Kitap masanın üzerinde duruyor.",
    "Bir çocuk bahçede oynuyor.",
    "Telefon şarj oluyor.",
    "Yağmur pencereden akıyor.",
    "Güneş dağın arkasından doğuyor.",
    "Kuşlar sabahları şarkı söylüyor.",
    "Bilgisayar masada çalışıyor."
]

# Yöntem 1: BERT [CLS] belirteci
# BERT tokenizer ve modeli yükle
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# Cümleleri BERT tokenizer kullanarak tokenize et
inputs = tokenizer(sentences, return_tensors='pt', padding=True, truncation=True)

# Modeli çalıştırırken gradyanları kaydetmemek için with torch.no_grad() kullanılır
with torch.no_grad():
    outputs = model(**inputs)

# Modelin çıktısındaki [CLS] belirtecinin gömme vektörünü alıyoruz
cls_embeddings = outputs.pooler_output.detach().numpy()

# Yöntem 2: BERT belirteç gömülmeleri (ortalama havuzlama)
with torch.no_grad():
    output = model(**inputs)[0]  # modelin tüm gömmeleri
mean_pooling = torch.mean(output, dim=1)
bert_embeddings = mean_pooling.detach().numpy()

# Yöntem 3: Sentence-BERT
sentence_model = SentenceTransformer('bert-base-nli-mean-tokens')
sentence_embeddings = sentence_model.encode(sentences)

# Benzerlik hesaplama: İki cümle arasındaki benzerliği hesaplamak için kosinüs benzerliğini kullanıyoruz
# Kosinüs benzerliği, iki vektör arasındaki açıya dayanır, değer 1'e yaklaştıkça cümleler daha benzer olur

def calculate_similarity(embeddings):
    similarities = []
    for i in range(len(embeddings)):
        for j in range(i + 1, len(embeddings)):
            sim = 1 - cosine(embeddings[i], embeddings[j])
            similarities.append(sim)
    return similarities

# Yöntem 1: BERT [CLS] belirteci ile benzerlikler
cls_similarities = calculate_similarity(cls_embeddings)
print(f"Yöntem 1 (BERT [CLS] belirteci): {cls_similarities}")

# Yöntem 2: BERT belirteç gömülmeleri ile benzerlikler
bert_similarities = calculate_similarity(bert_embeddings)
print(f"Yöntem 2 (BERT belirteç gömülmeleri): {bert_similarities}")

# Yöntem 3: Sentence-BERT ile benzerlikler
sentence_similarities = calculate_similarity(sentence_embeddings)
print(f"Yöntem 3 (Sentence-BERT): {sentence_similarities}")
