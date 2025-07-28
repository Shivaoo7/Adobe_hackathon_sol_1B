import json
import numpy as np
from sentence_transformers import SentenceTransformer
import fitz  # PyMuPDF

# Load multilingual embedding model
model = SentenceTransformer('sentence-transformers/distiluse-base-multilingual-cased-v1')

def extract_sections_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    sections = []
    
    for i, page in enumerate(doc):
        text = page.get_text("text")
        for para in text.split("\n\n"):
            cleaned = para.strip().replace("\n", " ")
            if len(cleaned) > 30:  # Ignore very short segments
                sections.append({"page": i + 1, "text": cleaned})
    
    return sections

def embed_texts(texts):
    return model.encode(texts, show_progress_bar=False, convert_to_numpy=True)

def save_metadata_json(data, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_metadata_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)