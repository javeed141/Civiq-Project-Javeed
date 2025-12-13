# # import streamlit as st
# # import os
# # import time
# # from dotenv import load_dotenv

# # from langchain_groq import ChatGroq
# # from langchain_text_splitters import RecursiveCharacterTextSplitter
# # from langchain_core.prompts import ChatPromptTemplate
# # from langchain_community.document_loaders import PyPDFLoader

# # from langchain_community.document_loaders import PyPDFDirectoryLoader
# # from langchain_community.vectorstores import FAISS
# # from langchain_google_genai import GoogleGenerativeAIEmbeddings

# # # ---------------- ENV ----------------
# # load_dotenv()
# # load_dotenv(dotenv_path=".env", override=True)
# # print("GOOGLE_API_KEY =", os.getenv("GOOGLE_API_KEY"))

# # os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
# # groq_api_key = os.getenv("GROQ_API_KEY")

# # # ---------------- UI ----------------
# # st.title("📄 Document Q&A (LangChain 2025 Safe)")

# # # ---------------- LLM ----------------
# # llm = ChatGroq(
# #     groq_api_key=groq_api_key,
# #     model_name="Llama3-8b-8192"
# # )

# # # ---------------- PROMPT ----------------
# # prompt = ChatPromptTemplate.from_template(
# #     """
# # Answer the question using ONLY the context below.
# # If the answer is not present, say "I don't know".

# # Context:
# # {context}

# # Question:
# # {question}
# # """
# # )

# # # ---------------- VECTOR EMBEDDING ----------------
# # def vector_embedding():
# #     if "vectors" not in st.session_state:
# #         embeddings = GoogleGenerativeAIEmbeddings(
# #             model="models/embedding-001"
# #         )

# #         loader = PyPDFLoader("Javeed_Resume.pdf")  # ✅ single PDF
# #         docs = loader.load()

# #         if not docs:
# #             st.error("❌ No documents loaded. Check PDF path.")
# #             return

# #         splitter = RecursiveCharacterTextSplitter(
# #             chunk_size=1000,
# #             chunk_overlap=200
# #         )

# #         final_docs = splitter.split_documents(docs)

# #         if not final_docs:
# #             st.error("❌ No chunks created from document.")
# #             return

# #         st.session_state.vectors = FAISS.from_documents(
# #             final_docs,
# #             embeddings
# #         )

# # # ---------------- INPUT ----------------
# # query = st.text_input("Enter your question")

# # if st.button("Documents Embedding"):
# #     vector_embedding()
# #     st.success("✅ Vector store created")

# # # ---------------- QA ----------------
# # if query:
# #     if "vectors" not in st.session_state:
# #         st.warning("⚠️ Please embed documents first")
# #     else:
# #         retriever = st.session_state.vectors.as_retriever(search_kwargs={"k": 4})

# #         docs = retriever.invoke(query)
# #         context = "\n\n".join(doc.page_content for doc in docs)

# #         start = time.process_time()
# #         response = llm.invoke(
# #             prompt.format_messages(
# #                 context=context,
# #                 question=query
# #             )
# #         )

# #         st.write(f"⏱ Response time: {time.process_time() - start:.2f}s")
# #         st.write("### Answer")
# #         st.write(response.content)

# #         with st.expander("📌 Retrieved Chunks"):
# #             for doc in docs:
# #                 st.write(doc.page_content)
# #                 st.write("----")
# import streamlit as st
# import os
# import time
# from dotenv import load_dotenv

# from langchain_groq import ChatGroq
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_core.prompts import ChatPromptTemplate

# from langchain_community.document_loaders import PyPDFDirectoryLoader
# from langchain_community.vectorstores import FAISS
# from langchain_mistralai import MistralAIEmbeddings

# # ---------------- ENV ----------------
# load_dotenv()

# groq_api_key = os.getenv("GROQ_API_KEY")
# mistral_api_key = os.getenv("MISTRAL_API_KEY")

# DATA_DIR = "../GEMMA/docs"
# FAISS_DIR = "faiss_index"

# # ---------------- UI ----------------
# st.title("📂 Multi-Document Q&A (Mistral + FAISS)")

# # ---------------- LLM ----------------
# llm = ChatGroq(
#     groq_api_key=groq_api_key,
#     model_name="llama-3.1-8b-instant"
# )

# # ---------------- PROMPT ----------------
# prompt = ChatPromptTemplate.from_template(
#     """
# Answer the question using ONLY the context below.
# If the answer is not present, say "I don't know".

# Context:
# {context}

# Question:
# {question}
# """
# )

# # ---------------- VECTOR STORE ----------------
# def load_or_create_vectors():
#     embeddings = MistralAIEmbeddings(
#         model="mistral-embed",
#         api_key=mistral_api_key
#     )

#     # Load existing vectors if present
#     if os.path.exists(FAISS_DIR):
#         return FAISS.load_local(
#             FAISS_DIR,
#             embeddings,
#             allow_dangerous_deserialization=True
#         )

