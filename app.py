import streamlit as st

st.title('first appe by nikita')

username = st.text_input('give me your name')

number = st.slider('select number', 0, 10)

if number % 2 == 0:
    st.write(f'hello {username}, your number is divisible by 2 ')


if number % 2 != 0:
    st.write(f'hello {username}, your number is not divisible by 2 ')

if st.button('dumb ape button'):
    st.write('why did you click this button')