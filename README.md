
# ☁️ CloudFile Reader – AI-Powered Content Summarization System

**CloudFile Reader** is an advanced **AI-driven, cloud-based summarization engine** that transforms long-form **YouTube videos**, **web articles**, and **uploaded documents** into short, structured, and meaningful summaries.  

Built using **Groq’s LPU-powered inference**, **LangChain**, and **Streamlit**, it delivers ultra-fast, accurate, and context-aware summaries — enabling users to consume vast information effortlessly.

---

## 🚀 Key Features

- 🔗 Supports both **YouTube URLs** and **web links**
- 📄 Upload and summarize **text**, **PDF**, and **Word** files
- ⚡ Powered by **Groq’s Llama-3.3-70B-Versatile** model
- 🧠 Produces precise **300-word executive summaries**
- 🌐 Intelligent web scraping with **BeautifulSoup**
- 💡 Modern and interactive **Streamlit interface**
- ☁️ Fully cloud-ready and scalable for enterprise usage

---

## 🧰 Tech Stack

- **Python 3.10+**
- **LangChain**
- **Groq API**
- **BeautifulSoup (bs4)**
- **Streamlit**
- **Requests**
- **dotenv**

---

## ⚙️ Installation & Setup

Follow these steps to run **CloudFile Reader** locally:

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/CloudFileReader.git
cd CloudFileReader
````

### 2️⃣ Create a Virtual Environment

```bash
python3 -m venv venv
```

### 3️⃣ Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Obtain Your Groq API Key

* Visit [https://console.groq.com](https://console.groq.com)
* Sign in and create your **Groq API Key**

### 6️⃣ Create a `.env` File

```bash
touch .env
```

### 7️⃣ Add Your API Key to `.env`

```bash
GROQ_API_KEY=your_groq_api_key_here
```

### 8️⃣ Run the Streamlit Application

```bash
streamlit run app.py
```

### 9️⃣ Open in Your Browser

Streamlit will launch a local server (e.g., `http://localhost:8501`).
Open this in your browser to start summarizing instantly!

---

## 🧩 Example Use Cases

| Input Type               | Output Summary Type         |
| ------------------------ | --------------------------- |
| YouTube Lecture (1 hour) | 300-word executive overview |
| Web Article (5 pages)    | Bullet-style key summary    |
| Research PDF             | Condensed structured report |

---

## 🧠 How It Works

1. Detects whether the input is a **YouTube**, **website**, or **uploaded file**
2. Loads data using **LangChain’s loaders** or **BeautifulSoup**
3. Converts text into **LangChain Document objects**
4. Summarizes using **Groq’s Llama-3.3-70B-Versatile** model
5. Applies a custom-built summarization **PromptTemplate**
6. Displays a 300-word summary via Streamlit UI

---

## 📈 Benefits

* ⏱️ Saves hours of reading or watching time
* 🧩 Provides quick understanding for decision-making
* 📚 Ideal for **students, researchers, analysts, and professionals**
* 🌎 Summarizes any public content link efficiently

---

## 🗂️ Project Structure

```
CloudFileReader/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (API keys)
├── .gitignore             # Git ignore file
├── README.md              # Project documentation
└── LICENSE                # MIT License
```

---

## 📦 Requirements

Create a `requirements.txt` file containing:

```txt
streamlit
langchain
langchain-groq
langchain-community
beautifulsoup4
requests
python-dotenv
youtube-transcript-api
```

---

## 🔒 Security Best Practices

* Never share your `.env` file publicly
* Add `.env` to `.gitignore`
* Keep all API keys confidential

---

## 🤝 Contributing

Contributions are highly welcome! To contribute:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to your branch (`git push origin feature/new-feature`)
5. Open a Pull Request

---

## 📧 Contact

For questions, feedback, or suggestions — open an **issue** on GitHub.

---

## 📄 License

This project is licensed under the **MIT License**.
See [LICENSE](LICENSE) for full details.

---

## 🙏 Acknowledgments

* **Groq** – for blazing-fast LPU inference
* **LangChain** – for modular LLM integration
* **Streamlit** – for seamless web UI creation
* **BeautifulSoup** – for powerful HTML parsing

---

## 🔮 Future Enhancements

* 📝 Advanced PDF summarization
* 🌐 Multi-language support
* 📊 Smart summary scoring metrics
* 💾 Save/export summaries to cloud storage
* 🔄 Batch URL processing
* 📱 Enhanced mobile-responsive UI

---

> ☁️ **CloudFile Reader** — Transforming information overload into clear insight, one summary at a time.
