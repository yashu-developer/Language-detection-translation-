import streamlit as st
from deep_translator import GoogleTranslator
# --- Page Configuration ---
st.set_page_config(page_title="Pro AI Translator", page_icon="📝", layout="centered")

# --- Custom Styling ---
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stTextArea textarea {
        font-size: 1.1rem !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- App Header ---
st.title("📝 Translingo Sense")
st.subheader("Free & Unlimited AI Translation")

# --- Language Setup ---
# Fetching supported languages automatically from the engine
langs_dict = GoogleTranslator().get_supported_languages(as_dict=True)
languages = list(langs_dict.keys())

# --- Layout ---
col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox("From (Source Language)", ["auto"] + languages)

with col2:
    # Defaulting target to English if available
    default_index = languages.index('english') if 'english' in languages else 0
    target_lang = st.selectbox("To (Target Language)", languages, index=default_index)

# --- Input Area ---
text_to_translate = st.text_area("Enter text to translate:", placeholder="Type or paste your content here...", height=200)

# --- Translation Logic ---
if st.button("Translate Now"):
    if text_to_translate.strip():
        with st.spinner("Processing..."):
            try:
                # Initialize Translator
                # source='auto' automatically detects the input language
                translated_text = GoogleTranslator(
                    source=source_lang, 
                    target=langs_dict[target_lang]
                ).translate(text_to_translate)

                # --- Output Area ---
                st.markdown("---")
                st.success(f"**Translated Text ({target_lang.title()}):**")
                st.code(translated_text, language=None)
                
                # Metadata
                st.caption(f"Word count: {len(text_to_translate.split())} | Character count: {len(text_to_translate)}")
                
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter some text to translate.")

# --- Sidebar Info ---
st.sidebar.title("About")
st.sidebar.info("""
This app uses a web-scraping translation engine. 
- **No API Key needed**
- **No Usage Limits**
- **100+ Languages supported**
""")