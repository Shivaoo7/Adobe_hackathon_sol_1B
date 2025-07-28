from build_index import build_vector_index
from query import query_rfps
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--build', action='store_true', help='Build the vector index')
    parser.add_argument('--query', type=str, help='Query the RFPs')
    args = parser.parse_args()
    
    if args.build:
        build_vector_index()
    elif args.query:
        query_rfps(args.query)
    else:
        print("Use --build to create index or --query \"your question\" to search.")