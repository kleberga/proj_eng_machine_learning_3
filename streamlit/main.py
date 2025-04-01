import streamlit as st

name = st.text_input("Nome")

st.markdown("""
# Teste   2          
""")

if name:
    st.write("Olá, " + name + "!")
else:
    st.write("Olá mundo")

