#  Medical FAQ RAG Chatbot

This is a Retrieval-Augmented Generation (RAG) based chatbot that answers patient queries using a curated medical FAQ dataset.  
The chatbot retrieves relevant answers from a knowledge base and generates clear, natural responses using Google's Gemini model.

To get started, download the code base or medical_faq_system_zip file and follow the setup instructions.

---

##  Dataset
The dataset was taken from the **MedQuAD dataset** (Medical Question Answering Dataset).  
It contains medical questions (qtype, question text) and their reference answers.  
I used the `train.csv` file which includes fields:
- **qtype** → category of question (e.g., symptoms, treatment, susceptibility)  
- **Question** → the actual patient query  
- **Answer** → medically verified response  

---

##  Tech Stack
- **Backend**: FastAPI (Python)  
- **Database**: ChromaDB (vector store for embeddings)  
- **Embeddings**: Gemini Embedding API (`text-embedding-004`)  
- **Frontend**: Streamlit interface to chat with the bot  

---

## Setup Instructions

1. **Clone repo**
   ```bash
   git clone https://github.com/<your-username>/medical-faq-chatbot.git
   cd medical-faq-chatbot

2. **Create virtual environment**
    ```bash
    python3 -m venv env
    source env/bin/activate
3. **Install dependencies**
    ```bash
    pip install -r requirements.txt

4. **Set API key**
    ```bash
    Create a .env file and add your Google API key:
    GOOGLE_API_KEY=your_key_here

5. **Load data into vector database**
    ```bash
    from the root project directory, here medical_faq_chatbot
    python3 backend/load_data.py

6. **Run backend**
    ```bash
    cd backend
    uvicorn main:app --reload --port 8001

7. **Run frontend**
    ```bash
    streamlit run frontend/app.py
    and open the link, you will be shown the option to open browser

8. You can send queries through either the fastapi, swagger ui docs, or the chat interface





