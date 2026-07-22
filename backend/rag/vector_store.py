from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
from .embeddings import embedding_model

COLLECTION_NAME = "pdf_rag"

client = QdrantClient(
    host="localhost",
    port=6333,
)

def recreate_collection():
    if client.collection_exists(COLLECTION_NAME):
        client.delete_collection(COLLECTION_NAME)

    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(
            size=384,
            distance=Distance.COSINE,
        ),
    )

vector_store = QdrantVectorStore(
    client=client,
    collection_name=COLLECTION_NAME,
    embedding=embedding_model,
)

def add_documents(chunks):
    vector_store.add_documents(chunks)