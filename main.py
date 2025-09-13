from fastapi import FastAPI
from pydantic import BaseModel
from rag_pipeline import query_pipeline

app = FastAPI(title="Medical FAQ Chatbot")

class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    answer: str

@app.post("/ask", response_model=QueryResponse)
def ask_question(req: QueryRequest):
    answer = query_pipeline(req.question)
    return {"answer": answer}
