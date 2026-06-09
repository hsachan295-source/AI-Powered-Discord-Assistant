# 🤖 AI-Powered Discord Assistant

> An intelligent, production-ready Discord bot powered by **LangChain**, **LangGraph**, and **Google Gemini** — capable of real-time web search and AI-driven conversations.

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Discord.py](https://img.shields.io/badge/Discord.py-2.x-5865F2?style=flat-square&logo=discord&logoColor=white)](https://discordpy.readthedocs.io)
[![LangChain](https://img.shields.io/badge/LangChain-Agent-1C3C3C?style=flat-square)](https://langchain.com)
[![Gemini](https://img.shields.io/badge/Gemini-3.5--Flash-4285F4?style=flat-square&logo=google&logoColor=white)](https://ai.google.dev)
[![Tavily](https://img.shields.io/badge/Tavily-Search_API-FF6B35?style=flat-square)](https://tavily.com)

---

## 1. Project Flow Diagram (Horizontal Block Flow)

The following Mermaid diagram shows the complete flow of data and execution across all system components. It contains the **User (Actor)**, **Platform Layer**, **AI Agent Core**, **Tool Layer**, and **External API** symbols — displaying the full process from left to right.

```mermaid
flowchart LR
    %% ─── Node Definitions ───────────────────────────────────────────────────

    USER(["👤 User / Client"])

    subgraph DISCORD_LAYER ["  🟣 Discord Platform Layer  "]
        direction TB
        DS["🖥️ Discord Server"]
        BOT["🤖 Discord Bot\n── bot.py ──\ndiscord.Client"]
    end

    subgraph AGENT_CORE ["  🟡 LangChain Agent Core  "]
        direction TB
        AGENT["🧠 LangChain Agent\n── agent.py ──\nLangGraph ReAct"]
        DECISION{{"⚡ Tool\nRequired?"}}
    end

    subgraph TOOL_LAYER ["  🟢 Tool Layer  "]
        direction TB
        TAVILY["🔍 Tavily Search Tool\n── surInterNet() ──\nReal-time Web Search"]
    end

    subgraph LLM_LAYER ["  🔵 LLM Layer  "]
        direction TB
        GEMINI[("🌟 Google Gemini\n── gemini-3.5-flash ──\nLLM Inference")]
    end

    %% ─── Main Flow ──────────────────────────────────────────────────────────

    USER      -->|"① Sends message"| DS
    DS        -->|"② Routes to bot"| BOT
    BOT       -->|"③ Captures & forwards"| AGENT
    AGENT     -->|"④ Analyzes query"| DECISION

    %% ─── Tool Branch ────────────────────────────────────────────────────────

    DECISION  -->|"⑤ YES — Tool needed"| TAVILY
    TAVILY    -.->|"⑥ Searches internet"| TAVILY
    TAVILY    -->|"⑦ Returns results"| AGENT

    %% ─── LLM Branch ────────────────────────────────────────────────────────

    DECISION  -->|"⑤ NO — Direct LLM"| GEMINI
    AGENT     -->|"⑧ Sends context + query"| GEMINI
    GEMINI    -->|"⑨ Generates response"| AGENT

    %% ─── Response Flow ──────────────────────────────────────────────────────

    AGENT     -->|"⑩ Returns answer"| BOT
    BOT       -->|"⑪ Formats & sends reply"| DS
    DS        -->|"⑫ Delivers to user"| USER

    %% ─── Styling ────────────────────────────────────────────────────────────

    classDef userStyle      fill:#dae8fc,stroke:#6c8ebf,stroke-width:3px,color:#1a1a2e,font-weight:bold
    classDef platformStyle  fill:#e1d5e7,stroke:#9673a6,stroke-width:2px,color:#1a1a2e
    classDef agentStyle     fill:#fff2cc,stroke:#d6b656,stroke-width:3px,color:#1a1a2e,font-weight:bold
    classDef decisionStyle  fill:#ffe6cc,stroke:#d79b00,stroke-width:3px,color:#1a1a2e,font-weight:bold
    classDef toolStyle      fill:#d5e8d4,stroke:#82b366,stroke-width:2px,color:#1a1a2e
    classDef llmStyle       fill:#dae8fc,stroke:#0050ef,stroke-width:3px,color:#1a1a2e,font-weight:bold

    class USER              userStyle
    class DS,BOT            platformStyle
    class AGENT             agentStyle
    class DECISION          decisionStyle
    class TAVILY            toolStyle
    class GEMINI            llmStyle
```

---

## 2. Architecture Legend

| Symbol | Node Type | Component | Description |
|:---:|---|---|---|
| 👤 | **Actor / User** | User / Client | The human interacting with the bot |
| 🖥️ | **Platform** | Discord Server | Discord messaging infrastructure |
| 🤖 | **Service** | Discord Bot | `discord.py` event listener (`bot.py`) |
| 🧠 | **AI Agent** | LangChain Agent | ReAct Agent with tool orchestration (`agent.py`) |
| ⚡ | **Decision** | Tool Router | Agent decides if external tool is needed |
| 🔍 | **Tool** | Tavily Search | Real-time web search via Tavily API |
| 🌟 | **LLM** | Google Gemini | `gemini-3.5-flash` for text generation |

---

## 3. Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **Interface** | `discord.py 2.x` | Discord event handling and message delivery |
| **Agent Framework** | `LangChain` + `LangGraph` | ReAct agent loop and tool orchestration |
| **LLM** | `Google Gemini 3.5 Flash` | Natural language understanding & generation |
| **Web Search** | `Tavily Search API` | Real-time internet search for up-to-date info |
| **Runtime** | `Python 3.10+`, `asyncio` | Async execution environment |
| **Config** | `python-dotenv` | Secure environment variable management |

---

## 4. Key Features

1. **🧠 Intelligent ReAct Agent** — Powered by `gemini-3.5-flash` via LangChain, the agent reasons and plans before responding.
2. **🔍 Real-time Web Search** — Automatically searches the internet via the Tavily API when the query needs current information.
3. **⚡ Async Processing** — Uses Python's `asyncio` and `discord.py` to handle concurrent message events without blocking.
4. **🔒 Secure Config** — All API keys are managed via `.env` and never committed to source control.

---

## 5. Codebase Structure

```
AI-Powered-Discord-Assistant/
├── bot.py               # Discord client, event listener, message handler
├── agent.py             # LangChain Agent, tool definitions, Gemini LLM setup
├── .env                 # API keys (gitignored)
├── .gitignore           # Excludes venv, .env, __pycache__
├── architecture.drawio  # Editable draw.io diagram
├── architecture.png     # Static architecture image
└── README.md            # Project documentation
```

| File | Role |
|---|---|
| **[bot.py](bot.py)** | Initializes `discord.Client`, listens for `on_message` events, forwards to agent |
| **[agent.py](agent.py)** | Defines LangChain agent, `surInterNet` tool, Gemini LLM binding |

---

## 6. Setup & Installation

### Prerequisites
Make sure you have **Python 3.10+** installed.

### Install Dependencies

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Activate (macOS / Linux)
source venv/bin/activate

# Install packages
pip install discord.py python-dotenv langchain langchain-google-genai tavily-python
```

### Environment Variables

Create a `.env` file in the project root:

```env
DISCORD_API_KEY=your_discord_bot_token
TAVILY_API_KEY=your_tavily_api_key
GOOGLE_API_KEY=your_gemini_api_key
```

### Run the Bot

```bash
python bot.py
```

---

## 7. Interactive draw.io Diagram

A fully styled, editable architecture diagram is included:

| Option | Link |
|---|---|
| 📁 **File** | [architecture.drawio](architecture.drawio) |
| 🌐 **Open Online** | [Open in diagrams.net](https://app.diagrams.net/?showEdit=1&open=https%3A%2F%2Fraw.githubusercontent.com%2Fhsachan295-source%2FAI-Powered-Discord-Assistant%2Fmain%2Farchitecture.drawio) |
| 🖼️ **Static Image** | [architecture.png](architecture.png) |

---

## 8. Detailed Execution Flow

| Step | Actor | Action |
|:---:|---|---|
| ① | **User** | Types a message in Discord |
| ② | **Discord Server** | Routes message to the registered bot |
| ③ | **Discord Bot** | `on_message` event fires; bot captures content |
| ④ | **LangChain Agent** | Receives `HumanMessage`, begins ReAct reasoning loop |
| ⑤ | **Agent Decision** | Determines if a tool (Tavily) is needed |
| ⑥ | **Tavily Tool** | Executes `surInterNet(query)` — searches the web |
| ⑦ | **Tavily Tool** | Returns search results back to the agent |
| ⑧ | **LangChain Agent** | Sends enriched context + query to Gemini |
| ⑨ | **Gemini LLM** | Generates a natural language response |
| ⑩ | **LangChain Agent** | Returns final answer to Discord Bot |
| ⑪ | **Discord Bot** | Sends response via `message.channel.send()` |
| ⑫ | **User** | Receives the final answer in Discord |
