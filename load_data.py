# import pandas as pd
# from database import db  # reuse the db connection
# from database import GeminiEmbeddingFunction
# from database import chromadb
# # Load dataset
# documents = pd.read_csv("/home/tstack/workspace-anushka/ts-ocr/medical_faq_system/data/train.csv")  # adjust path

# # Set up ChromaDB
# DB_NAME = "medquaddb"

# embed_fn = GeminiEmbeddingFunction()
# embed_fn.document_mode = True

# chroma_client = chromadb.Client()
# db = chroma_client.get_or_create_collection(name=DB_NAME, embedding_function=embed_fn)
# print("Columns in dataset:", documents.columns.tolist())
# print(documents.head(3))


# # Add documents to database
# if 'Answer' in documents.columns and 'qtype' in documents.columns and 'Question' in documents.columns:
#     # Take a subset for testing (remove this line for full dataset). To avoid free-tier API limitations, we will a subset with 1 batch.
#     documents = documents.head(100) 
    
#     answers_to_embed = documents['Answer'].tolist()
#     ids = [str(i) for i in range(len(documents))]
#     metadatas = documents[['qtype', 'Question']].to_dict('records')

#     # Add in smaller batches to avoid timeouts
#     batch_size = 100
#     for i in range(0, len(answers_to_embed), batch_size):
#         end_idx = min(i + batch_size, len(answers_to_embed))
#         db.add(
#             documents=answers_to_embed[i:end_idx],
#             metadatas=metadatas[i:end_idx],
#             ids=ids[i:end_idx]
#         )
#         print(f"Added batch {i//batch_size + 1}, documents {i} to {end_idx-1}")
        
#     print(f"Successfully added {len(documents)} documents to ChromaDB using Gemini embeddings.")
# else:
#     print("Error: DataFrame is missing 'Answer', 'qtype', or 'Question' columns.")

import pandas as pd
from database import GeminiEmbeddingFunction
import chromadb

DB_NAME = "medquaddb"

# Load dataset
documents = pd.read_csv("/home/tstack/workspace-anushka/ts-ocr/medical_faq_system/data/train.csv")
print("Columns in dataset:", documents.columns.tolist())
print(documents.head(3))

# Setup Chroma with persistence
embed_fn = GeminiEmbeddingFunction()
embed_fn.document_mode = True
chroma_client = chromadb.PersistentClient(path="./chroma_db")
db = chroma_client.get_or_create_collection(name=DB_NAME, embedding_function=embed_fn)

# Insert documents
if set(["Answer", "qtype", "Question"]).issubset(documents.columns):
    documents = documents.head(100)
    answers_to_embed = documents['Answer'].tolist()
    ids = [str(i) for i in range(len(documents))]
    metadatas = documents[['qtype', 'Question']].to_dict('records')

    batch_size = 100
    for i in range(0, len(answers_to_embed), batch_size):
        end_idx = min(i + batch_size, len(answers_to_embed))
        db.add(
            documents=answers_to_embed[i:end_idx],
            metadatas=metadatas[i:end_idx],
            ids=ids[i:end_idx]
        )
        print(f"Added batch {i//batch_size + 1}, documents {i} to {end_idx-1}")

    print(f" Successfully added {len(documents)} documents to ChromaDB.")
else:
    print(" Dataset missing required columns.")
