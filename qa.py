from search import search_repo
from llm import get_llm


def ask_repo(question):

    results = search_repo(question)

    context = "\n\n".join(
        [
            f"FILE: {doc.metadata['source']}\n{doc.page_content}"
            for doc in results
        ]
    )

    sources = list(
        set(
            doc.metadata.get("source", "Unknown")
            for doc in results
        )
    )

    prompt = f"""
You are an expert software engineer.

Answer the user's question using ONLY the repository context provided.

If the answer cannot be found in the context, say:
"I couldn't find enough information in the repository."

Repository Context:
{context}

Question:
{question}
"""

    llm = get_llm()

    response = llm.invoke(prompt)

    return {
        "answer": response.content,
        "sources": sources
    }