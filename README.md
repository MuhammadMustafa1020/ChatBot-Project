# 💬 LangGraph AI Chatbot with Persistent Memory

A production-ready AI chatbot application built with **LangGraph** state management and **Google Gemini AI**, featuring persistent conversation storage, real-time streaming responses, and an intuitive ChatGPT-like interface.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red)
![LangGraph](https://img.shields.io/badge/LangGraph-Latest-green)
![Google Gemini](https://img.shields.io/badge/Gemini-AI-orange)

## 🌟 Unique Features

This project goes beyond basic RAG applications by implementing:

1. **State-Aware Conversation Management with LangGraph**
   - Advanced state graph architecture for managing conversation flow
   - Checkpoint-based persistence using SQLite
   - Multi-threaded conversation handling with thread isolation

2. **Real-Time Streaming Responses**
   - Token-by-token streaming for better user experience
   - Efficient message chunking and rendering
   - Low-latency AI response delivery

3. **Persistent Multi-Session Chat**
   - Automatic conversation naming based on first message
   - Thread-based conversation storage
   - Resume any conversation from history
   - SQLite-based checkpointing system

4. **Professional ChatGPT-Like UI/UX**
   - Custom-designed dark theme interface
   - Inline rename/delete operations for chat management
   - Three-dot menu with popup actions
   - Responsive and intuitive design

5. **Smart Chat Organization**
   - Automatic chat title generation
   - Conversation history management
   - Active chat highlighting
   - Seamless chat switching

## 🎯 Project Overview

This AI chatbot demonstrates advanced concepts in:
- **Graph-based state management** using LangGraph
- **Persistent storage** with checkpoint recovery
- **Streaming AI responses** for enhanced UX
- **Session management** with isolated conversation threads
- **Modern UI design** inspired by industry-leading chat applications

The application uses Google's Gemini Flash model for fast, accurate responses while maintaining conversation context across multiple sessions.

## 🛠️ Technology Stack

### Backend
- **LangGraph** - State graph management and conversation flow
- **LangChain** - AI framework and message handling
- **Google Generative AI** - Gemini Flash LLM
- **SQLite** - Persistent conversation storage

### Frontend
- **Streamlit** - Web application framework
- **Custom CSS** - ChatGPT-inspired UI design
- **Session State Management** - Multi-conversation handling

### Additional
- **Python-dotenv** - Environment variable management
- **UUID** - Unique conversation identifiers

## 📋 Prerequisites

- Python 3.12 or higher
- Google AI API Key ([Get it here](https://makersuite.google.com/app/apikey))
- Git

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/LangGraph_Chatbot.git
cd LangGraph_Chatbot
```

### 2. Create Virtual Environment

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

**Important:** Get your free API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

### 5. Run the Application

```bash
streamlit run streamlit_frontend_database.py
```

The application will open in your browser at `http://localhost:8501`

## 📖 Usage Guide

### Starting a New Chat
1. Click the **➕ New Chat** button in the sidebar
2. Type your message in the input box
3. The chat will be automatically named based on your first message

### Managing Conversations
- **Switch Chats**: Click on any chat name in the sidebar
- **Rename Chat**: Click the ⋮ menu → Select "Rename"
- **Delete Chat**: Click the ⋮ menu → Select "Delete"

### Features in Action
- **Real-time Streaming**: Watch AI responses appear word-by-word
- **Persistent History**: All conversations are saved automatically
- **Multi-threading**: Each chat maintains its own conversation thread
- **Context Awareness**: AI remembers the entire conversation history

## 📁 Project Structure

```
LangGraph_Chatbot/
├── streamlit_frontend_database.py    # Main application with database persistence
├── langgraph_database_backend.py     # LangGraph state management backend
├── streamlit_frontend.py             # Simple version without persistence
├── langgraph_backend.py              # Basic backend implementation
├── streamlit_frontend_streaming.py   # Streaming-focused version
├── streamlit_frontend_threading.py   # Threading demonstration
├── chatbot.db                        # SQLite database (auto-generated)
├── .env                              # Environment variables (create this)
├── requirements.txt                  # Python dependencies
├── README.md                         # This file
├── GROUP_DETAILS.md                  # Group member information
└── DEPLOYMENT.md                     # Deployment guide
```

## 🎨 Key Implementation Highlights

### LangGraph State Management
```python
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

graph = StateGraph(ChatState)
graph.add_node("chat_node", chat_node)
chatbot = graph.compile(checkpointer=checkpointer)
```

### Persistent Checkpointing
```python
conn = sqlite3.connect(database="chatbot.db", check_same_thread=False)
checkpointer = SqliteSaver(conn=conn)
```

### Streaming Responses
```python
def ai_only_stream():
    for message_chunk, metadata in chatbot.stream(
        {"messages": [HumanMessage(content=user_input)]},
        config=CONFIG,
        stream_mode="messages"
    ):
        if isinstance(message_chunk, AIMessage):
            yield message_chunk.content
```

## 🌐 Deployment

### Streamlit Cloud (Recommended)

1. Push your code to GitHub
2. Visit [Streamlit Cloud](https://streamlit.io/cloud)
3. Connect your GitHub repository
4. Add your `GOOGLE_API_KEY` to secrets
5. Deploy!

**Detailed deployment instructions:** See [DEPLOYMENT.md](DEPLOYMENT.md)

## 🎥 Demo Video

[Link to demo video will be added here]

The demo video showcases:
- Application startup and interface tour
- Creating and managing multiple conversations
- Real-time streaming responses
- Rename and delete functionality
- Conversation persistence and recovery
- UI/UX design elements

## 👥 Group Members

See [GROUP_DETAILS.md](GROUP_DETAILS.md) for complete group information.

## 🔐 Security Notes

- Never commit your `.env` file to GitHub
- Keep your Google API key private
- The `.gitignore` file is configured to exclude sensitive files

## 🐛 Troubleshooting

### API Key Error
- Verify your API key is correct in `.env`
- Ensure the key has access to Gemini API
- Restart the application after updating `.env`

### Database Issues
- Delete `chatbot.db` and restart the app
- Check SQLite permissions in the project directory

### Import Errors
- Ensure virtual environment is activated
- Run `pip install -r requirements.txt` again

## 📝 License

This project is created for educational purposes as part of a semester project.

## 🙏 Acknowledgments

- Google Generative AI for providing the Gemini API
- LangChain and LangGraph communities
- Streamlit for the amazing web framework

## 📞 Contact

For questions or issues, please create an issue in the GitHub repository.

---

**Built with ❤️ using LangGraph, Streamlit, and Google Gemini AI**
