
````markdown
# 🧠 SmartMath: AI Math Solver & Knowledge Assistant

**SmartMath** is an intelligent AI-powered assistant built with **LangChain**, **Groq LLMs**, and **Streamlit**.  
It combines **mathematical computation**, **logical reasoning**, and **real-time knowledge retrieval** from Wikipedia — all in one unified interface.

---

## 🚀 Key Features

- 🧮 **Mathematical Problem Solving**  
  Handles arithmetic, algebra, geometry, and advanced calculations using powerful LLM math reasoning.

- 🤖 **Logical Reasoning**  
  Explains answers step-by-step, making it ideal for problem-solving and conceptual understanding.

- 🌐 **Knowledge Assistant**  
  Fetches real-time information and summaries directly from **Wikipedia**.

- 💬 **Interactive Chat Interface**  
  Built with **Streamlit Chat UI**, enabling smooth, real-time AI conversations.

---

## 🧩 Tech Stack

- **Frontend:** Streamlit  
- **Backend:** LangChain  
- **Model Provider:** Groq (LLaMA 3.3 70B Versatile)  
- **Tools:** LangChain Agents, Wikipedia API, LLMMathChain  

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/SmartMath.git
cd SmartMath
````

### 2️⃣ Create and Activate a Virtual Environment

```bash
# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set Your Groq API Key

In the Streamlit sidebar, you’ll be prompted to enter your **Groq API Key**.
You can obtain it from [https://console.groq.com/](https://console.groq.com/).

Alternatively, you can set it as an environment variable:

```bash
export GROQ_API_KEY="your_api_key_here"
```

### 5️⃣ Run the Application

```bash
streamlit run app.py
```

---

## 🧠 How It Works

1. **User Input:**
   Enter a math or reasoning question in the text area.

2. **LLM Processing:**
   The Groq-powered LLaMA model processes your query using LangChain’s tools and reasoning chains.

3. **Tool Execution:**

   * The **Calculator Tool** handles mathematical operations.
   * The **Wikipedia Tool** retrieves external facts.
   * The **Reasoning Tool** applies step-by-step logic.

4. **Response Generation:**
   The agent intelligently selects the right tool(s) and presents a structured explanation and final answer.

---

## 🧾 Example Query

**Input:**

> I have 5 bananas and 7 grapes. I eat 2 bananas and give away 3 grapes. Then I buy a dozen apples and 2 packs of blueberries. Each pack has 25 berries. How many total fruits do I have now?

**Output:**

> 🍎 You have a total of **67 fruits** after all transactions.

---

## 📦 Example `requirements.txt`

```txt
streamlit
langchain
langchain-groq
langchain-community
wikipedia
```

---

## 💡 Future Enhancements

* Support for **symbolic algebra** and **graph plotting**
* Integration with **WolframAlpha** or **Google Search APIs**
* Multi-language reasoning capability

---

## 🛡️ License

This project is released for educational and research purposes.
All model usage must comply with the **Groq API Terms of Service** and **Wikipedia usage policies**.

---

```
