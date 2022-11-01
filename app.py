# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 21:45:43 2022

@author: Amina Anjoom
"""
import streamlit as st
#import openai
from email_generator import email_generator


st.markdown("# Generate Email")

backend = email_generator()

with st.form(key="form"):
    prompt = st.text_input("Key words")
   # st.text("(Example: Write me a professional sounding email to my boss)")

    start = st.text_input("Begin writing the first few or several words of your email:")

    #slider = st.slider("How many characters do you want your email to be? ", min_value=64, max_value=550)
    #st.text("(A typical email is usually 100-500 characters)")

    submit_button = st.form_submit_button(label='Generate Email')

    if submit_button:
        with st.spinner("Generating Email..."):
            output = backend.generate_email(prompt, start)
        st.markdown("# Email Output:")
        st.subheader(start + output)
        st.markdown("____")
       # st.markdown("# Send Your Email")
        #st.subheader("You can press the Generate Email Button again if you're unhappy with the model's output")
        
        #st.subheader("Otherwise:")
        st.text(output)
       # url = "https://mail.google.com/mail/?view=cm&fs=1&to=&su=&body=" + backend.replace_spaces_with_pluses(start + output)

        #st.markdown("[Click me to send the email]({})".format(url))


