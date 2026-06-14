from langchain_chroma import Chroma
from langchain_core.documents import Document

def build_vectorstore(chunks, embeddings):

    docs = []

    for chunk in chunks:

        docs.append(
            Document(
                page_content=chunk["content"],
                metadata={
                    "source": chunk["filename"]
                }
            )
        )

    db = Chroma.from_documents(
        docs,
        embeddings,
        persist_directory="vectorstore"
    )

    return db