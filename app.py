# app.py
    
import streamlit as st    
from translator import Translator
from utils.language_utils import get_supported_languages, get_model_config

st.set_page_config(page_title="LinguaAI", layout="wide")
st.markdown("<h1 style='text-align: center;'>Lingua.ai 🌍</h1>", unsafe_allow_html=True)
st.markdown("---")

languages = get_supported_languages()

# Language dropdowns
col1, col2, col3 = st.columns([3, 1, 3])
with col1:
    source_lang = st.selectbox("Source Language", languages, index=0)
with col3:
    target_lang = st.selectbox("Target Language", languages, index=1)

# Session state
if "translator" not in st.session_state:
    st.session_state.translator = Translator()
if "input_text" not in st.session_state:
    st.session_state.input_text = ""
if "translated_text" not in st.session_state:
    st.session_state.translated_text = ""

# Input and Output layout
input_col, arrow_col, output_col = st.columns([3, 0.5, 3])

with input_col:
    st.session_state.input_text = st.text_area(
        f"Enter text in {source_lang}:",
        value=st.session_state.input_text,
        height=200,
        key="input_box"
    )

with arrow_col:
    st.markdown("<p style='text-align: center; font-size: 30px; margin-top: 85px;'>⇄</p>", unsafe_allow_html=True)

with output_col:
    st.text_area(
        f"Translated ({target_lang}):",
        value=st.session_state.translated_text,
        height=200,
        key="output_box",
        disabled=True
    )

btn_input_col, _, btn_output_col = st.columns([3, 0.5, 3])

# Translate Button
with btn_input_col:
    st.markdown("""
        <style>
        div.translate-button-container > button 
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="translate-button-container">', unsafe_allow_html=True)
    if st.button("Translate", key="translate_button"):
        if not st.session_state.input_text.strip():
            st.warning("Please enter some text.")
        else:
            model_config = get_model_config(source_lang, target_lang)
            if not model_config:
                st.error("⚠️ Unsupported language pair.")
            else:
                with st.spinner("Translating..."):
                    model_name = model_config["model"]
                    src_code = model_config["src_lang"]
                    tgt_code = model_config["tgt_lang"]
                    result = st.session_state.translator.translate(
                        st.session_state.input_text.strip(),
                        model_name,
                        src_lang=src_code,
                        tgt_lang=tgt_code
                    )
                st.session_state.translated_text = result
                st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# clear all Button
with btn_output_col:
    if st.session_state.translated_text:
        if st.button("🧹 Clear All", key="clear_button"):
            st.session_state.input_text = ""
            st.session_state.translated_text = ""
            st.rerun()

st.markdown("---")
st.caption("⚡ Lingua.ai | GenAI-Powered Multi-Language Translation")
