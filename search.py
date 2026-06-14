from embedder import get_embeddings
from langchain_chroma import Chroma

def search_repo(query):

    embeddings = get_embeddings()

    db = Chroma(
        persist_directory="vectorstore",
        embedding_function=embeddings
    )

    results = db.similarity_search(
        query,
        k=7
    )

    return results