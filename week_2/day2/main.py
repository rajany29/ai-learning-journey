import os
import numpy as np 
from sentence_transformers import SentenceTransformer

def cosine_similarity(a, b):
    return np.dot(a, b) / (
        np.linalg.norm(a) * np.linalg.norm(b)
    )

model = SentenceTransformer("all-MiniLM-L6-v2") #384
text = "Machine learning is fun."

embedding=model.encode(text)
# print(embedding.shape)
# print(embedding)

t1="There is not good language"
t2="no matching"

v1=model.encode(t1)
v2=model.encode(t2)
print(cosine_similarity(v1, v2))

