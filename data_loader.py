from llama_index.readers.file import PDFReader
from sentence_transformers import SentenceTransformer
from llama_index.core.node_parser import SentenceSplitter
from dotenv import load_dotenv
import os

load_dotenv()

# Local embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')
EMBEDDING_DIM = 384  # Dimension for all-MiniLM-L6-v2

# Initialize sentence splitter
splitter = SentenceSplitter(chunk_size=1000, chunk_overlap=200)

def load_and_chunk_pdf(path: str):
    docs = PDFReader().load_data(file=path)
    texts = [d.text for d in docs if getattr(d, 'text', None)]
    chunks = []
    for t in texts:
        chunks.extend(splitter.split_text(t))
    return chunks

def embed_texts(texts: list[str]):
    """Embed texts using sentence-transformers (local model)"""
    embeddings = model.encode(texts, convert_to_numpy=True)
    return embeddings.tolist()