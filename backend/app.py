from pathlib import Path
import shutil

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from utils.export import save_markdown

from loader import load_pdf
from chunker import split_documents
from summarizer import summarize_document, generate_final_summary

app = FastAPI(title="PDF Summarizer")
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

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@app.get("/")
def home():
    return {"message": "PDF Summarizer API Running"}

@app.post("/summarize")
async def summarize_pdf(file: UploadFile = File(...)):
    print("1. Request received")

    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    print("2. File saved")

    documents = load_pdf(str(file_path))
    print("3. PDF loaded")

    chunks = split_documents(documents)
    print(f"4. Created {len(chunks)} chunks")

    chunk_summaries = summarize_document(chunks)
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