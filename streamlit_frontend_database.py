import streamlit as st
from langgraph_database_backend import chatbot, retreive_all_threads
from langchain_core.messages import HumanMessage, AIMessage
import uuid

# **************************************** utility functions *************************

def generate_thread_id():
    thread_id = uuid.uuid4()
    return thread_id

def generate_chat_name(first_message):
    """Generate a chat name from the first message (max 30 chars)"""
    if len(first_message) > 30:
        return first_message[:30] + "..."
    return first_message

def reset_chat():
    thread_id = generate_thread_id()
    st.session_state['thread_id'] = thread_id
    add_thread(st.session_state['thread_id'])
    st.session_state['message_history'] = []

def add_thread(thread_id):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)
    # Initialize chat name if not exists
    if thread_id not in st.session_state['chat_names']:
        st.session_state['chat_names'][thread_id] = "New Chat"

def get_chat_name(thread_id):
    """Get the display name for a chat thread"""
    return st.session_state['chat_names'].get(thread_id, "New Chat")

def delete_chat(thread_id):
    """Delete a chat thread"""
    if thread_id in st.session_state['chat_threads']:
        st.session_state['chat_threads'].remove(thread_id)
    if thread_id in st.session_state['chat_names']:
        del st.session_state['chat_names'][thread_id]
    # If deleting current chat, reset to new chat
    if st.session_state['thread_id'] == thread_id:
        reset_chat()

def rename_chat(thread_id, new_name):
    """Rename a chat thread"""
    st.session_state['chat_names'][thread_id] = new_name

def load_conversation(thread_id):
    state = chatbot.get_state(config={'configurable': {'thread_id': thread_id}})
    # Check if messages key exists in state values, return empty list if not
    return state.values.get('messages', [])


# **************************************** Session Setup ******************************
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()

if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads'] = retreive_all_threads()

if 'chat_names' not in st.session_state:
    st.session_state['chat_names'] = {}
    # Load names for existing threads from their first message
    for thread_id in st.session_state['chat_threads']:
        messages = load_conversation(thread_id)
        if messages:
            # Find first user message
            for msg in messages:
                if isinstance(msg, HumanMessage):
                    st.session_state['chat_names'][thread_id] = generate_chat_name(msg.content)
                    break
            if thread_id not in st.session_state['chat_names']:
                st.session_state['chat_names'][thread_id] = "New Chat"
        else:
            st.session_state['chat_names'][thread_id] = "New Chat"

add_thread(st.session_state['thread_id'])


# **************************************** Sidebar UI *********************************

# Custom CSS for ChatGPT-like professional look
st.markdown("""
<style>
    /* Sidebar background */
    [data-testid="stSidebar"] {
        background-color: #171717;
    }
    
    /* Hide streamlit branding */
    .stDeployButton {display:none;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Chat buttons */
    .stButton > button {
        background-color: transparent;
        border: none;
        color: #ececec;
        padding: 10px 12px;
        border-radius: 8px;
        width: 100%;
        text-align: left;
        transition: background-color 0.2s;
        font-size: 14px;
    }
    
    .stButton > button:hover {
        background-color: #2a2a2a;
    }
    
    /* New chat button */
    div[data-testid="stSidebar"] > div:first-child .stButton > button {
        border: 1px solid #4a4a4a;
        background-color: transparent;
        margin-bottom: 20px;
        font-weight: 500;
    }
    
    /* Hide popover arrow */
    [data-testid="stPopoverBody"] button[kind="header"] {
        display: none !important;
    }
    
    /* Hide dropdown arrow on popover button - multiple selectors */
    button[data-baseweb="popover"] svg,
    [data-testid="stPopover"] svg,
    [data-testid="stPopover"] button svg,
    button[kind="header"] svg {
        display: none !important;
    }
    
    /* Force popover button to only show text */
    button[kind="header"] {
        padding-right: 8px !important;
    }
    
    button[kind="header"]::after {
        content: none !important;
    }
    
    /* Style popover button to look like just three dots */
    button[data-testid="baseButton-header"] {
        background-color: transparent !important;
        border: none !important;
        padding: 4px 8px !important;
        min-width: auto !important;
        width: auto !important;
    }
    
    button[data-testid="baseButton-header"]:hover {
        background-color: #3a3a3a !important;
        border-radius: 6px !important;
    }
    
    /* Popover content styling */
    [data-testid="stPopover"] {
        background-color: transparent;
    }
    
    [data-testid="stPopoverBody"] {
        background-color: #2f2f2f;
        border-radius: 12px;
        padding: 6px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.6);
        border: 1px solid #3f3f3f;
        min-width: 200px;
    }
    
    /* Style menu buttons inside popover */
    [data-testid="stPopoverBody"] .stButton > button {
        width: 100%;
        text-align: left;
        padding: 12px 16px;
        font-size: 15px;
        border-radius: 8px;
        margin: 2px 0;
    }
    
    [data-testid="stPopoverBody"] .stButton > button:hover {
        background-color: #3a3a3a;
    }
    
    /* Red color for delete button */
    [data-testid="stPopoverBody"] .stButton:last-child > button {
        color: #ef4444 !important;
    }
</style>
""", unsafe_allow_html=True)

