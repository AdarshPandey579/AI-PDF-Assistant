from langchain_community.document_loaders import PyPDFLoader

def load_pdf(file_path : str):
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    return documents


# [
#     Document(
#         page_content="Page 1 text...",
#         metadata={"page": 0}
#     ),

#     Document(
#         page_content="Page 2 text...",
#         metadata={"page": 1}
#     ),

#     Document(
#         page_content="Page 3 text...",
#         metadata={"page": 2}
#     )
# ]