from pathlib import Path
import shutil

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

from pdf_summarizer.loader import load_pdf
from pdf_summarizer.chunker import split_docs
from pdf_summarizer.summarizer import summarize_chunks, generate_final_summary
from utils.export import save_markdown

from rag.loader import load_documents
from rag.splitter import split_documents
from rag.vector_store import add_documents
from rag.chain import chain
from pydantic import BaseModel

app = FastAPI(title="AI Pdf Assistant")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://ai-pdf-assistant-mu.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


SUMMARY_UPLOAD_DIR = Path("uploads/summarizer")
SUMMARY_UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@app.get("/")
def home():
    return {"message": "PDF Summarizer API Running"}

@app.post("/summarize")
async def summarize_pdf(file: UploadFile = File(...)):
    print("1. Request received")

    file_path = SUMMARY_UPLOAD_DIR / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    print("2. File saved")

    documents = load_pdf(str(file_path))
    print("3. PDF loaded")

    chunks = split_docs(documents)
    print(f"4. Created {len(chunks)} chunks")

    chunk_summaries = summarize_chunks(chunks)
    print("5. Chunks summarized")

    final_summary = generate_final_summary(chunk_summaries)
    print("6. Final summary generated")

    markdown_path = save_markdown(final_summary)
    print("7. Markdown saved")

    return {
    "summary": final_summary,
    "markdown_file": markdown_path
    }

@app.get("/download/markdown")
def download_markdown():
    return FileResponse(
        "exports/summary.md",
        media_type="text/markdown",
        filename="summary.md"
    )


RAG_UPLOAD_DIR = Path("uploads/rag")
RAG_UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@app.post("/upload")
async def upload_pdfs(files: list[UploadFile] = File(...)):

    pdf_paths = []
    for file in files:

        file_path = RAG_UPLOAD_DIR / file.filename

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        pdf_paths.append(file_path)

    documents = load_documents(pdf_paths)

    chunks = split_documents(documents)

    add_documents(chunks)

    return {
        "message": "PDFs uploaded successfully",
        "files": len(files),
        "chunks": len(chunks),
    }


class ChatRequest(BaseModel):
    question: str

@app.post("/chat")
async def chat(request: ChatRequest):

    answer = chain.invoke(request.question)

    return {
        "answer": answer
    }