import streamlit as st

video = open('./data/penguins.mp4', 'rb').read()
st.video(video, start_time=10)

with st.form(key='my_form'):
    name = st.text_input('Enter your name')
    address = st.text_input('Enter your address')
    age_category = st.selectbox('Select your age category', ['0-18', '19-30', '31-50', '51-65', '65+'])
    hobbies = st.multiselect('Select your hobbies', ['Reading', 'Writing', 'Running', 'Swimming', 'Cycling'])

    submit_button = st.form_submit_button('Submit')
    cancel_button = st.form_submit_button('Cancel')

    if submit_button:
        st.write(f'Hello, {name}! Your address is {address}. You are in the {age_category} age category.')
        st.text(f'Your hobbies are: {", ".join(hobbies)}')

