#!/bin/bash

# Build Docker image
echo " Building Docker image..."
docker build -t adobe-rfp-search .

# Build index from PDFs
echo " Building vector index from RFPs..."
docker run --rm -v $(pwd)/data:/app/data -v $(pwd)/index:/app/index adobe-rfp-search --build

# Run a sample query
echo " Running sample query..."
docker run --rm -v $(pwd)/index:/app/index adobe-rfp-search --query "What are the eligibility criteria?"