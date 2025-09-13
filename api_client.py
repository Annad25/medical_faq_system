import requests

BACKEND_URL = "http://127.0.0.1:8001"  # replace with deployed FastAPI URL

def ask_backend(question: str):
    response = requests.post(f"{BACKEND_URL}/ask", json={"question": question})
    return response.json()["answer"]
