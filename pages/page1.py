import streamlit as st

st.subheader('This is a subheader')
st.text('This is a text')

code = '''def hello():
    print('Hello, Streamlit!')'''
st.code(code, language='python')
