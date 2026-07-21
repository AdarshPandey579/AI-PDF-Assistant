from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=3000,
        chunk_overlap=300
    )

    chunks = splitter.split_documents(documents)
    return chunks




# [
#     Document(page_content="Artificial Intelligence..."),
#     Document(page_content="Machine Learning..."),
#     Document(page_content="Deep Learning..."),
#     ...
# ]

# Document objects, but now they represent chunks, not entire pages.