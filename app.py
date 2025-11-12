import streamlit as st
from langchain_groq import ChatGroq
from langchain.chains import LLMChain
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.prompts import PromptTemplate
from langchain.agents import Tool, initialize_agent
from langchain.agents.agent_types import AgentType
from langchain.callbacks import StreamlitCallbackHandler
import re
import math

# -------------------------------
# STREAMLIT APP CONFIGURATION
# -------------------------------
st.set_page_config(
    page_title="SmartMath: AI Math Solver & Knowledge Assistant",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 SmartMath: AI Math Solver & Knowledge Assistant")
st.write(
    "Welcome to **SmartMath**, your intelligent assistant for solving mathematical problems, "
    "performing logical reasoning, and fetching real-time knowledge from Wikipedia."
)

# -------------------------------
# SIDEBAR - API KEY INPUT
# -------------------------------
groq_api_key = st.sidebar.text_input(label="🔑 Enter Groq API Key", type="password")

if not groq_api_key:
    st.info("Please add your Groq API key in the sidebar to continue.")
    st.stop()

# -------------------------------
# INITIALIZE LLM AND TOOLS
# -------------------------------
llm = ChatGroq(model="llama-3.3-70b-versatile", groq_api_key=groq_api_key)

# --- Wikipedia Tool ---
wikipedia_wrapper = WikipediaAPIWrapper()
wikipedia_tool = Tool(
    name="Wikipedia",
    func=wikipedia_wrapper.run,
    description="Fetch information and context about general knowledge topics."
)

# --- Safe Python Math Evaluator ---
def safe_math_solver(expression):
    """
    Safely evaluates basic mathematical expressions using Python's eval
    with restricted builtins for security.
    """
    try:
        # Sanitize expression – allow only digits, operators, and parentheses
        expression = re.sub(r"[^0-9+\-*/().]", "", expression)
        result = eval(expression, {"__builtins__": None, "math": math})
        return f"Answer: {result}"
    except Exception as e:
        return f"Error: Invalid expression ({str(e)})"

calculator = Tool(
    name="Calculator",
    func=safe_math_solver,
    description="Safely evaluates mathematical expressions using Python."
)

# --- Logical Reasoning Tool ---
prompt = """
You are a reasoning agent tasked with solving mathematical or logical questions. 
Think step-by-step, explain your reasoning clearly, and present the final answer with bullet points.

Question: {question}
Answer:
"""

prompt_template = PromptTemplate(
    input_variables=["question"],
    template=prompt
)

reasoning_chain = LLMChain(llm=llm, prompt=prompt_template)
reasoning_tool = Tool(
    name="Reasoning Tool",
    func=reasoning_chain.run,
    description="Handles complex logical or reasoning-based mathematical problems."
)

# -------------------------------
# INITIALIZE THE AGENT
# -------------------------------
assistant_agent = initialize_agent(
    tools=[wikipedia_tool, calculator, reasoning_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    handle_parsing_errors=True
)

# -------------------------------
# CHAT HISTORY SETUP
# -------------------------------
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi 👋, I'm SmartMath! I can solve math problems, reasoning tasks, and fetch knowledge for you."}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# -------------------------------
# MAIN INPUT AREA
# -------------------------------
question = st.text_area(
    "📘 Enter your question below:",
    "I have 5 bananas and 7 grapes. I eat 2 bananas and give away 3 grapes. Then I buy a dozen apples and 2 packs of blueberries. Each pack has 25 berries. How many total fruits do I have now?"
)

# -------------------------------
# PROCESS USER INPUT
# -------------------------------
if st.button("🧮 Solve My Problem"):
    if question.strip():
        with st.spinner("Thinking and solving..."):
            st.session_state.messages.append({"role": "user", "content": question})
            st.chat_message("user").write(question)

            st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)

            try:
                # Ask the agent to solve
                response = assistant_agent.run(question, callbacks=[st_cb])
            except Exception as e:
                response = f"⚠️ An error occurred while processing: {str(e)}"

            st.session_state.messages.append({"role": "assistant", "content": response})
            st.write("### 🧾 SmartMath Response:")
            st.success(response)
    else:
        st.warning("Please enter a question to solve.")
