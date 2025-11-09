import os
import validators
import streamlit as st
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.document_loaders import (
    YoutubeLoader, PyPDFLoader, TextLoader, UnstructuredWordDocumentLoader
)
from langchain_core.documents import Document

# ------------------------- Load Environment Variables -------------------------
load_dotenv()
default_groq_api_key = os.getenv("GROQ_API_KEY", "")

# ------------------------- Streamlit App Setup -------------------------
st.set_page_config(page_title="CloudFile Reader", page_icon="🧠", layout="centered")
st.title("🧠 CloudFile Reader– YouTube, Website, or File")
st.markdown("### Quickly summarize long content using **Groq + LangChain** ⚡")

# Sidebar
with st.sidebar:
    groq_api_key = st.text_input("🔑 Enter your Groq API Key", value=default_groq_api_key, type="password")
    st.markdown("---")
    st.caption("💡 Tip: You can get your API key from [groq.com](https://console.groq.com)")

# Input Method
option = st.radio("Select input type:", ["YouTube / Website URL", "Upload a File"], horizontal=True)
generic_url, uploaded_file = None, None

if option == "YouTube / Website URL":
    generic_url = st.text_input("Enter a URL to summarize", placeholder="https://example.com or YouTube link")
else:
    uploaded_file = st.file_uploader("Upload a file (.txt, .pdf, .docx)", type=["txt", "pdf", "docx"])

# ------------------------- Model Setup -------------------------
if groq_api_key:
    llm = ChatGroq(model="llama-3.3-70b-versatile", groq_api_key=groq_api_key)
else:
    llm = None

# ------------------------- Prompt Template -------------------------
prompt_template = """
You are a professional summarization assistant.
Summarize the following content in about 300 words, capturing the main ideas clearly and concisely.

Content:
{context}
"""
prompt = PromptTemplate(template=prompt_template, input_variables=["context"])

# ------------------------- Summarization Logic -------------------------
if st.button("🚀 Summarize Content"):
    if not groq_api_key.strip():
        st.error("⚠️ Please provide your Groq API Key first.")
    else:
        try:
            with st.spinner("⏳ Processing... Please wait..."):
                docs = []

                # Case 1: URL Input (YouTube or Website)
                if option == "YouTube / Website URL":
                    if not generic_url or not validators.url(generic_url):
                        st.error("⚠️ Please enter a valid URL.")
                        st.stop()

                    if "youtube.com" in generic_url or "youtu.be" in generic_url:
                        loader = YoutubeLoader.from_youtube_url(generic_url, add_video_info=True)
                        docs = loader.load()
                    else:
                        headers = {"User-Agent": "Mozilla/5.0"}
                        response = requests.get(generic_url, headers=headers, timeout=10)
                        soup = BeautifulSoup(response.text, "html.parser")
                        paragraphs = [p.get_text(strip=True) for p in soup.find_all("p") if p.get_text(strip=True)]
                        page_text = "\n".join(paragraphs)
                        docs = [Document(page_content=page_text)]

                # Case 2: File Upload
                elif uploaded_file is not None:
                    file_name = uploaded_file.name.lower()
                    temp_path = f"./temp_{uploaded_file.name}"
                    with open(temp_path, "wb") as f:
                        f.write(uploaded_file.read())

                    if file_name.endswith(".pdf"):
                        loader = PyPDFLoader(temp_path)
                    elif file_name.endswith(".txt"):
                        loader = TextLoader(temp_path)
                    elif file_name.endswith(".docx"):
                        loader = UnstructuredWordDocumentLoader(temp_path)
                    else:
                        st.error("⚠️ Unsupported file format.")
                        st.stop()

                    docs = loader.load()
                    os.remove(temp_path)

                if not docs or not docs[0].page_content.strip():
                    st.warning("⚠️ No readable text content found.")
                else:
                    # Create summarization chain
                    document_chain = create_stuff_documents_chain(llm, prompt)

                    # Run summarization
                    result = document_chain.invoke({"context": docs})
                    summary_text = result.get("output_text") if isinstance(result, dict) else result

                    # Display Summary
                    st.success("✅ Summary Generated Successfully!")
                    st.write(summary_text)

                    # Download option
                    st.download_button(
                        label="📥 Download Summary as TXT",
                        data=summary_text,
                        file_name="summary.txt",
                        mime="text/plain"
                    )

                    st.code(summary_text, language="markdown")
                    st.info("💡 You can copy or download the summary above!")

        except Exception as e:
            st.error(f"❌ Exception Occurred: {e}")
