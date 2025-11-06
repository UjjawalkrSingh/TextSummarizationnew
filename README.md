# 🧠 SummarifyX – AI-Powered YouTube & Website Summarizer

SummarifyX is an advanced **AI-powered, cloud-based text summarization system** designed to convert long-form **YouTube videos** and **web articles** into short, meaningful, and high-quality summaries.  

It leverages **Large Language Models (LLMs)** via **Groq's ultra-fast LPU-based inference**, along with **LangChain**, **Streamlit**, and **BeautifulSoup** to provide instant, accurate, and structured summaries — saving users valuable time and effort.

---

## 🚀 Features

- 🔗 Accepts both **YouTube URLs** and **website links**
- ⚡ Powered by **Groq's LPU-based "Llama-3.3-70B-Versatile"** model
- 🧩 Uses **LangChain** for intelligent summarization
- 🧠 Generates ~300-word **executive summaries**
- 🌐 Fast web content extraction using **BeautifulSoup**
- 💡 Clean and interactive **Streamlit UI**
- ☁️ Cloud-ready, scalable, and efficient

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

Follow these simple steps to install and run SummarifyX locally:

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/SummarifyX.git
cd SummarifyX
```

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

### 5️⃣ Get Your Groq API Key

- Visit [https://console.groq.com](https://console.groq.com)
- Sign in and generate your **Groq API Key**

### 6️⃣ Create a `.env` File

In your project root, create a `.env` file:

```bash
touch .env
```

### 7️⃣ Add Your API Key to `.env`

```bash
GROQ_API_KEY=your_groq_api_key_here
```

### 8️⃣ Run the Streamlit App

```bash
streamlit run app.py
```

### 9️⃣ Open in Browser

After launching, Streamlit will provide a local URL (e.g., `http://localhost:8501`).  
Open it in your browser.

### 🔟 Enter Your URL & Summarize

- Enter your **Groq API key** in the sidebar (optional if stored in `.env`)
- Paste any **YouTube** or **website** URL
- Click **"Summarize the Content"**
- 🎉 Get your AI-generated summary instantly!

---

## 🧩 Example Use Case

| Input                     | Output                      |
| ------------------------- | --------------------------- |
| YouTube Lecture (45 mins) | 300-word structured summary |
| Research Blog (5 pages)   | Executive overview          |
| Corporate Article         | Bullet-style key insights   |

---

## 🧠 How It Works (Behind the Scenes)

1. Detects if the URL is a **YouTube video** or a **website**
2. Loads data via **LangChain's YouTubeLoader** or **BeautifulSoup scraper**
3. Converts text into LangChain **Document objects**
4. Uses **Groq's Llama-3.3-70B-Versatile** model for summarization
5. Applies a **custom summarization prompt template**
6. Displays a concise, 300-word summary instantly

---

## 📈 Benefits

- Saves time for **students, researchers, and professionals**
- Reduces information overload
- Enhances **productivity** and **decision-making**
- Enables quick content understanding from **any public link**

---

## 🛠️ Project Structure

```
SummarifyX/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (API keys)
├── .gitignore            # Git ignore file
├── README.md             # Project documentation
└── LICENSE               # MIT License
```

---

## 📦 Requirements

Create a `requirements.txt` file with the following dependencies:

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

## 🔒 Security Note

- Never commit your `.env` file to version control
- Add `.env` to your `.gitignore` file
- Keep your Groq API key confidential

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📧 Contact

For questions or suggestions, please open an issue on GitHub.

---

## 📄 License

This project is licensed under the **MIT License**.  
See [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgments

- **Groq** for providing ultra-fast LLM inference
- **LangChain** for simplifying LLM application development
- **Streamlit** for the intuitive web framework
- **OpenAI** for advancing AI research

---

## 🔮 Future Enhancements

- 📝 Support for PDF document summarization
- 🎯 Multi-language support
- 📊 Summary quality scoring
- 💾 Save and export summaries
- 🔄 Batch processing multiple URLs
- 📱 Mobile-responsive design improvements

---

> ⚡ **SummarifyX** — Making long-form content short, smart, and simple!

---

**⭐ If you find this project helpful, please give it a star on GitHub!**