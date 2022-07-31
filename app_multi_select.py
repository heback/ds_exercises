import streamlit as st

my_lang = [
    'Python',
    'C',
    'C++',
    'C#',
    'Go',
    'Java']
choice = st.selectbox('Langauge', my_lang)
st.write('You selected {}'.format(choice))

multi_choices = st.multiselect('Multi Select', my_lang)
