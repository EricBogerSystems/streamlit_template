import streamlit as st
from streamlit_option_menu import option_menu
from modules.api_gui import API_GUI


gui = API_GUI()


# Streamlit page config
st.set_page_config(page_title="Template App", page_icon="🖥️", layout="wide")

# Use local CSS file style.css
with open("style/default_style.css")as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)


st.title("Template App")
st.subheader("... under construction ...")

args = None
gui.run(args)