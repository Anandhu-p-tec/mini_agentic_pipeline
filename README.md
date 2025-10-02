# Mini Agentic Pipeline – AI Agent with Retrieval, Reasoning & Tool Execution

## 📌 Project Overview
This project implements a **Mini Agentic Pipeline**, an AI system capable of autonomously answering queries by:

1. Retrieving relevant context from a small knowledge base (`kb_docs/`).
2. Reasoning with **Gemini LLM** to decide the next action.
3. Executing an action via a tool (CSV lookup for prices).
4. Producing a final answer along with detailed logs for traceability.

The system demonstrates **agentic behavior**, deciding whether to rely on the KB or a tool based on the query.

## 🎥 Demo Video

[![Watch the demo](https://img.youtube.com/vi/rXxNusDsDOw/0.jpg)](https://youtu.be/rXxNusDsDOw)


---

## 🏗️ Architecture

**Pipeline Flow (ASCII View):**

```markdown
```mermaid
flowchart TD
    A([🧑 User Query]) --> B([⚡ Controller])
    B --> C([🔍 Retriever])
    C -->|Semantic Search in KB Docs (FAISS)| D([🧠 Reasoner - Gemini])
    
    D -->|Uses KB| E([📘 Final Answer from KB])
    D -->|Invokes Tool| F([🛠️ Actor - CSV Tool])
    
    F --> G([✅ Final Answer])
    E --> G
```
## 🔎 Components Explained

- **Controller:** Orchestrates the entire pipeline, handles queries, collects context, invokes the Reasoner and Actor, and logs all steps.
- **Retriever:** Searches KB documents in `kb_docs/` using **FAISS vector store** with embeddings for semantic retrieval.
- **Reasoner (Gemini):** Decides whether to answer using KB or invoke a tool (CSV). Uses modular prompts stored in `src/prompts/`.
- **Actor (CSV Tool):** Handles structured queries (prices). Reads `data/prices.csv` to fetch answers automatically.
- **Logs:** Stored in `logs/` to trace query handling, reasoning, and actions taken by the agent.

---

## 📂 Folder Structure
my-agentic-rag/
├─ kb_docs/ # Knowledge base documents
├─ data/ # CSV files (prices.csv)
├─ src/ # Source code
│ ├─ retriever.py
│ ├─ reasoner.py
│ ├─ actor_csv.py
│ ├─ controller.py
│ ├─ prompts/
│ │ ├─ prompt_v1.txt
│ │ └─ prompt_v2.txt
│ └─ utils.py
├─ logs/ # Execution logs
├─ tests/
│ └─ test_queries.py # Automated query tests
├─ demo_queries.txt # Queries for automated testing
├─ requirements.txt
├─ .env # Gemini API key and environment variables
├─ main.py # Interactive agent
└─ README.md


---

## ⚙️ Setup Instructions

1. **Clone or download the repo** to your local machine.

2. **Create a virtual environment** (recommended):

```bash
uv venv .venv
.venv\Scripts\activate       # Windows
source .venv/bin/activate    # Linux/macOS
```
3. Install dependencies:
```
pip install -r requirements.txt
```
4. Set up environment variables:
Create a .env file with your Gemini API key:
```
GEN_API_KEY=your_gemini_api_key_here
```
### 🚀 Usage
1. Interactive Mode
Run the agent and type queries manually:
```
python main.py
```
Example queries:

"What is the price of Apple?"

"Tell me about the company's history"

The agent decides whether to fetch from KB or CSV and returns the answer with step-by-step reasoning.

2. Automated Test Queries
   Run batch queries from demo_queries.txt:
   ```
   python -m tests.test_queries
   ```
Reads all queries automatically.

Prints reasoning and final answers in the terminal.

Saves detailed JSON logs in logs/, e.g., logs/run_20251002_123456.json.

### 💡 Demo Queries
Sample queries in demo_queries.txt:
```
What products does the company sell?
Tell me about the company's history.
What is the shipping policy?
How can I return a laptop?
What payment methods are accepted?
Tell me the warranty details for smartphones.
What is the price of apple?
How much does laptop_a cost?
How much is smartphone_x?
What discounts are currently available?
```
### 🧩 Design Decisions

Agentic behavior: Agent autonomously decides between KB and tool usage.

Logging: Detailed step-by-step logs stored for evaluation.

CSV as a tool: Acts as a lightweight API for structured data.

FAISS vector store: Ensures semantic retrieval from KB documents.

Gemini LLM: Used for reasoning and decision-making.

### ⚠️ Known Limitations

Current tool integration only supports CSV lookup.

KB size is limited (8–20 docs).

Gemini model selection may vary based on API availability.

Ambiguous queries may require user clarification.


