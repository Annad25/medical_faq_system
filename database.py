import chromadb
from google import genai
from google.genai import types
from google.api_core import retry
from chromadb import EmbeddingFunction, Documents, Embeddings

from config import GOOGLE_API_KEY

client = genai.Client(api_key=GOOGLE_API_KEY)

is_retriable = lambda e: (isinstance(e, genai.errors.APIError) and e.code in {429, 503})

class GeminiEmbeddingFunction(EmbeddingFunction):
    document_mode = True

    @retry.Retry(predicate=is_retriable)
    def __call__(self, input: Documents) -> Embeddings:
        task = "retrieval_document" if self.document_mode else "retrieval_query"
        embeddings = []
        for text in input:
            response = client.models.embed_content(
                model="models/text-embedding-004",
                contents=text,
                config=types.EmbedContentConfig(task_type=task),
            )
            embeddings.append(response.embeddings[0].values)
        return embeddings

# Init DB
DB_NAME = "medquaddb"
embed_fn = GeminiEmbeddingFunction()
chroma_client = chromadb.PersistentClient(path="./chroma_db")
db = chroma_client.get_or_create_collection(name=DB_NAME, embedding_function=embed_fn)

print(" DB contains:", db.count(), "documents")
print(" Sample entries:", db.peek())

