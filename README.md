# 🤖 AI-Powered Discord Assistant

An intelligent, agent-based Discord bot that uses state-of-the-art Generative AI models. The bot listens to user messages, understands context, and uses specialized tools to surf the web and generate images dynamically.

---

## 🗺️ System Architecture (Horizontal Block Diagram)

Below is the horizontal block diagram showing how the data flows from the User to the Discord Bot, the Agent, and its tools, and back to the User.

```mermaid
graph LR
    User["👤 User (Discord Client)"] -->|1. Sends Message| Bot["💬 Discord Bot (bot.py)"]
    Bot -->|2. Invokes Agent (ainvoke)| Agent["🤖 LangChain Agent (agent.py)"]
    
    Agent -->|3a. Queries Web| Tavily["🔍 Tavily Web Search (surInterNet)"]
    Tavily -.->|4a. Results| Agent
    
    Agent -->|3b. Requests Image| OpenAI["🎨 Image Gen (generateAndSendImage)"]
    OpenAI -.->|4b. Uploads Image File| Bot
    
    Agent -.->|5. Returns Status| Bot
    Bot -.->|6. Delivers Reply| User

    style User fill:#7289da,stroke:#5b73c7,stroke-width:2px,color:#fff
    style Bot fill:#5865F2,stroke:#4752C4,stroke-width:2px,color:#fff
    style Agent fill:#F4B400,stroke:#DBA100,stroke-width:2px,color:#fff
    style Tavily fill:#0F9D58,stroke:#0B7F46,stroke-width:2px,color:#fff
    style OpenAI fill:#DB4437,stroke:#C23B2F,stroke-width:2px,color:#fff
```

### 📈 Interactive draw.io Diagram
We have also included a fully styled edit-ready draw.io diagram file:
- **File Link:** [architecture.drawio](file:///d:/Data%20science%20course/12-Generative%20AI/project-AI-powered-discord-assistant-10/architecture.drawio)
- **How to edit/view:** Open [draw.io (diagrams.net)](https://app.diagrams.net/) and drag and drop the `architecture.drawio` file onto the canvas to view or modify it.

---

## 🚀 Key Features

1. **Intelligent Conversational Agent:** Powered by `gemini-3.5-flash` via LangChain Google GenAI, allowing the bot to engage in meaningful conversations with users.
2. **Real-time Web Search:** The agent can access current information on the internet through the Tavily Search API.
3. **AI Image Generation:** Generates images on the fly using OpenAI models (`gpt-5.4-mini` / DALL-E wrapper) and uploads the generated files directly back into the Discord channel.
4. **Asynchronous Processing:** Uses Python's `asyncio` and `discord.py` to handle events concurrently, including background image uploading.

---

## 📁 Codebase Structure

The project consists of two core files:

*   **[bot.py](file:///d:/Data%20science%20course/12-Generative%20AI/project-AI-powered-discord-assistant-10/bot.py):** Initializes the Discord client, listens for incoming messages, and passes them to the LangChain Agent.
*   **[agent.py](file:///d:/Data%20science%20course/12-Generative%20AI/project-AI-powered-discord-assistant-10/agent.py):** Defines the LangChain agent configuration, custom tools (`surInterNet` and `generateAndSendImage`), and binds the models.

---

## 🛠️ Setup & Installation

### 1. Prerequisites
Make sure you have **Python 3.10+** installed on your system.

### 2. Install Dependencies
Initialize your virtual environment and install the required libraries:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# On Windows (CMD):
.\venv\Scripts\activate.bat
# On macOS/Linux:
source venv/bin/activate

# Install required packages
pip install discord.py python-dotenv langchain-openai langchain-google-genai tavily-python
```

### 3. Environment Variables
Create a `.env` file in the root directory and define the following API keys:

```env
DISCORD_API_KEY=your_discord_bot_token
TAVILY_API_KEY=your_tavily_search_api_key
OPENAI_API_KEY=your_openai_api_key
GOOGLE_API_KEY=your_gemini_api_key
```

### 4. Running the Bot
Once the environment variables are configured and the virtual environment is activated, run:

```bash
python bot.py
```

---

## 🛠️ Detailed Component Interaction

1.  **User Message:** The user types a message in Discord.
2.  **Discord Bot (`bot.py`):** Captures the message event, triggers a typing status (`typing()`), and invokes the agent asynchronously.
3.  **Agent Execution (`agent.py`):** Uses the `gemini-3.5-flash` model to analyze the user prompt.
    *   If it requires recent information, it runs the `surInterNet` tool.
    *   If it requires an image, it runs the `generateAndSendImage` tool, which generates the image, decodes it from Base64, and uploads the file directly to the Discord channel using `asyncio.run_coroutine_threadsafe`.
4.  **Final Response:** The bot sends the textual response from the agent to the Discord channel.
