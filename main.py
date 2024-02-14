import streamlit as st
from PIL import Image

st.title('Hello World')
st.caption('This is a simple Streamlit app.')

image = Image.open('./data/penguin.jpg')
st.image(image, caption='A penguin', width=100)
