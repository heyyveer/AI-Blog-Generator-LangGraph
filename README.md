# 📝 AI Blog Generator using LangGraph

An intelligent **multi-agent AI blog generation system** built using **LangGraph**, **LangChain**, **Groq LLM**, and **Streamlit**.

Unlike traditional AI blog generators, this project follows a **production-style content creation workflow** where each stage is reviewed by a human before moving forward.

---

# 🚀 Features

✅ Multi-Agent Workflow

- Content Planner
- Research Agent
- Outline Generator
- Blog Writer
- Content Editor

---

## 🧑‍💻 Human-in-the-Loop (HITL)

After every major stage, users can:

- ✅ Approve
- ❌ Reject
- 💬 Provide feedback

Rejected content is regenerated using reviewer feedback before continuing.

---

## 🔄 Workflow

```text
Topic
   │
Planner
   │
Research
   │
Human Review
   │
Outline
   │
Human Review
   │
Writer
   │
Human Review
   │
Editor
   │
Final Blog
```

---

# 🏗️ Tech Stack

- Python
- LangGraph
- LangChain
- ChatGroq
- Streamlit
- TypedDict State
- MemorySaver
- Human-in-the-Loop

---

# 📂 Project Structure

```text
AI-Blog-Generator-LangGraph/

│── app.py
│── graph.py
│── agents.py
│── prompts.py
│── state.py
│── requirements.txt
│── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/AI-Blog-Generator-LangGraph.git
```

Move into the project

```bash
cd AI-Blog-Generator-LangGraph
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```text
GROQ_API_KEY=your_api_key
```

Run the application

```bash
streamlit run app.py
```

---

# 🎯 How It Works

### Step 1

Provide:

- Blog Topic
- Target Audience
- Writing Tone
- Keywords

---

### Step 2

Planner Agent creates a research strategy.

---

### Step 3

Research Agent gathers information.

---

### Step 4

Human reviews the research.

- Approve
- Reject with feedback

---

### Step 5

Outline Agent creates the blog structure.

---

### Step 6

Human reviews the outline.

---

### Step 7

Writer Agent generates the complete blog.

---

### Step 8

Human reviews the draft.

---

### Step 9

Editor Agent polishes the content.

---

# 📸 Screenshots

Add screenshots here

```
Home Page

Research Review

Outline Review

Draft Review

Final Blog
```

---

# 🌟 Future Improvements

- Web Search Integration
- Citation Support
- SEO Score
- Grammar Score
- Export to PDF
- Export to DOCX
- Multi-language Blog Generation
- AI Image Generation
- Blog Publishing API

---

# 🤝 Contributing

Contributions are welcome.

Fork the repository and submit a pull request.

---

# 📜 License

MIT License

---

# 👨‍💻 Author

**Veer Tiwari**

Machine Learning & Generative AI Enthusiast

- GitHub: https://github.com/yourusername
- LinkedIn: https://linkedin.com/in/yourprofile
