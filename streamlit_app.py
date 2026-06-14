import streamlit as st

from qa import ask_repo
from repo_loader import clone_repo, load_files
from chunker import create_chunks
from embedder import get_embeddings
from vector_store import build_vectorstore

st.set_page_config(
    page_title="CodeSense AI",
    page_icon="🚀",
    layout="wide"
)

# Session State
if "repo_loaded" not in st.session_state:
    st.session_state.repo_loaded = False

if "messages" not in st.session_state:
    st.session_state.messages = []

# Header
st.title("CodeSense AI")
st.caption("Chat with any GitHub repository")

# Sidebar
with st.sidebar:

    st.header("Repository Setup")

    repo_url = st.text_input(
        "GitHub Repository URL"
    )

    if st.button("Load Repository"):

        try:

            with st.spinner(
                "Cloning and indexing repository..."
            ):

                clone_repo(repo_url)

                docs = load_files(
                    "repos/project"
                )

                chunks = create_chunks(
                    docs
                )

                embeddings = get_embeddings()

                build_vectorstore(
                    chunks,
                    embeddings
                )

                st.session_state.repo_loaded = True
                st.session_state.docs_count = len(docs)
                st.session_state.chunks_count = len(chunks)

            st.success(
                "Repository loaded!"
            )

        except Exception as e:

            st.error(str(e))

    if st.session_state.repo_loaded:

        st.divider()

        st.metric(
            "Files",
            st.session_state.docs_count
        )

        st.metric(
            "Chunks",
            st.session_state.chunks_count
        )

# Main Chat Area

if not st.session_state.repo_loaded:

    st.info(
        "Load a GitHub repository from the sidebar to begin."
    )

else:

    # Suggested Questions

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📖 Explain Project"):
            prompt = "Explain this repository"

            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": prompt
                }
            )

            result = ask_repo(prompt)

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": result["answer"],
                    "sources": result["sources"]
                }
            )

            st.rerun()

    with col2:
        if st.button("🏗 Architecture"):
            prompt = "Explain the architecture of this repository"

            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": prompt
                }
            )

            result = ask_repo(prompt)

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": result["answer"],
                    "sources": result["sources"]
                }
            )

            st.rerun()

    with col3:
        if st.button("🛠 Technologies"):
            prompt = "What technologies and libraries are used?"

            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": prompt
                }
            )

            result = ask_repo(prompt)

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": result["answer"],
                    "sources": result["sources"]
                }
            )

            st.rerun()

    # Display Chat History

    for message in st.session_state.messages:

        with st.chat_message(
            message["role"]
        ):

            st.markdown(
                message["content"]
            )

            if "sources" in message:

                with st.expander(
                    "Sources"
                ):

                    for source in message["sources"]:
                        st.code(source)

    # User Input

    user_question = st.chat_input(
        "Ask about the repository..."
    )

    if user_question:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": user_question
            }
        )

        with st.chat_message("user"):
            st.markdown(user_question)

        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                result = ask_repo(
                    user_question
                )

                st.markdown(
                    result["answer"]
                )

                with st.expander(
                    "Sources"
                ):

                    for source in result["sources"]:
                        st.code(source)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": result["answer"],
                "sources": result["sources"]
            }
        )