#     # Load all PDFs from folder
#     loader = PyPDFDirectoryLoader(DATA_DIR)
#     documents = loader.load()

#     if not documents:
#         st.error("❌ No PDF files found in data folder")
#         st.stop()

#     splitter = RecursiveCharacterTextSplitter(
#         chunk_size=1000,
#         chunk_overlap=200
#     )

#     chunks = splitter.split_documents(documents)

#     vectorstore = FAISS.from_documents(chunks, embeddings)

#     # Save vectors to disk
#     vectorstore.save_local(FAISS_DIR)

#     return vectorstore

# # ---------------- INPUT ----------------
# query = st.text_input("Ask a question about the documents")

# if st.button("Create / Load Embeddings"):
#     st.session_state.vectors = load_or_create_vectors()
#     st.success("✅ Vector store ready")

# # ---------------- QA ----------------
# if query:
#     if "vectors" not in st.session_state:
#         st.warning("⚠️ Please create/load embeddings first")
#     else:
#         retriever = st.session_state.vectors.as_retriever(search_kwargs={"k": 4})
#         docs = retriever.invoke(query)

#         context = "\n\n".join(doc.page_content for doc in docs)

#         response = llm.invoke(
#             prompt.format_messages(
#                 context=context,
#                 question=query
#             )
#         )

#         st.write("### Answer")
#         st.write(response.content)

#         with st.expander("📌 Source Chunks"):
#             for doc in docs:
#                 st.write(f"**Source:** {doc.metadata.get('source')}")
#                 st.write(doc.page_content)
#                 st.write("----")
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_community.vectorstores import FAISS
from langchain_mistralai import MistralAIEmbeddings

# ---------------- ENV ----------------
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

DATA_DIR = "../GEMMA/docs"
FAISS_DIR = "faiss_index"

# ---------------- APP ----------------
app = Flask(__name__)
CORS(app)

# ---------------- LLM ----------------
llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="llama-3.1-8b-instant"
)

# ---------------- PROMPT ----------------
prompt = ChatPromptTemplate.from_template(
    """
You are a CivicQ assistant.

Rules:
- Use ONLY the context provided below.
- If exact information is missing, say "I don't know".

Context:
{context}

Question:
{question}
"""
)

# ---------------- VECTOR STORE (STATIC KNOWLEDGE) ----------------
def load_or_create_vectors():
    embeddings = MistralAIEmbeddings(
        model="mistral-embed",
        api_key=MISTRAL_API_KEY
    )

    if os.path.exists(FAISS_DIR):
        return FAISS.load_local(
            FAISS_DIR,
            embeddings,
            allow_dangerous_deserialization=True
        )

    loader = PyPDFDirectoryLoader(DATA_DIR)
    documents = loader.load()

    if not documents:
        raise RuntimeError("No PDFs found in DATA_DIR")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documents)
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(FAISS_DIR)

    return vectorstore


vectorstore = load_or_create_vectors()
retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

# ---------------- USER DATA → TEXT (NO VECTORS) ----------------
def format_user_data(user_data: dict) -> str:
    if not user_data:
        return "No user-specific issue data available."

    issues = user_data.get("issues", [])

    if not issues:
        return "User has not raised any issues."

    text = f"User has raised {len(issues)} issues.\n"

    for idx, issue in enumerate(issues, start=1):
        text += (
            f"Issue {idx}: {issue.get('title')} | "
            f"Location: {issue.get('location')} | "
            f"Status: {issue.get('status')} | "
            f"Created: {issue.get('createdAt')}\n"
        )

    last_issue = issues[-1]
    text += (
        f"\nLast raised issue: {last_issue.get('title')} "
        f"at {last_issue.get('location')} "
        f"with status {last_issue.get('status')}."
    )

    return text


# ---------------- API ROUTE ----------------
@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.get_json(force=True)

        messages = data.get("messages")
        user_data = data.get("userData")

        if not messages:
            return jsonify({"error": "messages missing"}), 400

        # last user message
        last_user_message = next(
            (m["content"] for m in reversed(messages) if m["role"] == "user"),
            None
        )

        if not last_user_message:
            return jsonify({"error": "no user message"}), 400

        # -------- USER CONTEXT (EXACT FACTS) --------
        user_context = format_user_data(user_data)

        # -------- RAG CONTEXT (APP KNOWLEDGE) --------
        docs = retriever.invoke(last_user_message)
        rag_context = "\n\n".join(doc.page_content for doc in docs)

        # -------- FINAL CONTEXT --------
        final_context = f"""
            User Issue Data:
            {user_context}

            Application Knowledge:
            {rag_context}
            """

        response = llm.invoke(
            prompt.format_messages(
                context=final_context,
                question=last_user_message
            )
        )

        return jsonify({"answer": response.content})

    except Exception as e:
        print("🔥 BACKEND ERROR:", e)
        return jsonify({"error": str(e)}), 500


# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
