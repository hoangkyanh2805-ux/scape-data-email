"""
Semantic retrieval: cosine similarity plus top-k retrieval.

This module avoids hard runtime dependency on numpy so mock/local runs can work
before optional RAG dependencies are installed.
"""

import math
from typing import List, Tuple

try:
    import yaml
except ImportError:  # pragma: no cover - depends on local environment
    yaml = None


def cosine_similarity(a: List[float], b: List[float]) -> float:
    """Calculate cosine similarity between two vectors."""
    if len(a) != len(b):
        raise ValueError("Embedding vectors must have the same length")

    dot = sum(x * y for x, y in zip(a, b))
    a_norm = math.sqrt(sum(x * x for x in a)) + 1e-10
    b_norm = math.sqrt(sum(y * y for y in b)) + 1e-10
    return float(dot / (a_norm * b_norm))


def retrieve(
    query_embedding: List[float],
    stored_embeddings: List[Tuple[int, List[float]]],
    top_k: int = 20,
    min_similarity: float = 0.7,
) -> List[int]:
    """Retrieve top-k most similar embedding IDs."""
    if not stored_embeddings:
        raise ValueError("Stored embeddings cannot be empty")

    if len(query_embedding) == 0:
        raise ValueError("Query embedding cannot be empty")

    scores = []
    for item_id, embedding in stored_embeddings:
        sim = cosine_similarity(query_embedding, embedding)
        if sim >= min_similarity:
            scores.append((item_id, sim))

    scores.sort(key=lambda x: x[1], reverse=True)
    return [item_id for item_id, _ in scores[:top_k]]


def retrieve_with_scores(
    query_embedding: List[float],
    stored_embeddings: List[Tuple[int, List[float]]],
    top_k: int = 20,
    min_similarity: float = 0.7,
) -> List[Tuple[int, float]]:
    """Retrieve top-k results with similarity scores."""
    scores = []
    for item_id, embedding in stored_embeddings:
        sim = cosine_similarity(query_embedding, embedding)
        if sim >= min_similarity:
            scores.append((item_id, sim))

    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[:top_k]


def load_config(config_path: str = "config.yaml") -> dict:
    """Load retrieval config from YAML file, or return defaults."""
    defaults = {"top_k": 20, "min_similarity_score": 0.7}
    if yaml is None:
        return defaults

    try:
        with open(config_path, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
        return config.get("retrieval", {}) if config else defaults
    except FileNotFoundError:
        return defaults


if __name__ == "__main__":
    from embed import embed

    query = "Find public XAUUSD beginner questions in TikTok comments"
    query_emb = embed(query)

    samples = [
        (1, embed("Public TikTok comments about XAUUSD beginner questions")),
        (2, embed("YouTube Forex education comments with profile links")),
        (3, embed("Private group members requiring login")),
        (4, embed("Generic startup founder contact list")),
    ]

    results = retrieve_with_scores(query_emb, samples, top_k=2)
    print(f"Query: {query}")
    print("Top 2 results:")
    for item_id, score in results:
        print(f"  ID {item_id}: {score:.4f}")
