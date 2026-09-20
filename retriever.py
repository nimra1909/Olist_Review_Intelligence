import chromadb
from sentence_transformers import SentenceTransformer
client = chromadb.PersistentClient(path="./chroma_db_reviews/chroma_db_reviews")
collection = client.get_or_create_collection("customer_reviews")
embed_model = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)
def retrieve_reviews(query: str, top_k: int = 3):
    query_vector = embed_model.encode([query]).tolist()
    results = collection.query(query_embeddings=query_vector, n_results=top_k)
    matched_reviews = []
    if results and "documents" in results and results["documents"]:
        for doc, meta in zip(results["documents"][0], results["metadatas"][0]):
            matched_reviews.append({
                "review": doc,
                "order_id": meta.get("order_id"),
                "review_score": meta.get("review_score"),
                "predicted_stars": meta.get("predicted_stars")
            })
    return matched_reviews
