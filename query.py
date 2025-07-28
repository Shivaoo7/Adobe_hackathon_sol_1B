import faiss
import numpy as np
from utils import embed_texts, load_metadata_json

INDEX_PATH = "index/rfp_faiss.index"
META_PATH = "index/metadata.json"

def query_rfps(user_query, top_k=5):
    index = faiss.read_index(INDEX_PATH)
    metadata = load_metadata_json(META_PATH)
    
    query_vec = embed_texts([user_query])
    query_vec = np.array(query_vec).astype("float32")
    
    D, I = index.search(query_vec, top_k)
    
    print(f"\n🔍 Top {top_k} results for: \"{user_query}\"\n")
    
    for rank, i in enumerate(I[0], 1):
        result = metadata[i]
        print(f"{rank}. {result['rfp_id']} (Page {result['page']})\n   ↪ {result['text'][:300].strip()}...\n")