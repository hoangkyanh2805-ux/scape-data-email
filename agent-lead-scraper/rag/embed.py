"""
Semantic embedding helpers for actor configurations and source queries.

OpenAI is optional at import time so local mock runs can execute without the
embedding dependency installed. Calls to embed functions still require the
package and OPENAI_API_KEY.
"""

import os
from typing import List

try:
    from openai import OpenAI
except ImportError:  # pragma: no cover - depends on local environment
    OpenAI = None


def _client():
    if OpenAI is None:
        raise RuntimeError("openai package not installed; install requirements to enable RAG embeddings")

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not set")
    return OpenAI(api_key=api_key)


def embed(text: str) -> List[float]:
    """
    Generate semantic embedding for a single text.

    Args:
        text: Input text, such as a query or actor config description.

    Returns:
        Embedding vector.
    """
    if not text or len(text.strip()) == 0:
        raise ValueError("Text cannot be empty")

    try:
        response = _client().embeddings.create(
            input=text,
            model="text-embedding-3-small",
        )
        return response.data[0].embedding
    except Exception as e:
        raise RuntimeError(f"Embedding failed: {str(e)}")


def embed_batch(texts: List[str]) -> List[List[float]]:
    """
    Generate embeddings for multiple texts.

    Args:
        texts: List of texts to embed.

    Returns:
        List of embedding vectors in input order.
    """
    if not texts:
        raise ValueError("Texts list cannot be empty")

    try:
        response = _client().embeddings.create(
            input=texts,
            model="text-embedding-3-small",
        )
        embeddings = sorted(response.data, key=lambda x: x.index)
        return [emb.embedding for emb in embeddings]
    except Exception as e:
        raise RuntimeError(f"Batch embedding failed: {str(e)}")


if __name__ == "__main__":
    test_text = "Find public XAUUSD beginner questions in TikTok comments"
    emb = embed(test_text)
    print(f"Query: {test_text}")
    print(f"Embedding dimension: {len(emb)}")
    print(f"First 5 values: {emb[:5]}")
