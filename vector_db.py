import faiss
import pandas as pd
from sentence_transformers import SentenceTransformer
import numpy as np

# Load dataset
df = pd.read_csv("housing.csv")

# Convert each row into text format
df["combined"] = df.apply(lambda row: 
    f"Price {row['price']}, Area {row['area']} sqft, "
    f"Bedrooms {row['bedrooms']}, Bathrooms {row['bathrooms']}, "
    f"Stories {row['stories']}, Parking {row['parking']}", axis=1
)

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(df["combined"].tolist())

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

def search_property(query, k=1):
    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), k)
    return df.iloc[indices[0]]