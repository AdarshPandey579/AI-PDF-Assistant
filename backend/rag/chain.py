from retriever import retriever
from prompts import PROMPT

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


retriever = retriever
model = ChatGroq(model= "llama-3.3-70b-versatile",api_key=os.getenv("GROQ_API_KEY"),temperature=0)
parser = StrOutputParser()

def format_docs(docs):
    return "\n\n".join(
        f"Source: {doc.metadata.get('file_name', 'Unknown')}\n{doc.page_content}"
        for doc in docs
    )

parllel_chain = RunnableParallel({
    "context" : retriever | RunnableLambda(format_docs),
    "question" : RunnablePassthrough()
})

chain = parllel_chain | prompt | model | parser


# response = chain.invoke("What is Deep Learning?")
# print(response)