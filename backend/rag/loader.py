from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from rich import print

def load_documents(file_paths: list[str]):
    """
    Load multiple PDF files and return LangChain Document objects.
    """
    
    documents = []
    for file_path in file_paths:
        file_path = Path(file_path)
        loader = PyPDFLoader(file_path)
        docs = loader.load()
        for doc in docs:
            doc.metadata["file_name"] = file_path.name
        documents.extend(docs)

    return documents



# load_documents(["../uploads/PDF_Summarizer_Test_Document.pdf"])


# Document(
#         metadata={
#             'producer': 'ReportLab PDF Library - (opensource)',
#             'creator': '(unspecified)',
#             'creationdate': '2026-07-14T20:09:03+00:00',
#             'author': '(anonymous)',
#             'keywords': '',
#             'moddate': '2026-07-14T20:09:03+00:00',
#             'subject': '(unspecified)',
#             'title': '(anonymous)',
#             'trapped': '/False',
#             'source': '..\\uploads\\PDF_Summarizer_Test_Document.pdf',
#             'total_pages': 15,
#             'page': 8,
#             'page_label': '9',
#             'file_name': 'PDF_Summarizer_Test_Document.pdf'
#         },
#         page_content='Chapter 9: Timeline\n2017: Transformer 2018: BERT 2020: GPT-3 2022: ChatGPT 2025+: Agentic AI2017: Transformer\n2018: BERT 2020: GPT-3 2022: ChatGPT 
# 2025+: Agentic AI2017: Transformer 2018: BERT 2020:\nGPT-3 2022: ChatGPT 2025+: Agentic AI'