from langchain_text_splitters import RecursiveCharacterTextSplitter

def create_chunks(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = []

    for doc in documents:

        split_texts = splitter.split_text(
            doc["content"]
        )

        for text in split_texts:

            chunks.append({
                "filename": doc["filename"],
                "content": text
            })

    return chunks