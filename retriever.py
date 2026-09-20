# retrieve_reviews.py
from typing import List, Dict, Any, Optional
import chromadb
from sentence_transformers import SentenceTransformer


# Initialize once at module level (will be reused across Streamlit sessions)
client = chromadb.PersistentClient(path="./chroma_db_reviews/chroma_db_reviews")
collection = client.get_or_create_collection(name="customer_reviews")

# Load the multilingual embedding model once
embed_model = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)


def retrieve_reviews(query: str, top_k: int = 3) -> List[Dict[str, Any]]:
    """
    Retrieve the most relevant customer reviews for a given query.

    Args:
        query: Natural language search query
        top_k: Number of reviews to return (default: 3)

    Returns:
        List of dictionaries containing:
            - review
            - order_id
            - review_score
            - predicted_stars
    """
    if not query or not query.strip():
        return []

    # Encode the query
    query_vector = embed_model.encode([query], show_progress_bar=False).tolist()

    # Query the collection
    results = collection.query(
        query_embeddings=query_vector,
        n_results=top_k,
        include=["documents", "metadatas", "distances"]
    )

    matched_reviews = []

    if results and results.get("documents") and results["documents"][0]:
        documents = results["documents"][0]
        metadatas = results["metadatas"][0] if results.get("metadatas") else [{}] * len(documents)
        distances = results["distances"][0] if results.get("distances") else [None] * len(documents)

        for doc, meta, distance in zip(documents, metadatas, distances):
            matched_reviews.append({
                "review": doc,
                "order_id": meta.get("order_id"),
                "review_score": meta.get("review_score"),
                "predicted_stars": meta.get("predicted_stars"),
                "distance": distance,  # lower = more similar
            })

    return matched_reviews


# Optional: quick test when running the file directly
if __name__ == "__main__":
    test_query = "entrega demorou muito"
    results = retrieve_reviews(test_query, top_k=3)

    print(f"\nQuery: {test_query}")
    print("-" * 50)
    for i, r in enumerate(results, 1):
        print(f"{i}. Score: {r.get('review_score')} | Predicted: {r.get('predicted_stars')}")
        print(f"   Order: {r.get('order_id')}")
        print(f"   Review: {r.get('review')[:120]}...")
        print()
