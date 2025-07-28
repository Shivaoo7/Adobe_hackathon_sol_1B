# RFP Search Tool

Quick semantic search through RFP documents using vector embeddings.

## What it does

Processes PDF files and lets you search through them with natural language queries. Built this to stop manually digging through dozens of RFP documents looking for specific requirements.

## Setup

Drop your PDF files in the `data/` folder, then:

```bash
# Build and run everything
chmod +x sample_usage.sh
./sample_usage.sh
```

Or manually:

```bash
# Build the search index
python main.py --build

# Search for something
python main.py --query "eligibility requirements"
```

## Docker version

```bash
docker build -t rfp-search .
docker run --rm -v $(pwd)/data:/app/data -v $(pwd)/index:/app/index rfp-search --build
docker run --rm -v $(pwd)/index:/app/index rfp-search --query "your search here"
```

## Requirements

- Python 3.10+
- About 2GB RAM for the embedding model
- PDFs with actual text (not just scanned images)

## How it works

1. Extracts text from PDFs page by page
2. Splits content into meaningful sections
3. Converts text to vector embeddings using a multilingual model
4. Stores everything in a FAISS index for fast similarity search
5. When you query, finds the most relevant sections and shows you where they came from

The search understands context and meaning, not just keyword matching. So "project timeline" will find sections about schedules, deadlines, milestones, etc.

## File structure

```
adobe_hackathon_sol_1B/
├── data/           # Put your PDFs here
├── index/          # Generated search index files
├── main.py         # CLI interface
├── build_index.py  # Index creation
├── query.py        # Search functionality  
├── utils.py        # PDF processing utilities
└── requirements.txt
```

## Troubleshooting

**No results found**: Check if your PDFs have selectable text. Scanned documents won't work without OCR.

**Out of memory**: The embedding model needs ~2GB RAM. Try processing fewer files at once.

**Slow indexing**: Normal for large documents. The multilingual model is thorough but not fast.

**Docker issues**: Make sure you have enough disk space and the data/index folders are properly mounted.

## Notes

Uses PyMuPDF for PDF parsing and sentence-transformers for embeddings. The multilingual model works well with English but can handle other languages too.

Index files are saved locally so you only need to rebuild when adding new documents.