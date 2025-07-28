import os
import faiss
import numpy as np
from utils import extract_sections_from_pdf, embed_texts, save_metadata_json

PDF_DIR = "data"
INDEX_PATH = "index/rfp_faiss.index"
META_PATH = "index/metadata.json"

def build_vector_index():
    all_sections = []
    metadata = []
    
    for pdf_file in os.listdir(PDF_DIR):
        if pdf_file.endswith(".pdf"):
            rfp_id = pdf_file
            print(f"Processing {pdf_file}...")
            sections = extract_sections_from_pdf(os.path.join(PDF_DIR, pdf_file))
            embeddings = embed_texts([s['text'] for s in sections])
            all_sections.extend(embeddings)
            
            for idx, sec in enumerate(sections):
                metadata.append({"rfp_id": rfp_id, "text": sec['text'], "page": sec['page']})
    
    if not all_sections:
        print("No sections found to index.")
        return
    
    vector_matrix = np.vstack(all_sections).astype("float32")
    index = faiss.IndexFlatL2(vector_matrix.shape[1])
    index.add(vector_matrix)
    
    os.makedirs(os.path.dirname(INDEX_PATH), exist_ok=True)
    faiss.write_index(index, INDEX_PATH)
    save_metadata_json(metadata, META_PATH)
    
    print(f"Index built with {len(metadata)} sections from {len(os.listdir(PDF_DIR))} PDFs.")