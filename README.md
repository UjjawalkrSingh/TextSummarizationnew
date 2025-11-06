# SummarifyX — AI-Powered Text Summarization from YouTube & Websites

**SummarifyX** is an advanced **AI-powered cloud-based summarization system** that converts long-form YouTube videos and website articles into short, meaningful, and high-value summaries.

It leverages **Large Language Models (LLMs)**, **LangChain**, and **Groq’s ultra-fast LPU infrastructure** to provide **instant, human-like summaries** — helping users digest massive information in seconds.

---

## Key Features

- **URL-Based Input** — Paste any **YouTube video link** or **website URL**.  
- **Automatic Content Extraction** — Fetches YouTube transcripts or scrapes web article text using **BeautifulSoup**.  
- **Groq-Powered Summarization** — Uses **Llama-3.3-70B-Versatile** model for blazing-fast and contextually rich summaries.  
- **LangChain Integration** — Streamlines the summarization chain and document management.  
- **Streamlit Interface** — Simple, intuitive, and responsive front-end for end users.  
- **Executive Summaries (~300 words)** — Clear, concise, and semantically rich summaries.  
- **Cloud-Optimized Efficiency** — Near-real-time inference via Groq’s **Language Processing Units (LPUs)**.  

---

## Tech Stack

| Component | Technology |
|------------|-------------|
| **Frontend / UI** | Streamlit |
| **LLM Interface** | LangChain |
| **Model Provider** | Groq API (`llama-3.3-70b-versatile`) |
| **Content Extraction** | BeautifulSoup (for web) + LangChain’s `YoutubeLoader` |
| **Backend Language** | Python 3.10+ |
| **Environment Management** | dotenv |
| **Validation** | validators |
| **HTTP Requests** | requests |

---

## System Architecture

```mermaid
graph TD
A[User Input URL + Groq API Key] --> B{Check URL Type}
B -->|YouTube| C[LangChain YoutubeLoader → Transcript]
B -->|Website| D[BeautifulSoup → Extract <p> Tags]
C --> E[LangChain Document Object]
D --> E
E --> F[Groq Llama-3.3-70B Model via LangChain Chain]
F --> G[AI Summarization (≈300 words)]
G --> H[Display Summary in Streamlit UI]

- Installation & Setup
1️. Clone the Repository
git clone https://github.com/UjjawalkrSingh/TextSummarization.git
cd TextSummarization

2️. Create and Activate Virtual Environment
python3 -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows

3️. install Dependencies
pip install -r requirements.txt

4️. Add Environment Variables
Create a .env file in the root directory:
GROQ_API_KEY=your_groq_api_key_here

 
 You can get your Groq API key from https://console.groq.com.


Usage
-Run the Application
streamlit run app.py

 In the Browser


Open the local Streamlit app (usually at http://localhost:8501)


Enter your Groq API Key


Paste any YouTube video URL or Website link


Click “Summarize the Content”

 - Example Use Cases


Summarize an entire YouTube lecture or podcast


Get quick takeaways from long research articles


Generate summaries for corporate reports or blogs


Use for academic revision, knowledge extraction, or content review



 Code Overview
SectionDescriptionLangChain + GroqIntegrates the Groq Llama-3.3-70B model for summarization.YoutubeLoaderFetches and parses YouTube transcripts automatically.BeautifulSoupExtracts readable paragraph text (<p>) from web pages.PromptTemplateCustom summarization prompt (≈300 words).Streamlit UIHandles user inputs and output visualization.
Summarization Flow


Validate URL and API key.


Detect source type (YouTube / Website).


Extract textual data.


Convert to LangChain Document format.


Apply summarization chain using Groq’s LLM.


Display structured summary in UI.



- Example Output
Input:

https://www.youtube.com/watch?v=dQw4w9WgXcQ

Output:

A concise, well-structured summary of the entire video transcript (~300 words), highlighting main ideas, arguments, and context.


 - Performance
MetricDescriptionSpeedNear real-time summarization due to Groq LPUs.ScalabilityEfficient handling of large text inputs.AccuracyContext-aware compression via Llama-3.3-70B.Ease of UseSingle-click summarization via Streamlit UI.

- Author
Developed by: Ujjawal Kr Singh
- AI Engineer | Cloud Developer | Data Science Enthusiast

 - License
This project is licensed under the MIT License — see the LICENSE file for details.

- Acknowledgements


LangChain — Framework for building LLM applications.


Groq — High-performance LPU infrastructure for AI inference.


Streamlit — Simplified app deployment for ML tools.


BeautifulSoup — Web scraping utilities.

“SummarifyX — Making knowledge faster, smarter, and simpler.”


