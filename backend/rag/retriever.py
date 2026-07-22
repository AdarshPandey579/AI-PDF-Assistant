from .vector_store import vector_store

retriever = vector_store.as_retriever(search_type="similarity",search_kwargs={"k": 5})

# search_type="mmr"

# docs = retriever.invoke("Explain Docker Compose") # store list of similar responses