st.sidebar.title('💬 LangGraph Chat')

if st.sidebar.button('➕ New Chat', use_container_width=True):
    reset_chat()
    st.rerun()

st.sidebar.markdown("---")

# Show all chats
for thread_id in st.session_state['chat_threads'][::-1]:
    chat_name = get_chat_name(thread_id)
    is_current = (thread_id == st.session_state['thread_id'])
    
    # Check if this chat is in edit mode
    if st.session_state.get(f'editing_{thread_id}', False):
        # Show rename interface
        st.sidebar.markdown(f"**✏️ Rename Chat**")
        new_name = st.sidebar.text_input(
            "New name",
            value=chat_name,
            key=f"rename_input_{thread_id}",
            label_visibility="collapsed"
        )
        col1, col2 = st.sidebar.columns(2)
        with col1:
            if st.button('✓ Save', key=f"save_{thread_id}", use_container_width=True):
                rename_chat(thread_id, new_name)
                st.session_state[f'editing_{thread_id}'] = False
                st.rerun()
        with col2:
            if st.button('✗ Cancel', key=f"cancel_{thread_id}", use_container_width=True):
                st.session_state[f'editing_{thread_id}'] = False
                st.rerun()
        st.sidebar.markdown("---")
    else:
        # Normal chat display with three-dot menu
        col1, col2 = st.sidebar.columns([6, 1])
        
        with col1:
            # Chat button
            display_name = f"💬 {chat_name}" if is_current else chat_name
            if st.button(
                display_name,
                key=f"chat_{thread_id}",
                use_container_width=True
            ):
                if thread_id != st.session_state['thread_id']:
                    st.session_state['thread_id'] = thread_id
                    messages = load_conversation(thread_id)
                    temp_messages = []
                    for msg in messages:
                        role = 'user' if isinstance(msg, HumanMessage) else 'assistant'
                        temp_messages.append({'role': role, 'content': msg.content})
                    st.session_state['message_history'] = temp_messages
                    st.rerun()
        
        with col2:
            # Three-dot menu with popover
            with st.popover("⋮", use_container_width=False):
                # Rename option
                if st.button('Rename', key=f"do_rename_{thread_id}", use_container_width=True):
                    st.session_state[f'editing_{thread_id}'] = True
                    st.rerun()
                
                # Delete option
                if st.button('Delete', key=f"do_delete_{thread_id}", use_container_width=True):
                    delete_chat(thread_id)
                    st.rerun()


# **************************************** Main UI ************************************

# loading the conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

user_input = st.chat_input('Type here')

if user_input:

    # Generate chat name from first message
    if len(st.session_state['message_history']) == 0:
        st.session_state['chat_names'][st.session_state['thread_id']] = generate_chat_name(user_input)

    # first add the message to message_history
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.text(user_input)

    CONFIG = {'configurable': {'thread_id': st.session_state['thread_id']}}

     # first add the message to message_history
    with st.chat_message("assistant"):
        def ai_only_stream():
            for message_chunk, metadata in chatbot.stream(
                {"messages": [HumanMessage(content=user_input)]},
                config=CONFIG,
                stream_mode="messages"
            ):
                if isinstance(message_chunk, AIMessage):
                    # yield only assistant tokens
                    yield message_chunk.content

        ai_message = st.write_stream(ai_only_stream())

    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})