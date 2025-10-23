import sys
sys.path.append('.')

import streamlit as st
from core.nlp_engine import NLPEngine
from core.response_generator import ResponseGenerator

# Page configuration
st.set_page_config(
    page_title="TechHub AI Support",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .header {
        text-align: center;
        padding: 20px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []

if 'nlp_engine' not in st.session_state:
    with st.spinner("Loading AI Engine..."):
        st.session_state.nlp_engine = NLPEngine()

if 'response_generator' not in st.session_state:
    st.session_state.response_generator = ResponseGenerator()

# Header
st.markdown("""
    <div class="header">
        <h1>🤖 TechHub Customer Support AI</h1>
        <p>Instant answers to your electronics questions</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("About TechHub AI")
    st.info("""
    This is an AI-powered customer support chatbot for TechHub Electronics.
    
    **Available 24/7** to answer questions about:
    - Shipping & Delivery
    - Returns & Refunds
    - Product Availability
    - Account Issues
    - Warranty & Support
    - And more!
    """)
    
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()
    
    st.markdown("---")
    st.write("**Need Human Support?**")
    st.write("📧 support@techhub.com")
    st.write("📞 1-800-TECHHUB")

# Main chat area
st.subheader("Chat with TechHub Support")

# Display chat history
for message in st.session_state.messages:
    if message['role'] == 'user':
        st.markdown(f"""
        <div style="text-align: right; margin-bottom: 10px;">
            <div style="display: inline-block; background-color: #007bff; color: white; padding: 10px 15px; border-radius: 10px; max-width: 70%;">
                {message['content']}
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div style="text-align: left; margin-bottom: 10px;">
            <div style="display: inline-block; background-color: #e9ecef; color: #333; padding: 10px 15px; border-radius: 10px; max-width: 70%;">
                {message['content']}
            </div>
        </div>
        """, unsafe_allow_html=True)

# Input area
st.markdown("---")

col1, col2 = st.columns([4, 1])
with col1:
    user_input = st.text_input(
        "Type your question here:",
        placeholder="e.g., How long does shipping take?",
        key=f"user_question_{len(st.session_state.messages)}"
    )

with col2:
    submit_button = st.button("Send", use_container_width=True)

# Handle submit
if submit_button and user_input:
    st.session_state.messages.append({
        'role': 'user',
        'content': user_input
    })
    
    with st.spinner("Processing your question..."):
        try:
            analysis = st.session_state.nlp_engine.analyze_query(user_input)
            response_data = st.session_state.response_generator.generate_response(analysis)
            
            st.session_state.messages.append({
                'role': 'assistant',
                'content': response_data['response']
            })
            
        except Exception as e:
            st.error(f"Error: {str(e)}")
    
    st.rerun()

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #666; font-size: 12px;">
        <p>Powered by TechHub AI | Available 24/7</p>
    </div>
""", unsafe_allow_html=True)