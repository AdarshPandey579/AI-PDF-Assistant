from .retriever import retriever
from .prompts import PROMPT

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel , RunnablePassthrough , RunnableLambda


load_dotenv()

prompt = PromptTemplate(
    template= PROMPT,
    input_variables=["context", "question"]
)


pdf_retriever = retriever
model = ChatGroq(model= "llama-3.3-70b-versatile",api_key=os.getenv("GROQ_API_KEY"),temperature=0)
parser = StrOutputParser()

def format_docs(docs):
    return "\n\n".join(
        f"Source: {doc.metadata.get('file_name', 'Unknown')}\nPage: {doc.metadata.get("page")}\n\n{doc.page_content}"
        for doc in docs
    )

parallel_chain = RunnableParallel({
    "context" : pdf_retriever | RunnableLambda(format_docs),
    "question" : RunnablePassthrough()
})

chain = parallel_chain | prompt | model | parser

# while True:
#     query = input("INPUT: ")
#     if query == "exit": break
#     response = chain.invoke(query)
#     print(response)

# response = chain.invoke("What is Deep Learning?")
# print(response)