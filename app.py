import os
import validators
import streamlit as st
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.document_loaders import YoutubeLoader
from langchain_core.documents import Document


# ------------------------- Load Environment Variables -------------------------
load_dotenv()
default_groq_api_key = os.getenv("GROQ_API_KEY", "")


# ------------------------- Streamlit App UI -------------------------
st.set_page_config(page_title="LangChain: Summarize Text From YT or Website", page_icon="🦜")
st.title("🦜 LangChain: Summarize Text From YT or Website")
st.markdown("### Kindly Enter Your Groq API Key Below to Start Summarization")
st.subheader("Summarize from URL (YouTube or Website)")


# ------------------------- Sidebar Input -------------------------
with st.sidebar:
    groq_api_key = st.text_input("Groq API Key", value=default_groq_api_key, type="password")

generic_url = st.text_input("Enter a URL to summarize", label_visibility="collapsed")


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
if st.button("Summarize the Content from YT or Website"):
    if not groq_api_key.strip() or not generic_url.strip():
        st.error("⚠️ Please provide both the Groq API Key and a valid URL.")
    elif not validators.url(generic_url):
        st.error("⚠️ Please enter a valid URL. It can be a YouTube video or a website link.")
    else:
        try:
            with st.spinner("⏳ Processing... Please wait..."):

                # Load content from YouTube or Website
                if "youtube.com" in generic_url or "youtu.be" in generic_url:
                    loader = YoutubeLoader.from_youtube_url(generic_url, add_video_info=True)
                    docs = loader.load()
                else:
                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
                    response = requests.get(generic_url, headers=headers, timeout=10)
                    soup = BeautifulSoup(response.text, "html.parser")
                    paragraphs = [p.get_text(strip=True) for p in soup.find_all("p") if p.get_text(strip=True)]
                    page_text = "\n".join(paragraphs)
                    docs = [Document(page_content=page_text)]

                if not docs or not docs[0].page_content.strip():
                    st.warning("⚠️ No readable text content found at this URL.")
                else:
                    # Create summarization chain
                    document_chain = create_stuff_documents_chain(llm, prompt)

                    # Run the summarization chain
                    result = document_chain.invoke({"context": docs})

                    # Handle output
                    summary_text = result.get("output_text") if isinstance(result, dict) else result

                    st.success("✅ Summary Generated Successfully!")
                    st.write(summary_text)

        except Exception as e:
            st.error(f"❌ Exception Occurred: {e}")


# ------------------------- Footer -------------------------
st.markdown("---")
st.markdown(
    "<p style='text-align: center;'>Built with ❤️ by <b>Ujjwal Sinha</b> • "
    "<a href='https://github.com/Ujjwal-sinha' target='_blank'>GitHub</a></p>",
    unsafe_allow_html=True
)
