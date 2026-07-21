from langchain_huggingface import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5",
    # model_kwargs={"device": "cpu"},
    model_kwargs={"device": "cuda:0"},
    encode_kwargs={"normalize_embeddings": True}
)
