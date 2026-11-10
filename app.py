import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_title="Sector Officer Route Map")

# 1. Read the HTML file directly from the repository
with open("Larger_UI_Map_App.html", "r", encoding="utf-8") as map_file:
    html_content = map_file.read()

# 2. Display the HTML content in the Streamlit app
components.html(html_content, height=950, scrolling=True)