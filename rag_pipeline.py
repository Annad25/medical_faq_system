from database import db, embed_fn, client

def add_documents(docs):
    answers = docs["Answer"].tolist()
    ids = [str(i) for i in range(len(docs))]
    metadatas = docs[["qtype", "Question"]].to_dict("records")

    batch_size = 100
    for i in range(0, len(answers), batch_size):
        db.add(
            documents=answers[i:i+batch_size],
            metadatas=metadatas[i:i+batch_size],
            ids=ids[i:i+batch_size]
        )

def query_pipeline(user_query: str, n_results: int = 2) -> str:
    embed_fn.document_mode = False
    result = db.query(query_texts=[user_query], n_results=n_results)
    [all_passages] = result["documents"]

    query_oneline = user_query.replace("\n", " ")
    prompt = f"""You are a helpful medical assistant.
Answer in simple terms for a non-medical person.

QUESTION: {query_oneline}
"""
    for passage in all_passages:
        passage_oneline = passage.replace("\n", " ")
        prompt += f"PASSAGE: {passage_oneline}\n"

    answer = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return answer.text
