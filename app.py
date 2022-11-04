# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 21:45:43 2022

@author: Amina Anjoom
"""
import streamlit as st
import pyarrow as pa
#import openai
from email_generator import email_generator



st.markdown("# Generate Email")

backend = email_generator()

with st.form(key="form"):
    prompt = st.text_input("Key words")

    start = st.text_input("Begin writing the first few or several words of your email:")

    submit_button1 = st.form_submit_button(label='Generate Email')

    if submit_button1:
        with st.spinner("Generating Email..."):
            output = backend.generate_email(prompt, start)
        st.markdown("# Email Output:")
        st.markdown("____")
        st.text(output)
    submit_button2 = st.form_submit_button(label='Arabic Translation')
    if submit_button2:
        out= backend.generate_email(prompt, start)
        with st.spinner("Generating translation..."):
            translation = backend.generate_arabic(out)
        st.markdown("# Email Output:")
        st.subheader(out)
        st.markdown("____")
        st.text(translation)
    
     

