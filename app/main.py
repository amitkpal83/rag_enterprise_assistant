from fastapi import FastAPI
from pydantic import BaseModel
from app.rag_pipeline import RAGPipeline

app = FastAPI()
rag = None

class QueryRequest(BaseModel):
    question: str

@app.on_event("startup")
def startup():
    global rag
    from langchain.vectorstores import FAISS
    from langchain.embeddings import OpenAIEmbeddings
    rag = RAGPipeline(FAISS.from_texts(["sample document"], OpenAIEmbeddings()))

@app.post("/ask")
def ask(req: QueryRequest):
    return rag.query(req.question)
