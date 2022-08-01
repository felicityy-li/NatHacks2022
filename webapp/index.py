import streamlit as st
import pandas as pd
import numpy as np

app_mode = st.sidebar.selectbox("Navigate to",['Home','Support','About us'])
stress_score = 0
sentences = ""

if app_mode == 'Home':
    st.image("https://braincorebismarck.com/wp-content/uploads/2017/05/braincore_icons-02-e1495563799323.png")
    st.title("Neuro Journal")
    journal = st.text_area("Journal your feelings and vent about a time you were stressed",placeholder="natHacks2022 is closing in 12 hours, but I haven't finished my code yet!")
    clicked = st.button("Close journal")
    if (clicked == True):
        sentences = journal.split(".")
        stress_score = 1
        app_mode = 'Support'
elif app_mode == 'Support':
    st.markdown("It seems like you are in a very stressful situation. We would love to help you with it.")
    if stress_score < 3:
        options = st.selectbox("Select the following stress relief methods",['Games','Spotify playlist'])
