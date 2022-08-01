import streamlit as st
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
##from scipy.io import wavfile
##from scipy import signal
##import sentiment_analysis
##from sentiment_analysis import *

app_mode = st.sidebar.selectbox("Navigate to",['Home','About us'])
stress_score = 0
sentences = ""

sounds_of_nature_playlist = ['https://www.youtube.com/watch?v=eKFTSSKCzWA&ab_channel=johnnielawson',
                             'https://www.youtube.com/watch?v=ipf7ifVSeDU&ab_channel=CalmedByNature',
                             'https://www.youtube.com/watch?v=q76bMs-NwRk&ab_channel=TheRelaxedGuy']
classical_music_playlist = ['https://www.youtube.com/watch?v=pxEj6m_7Qfk&ab_channel=HALIDONMUSIC',
                            'https://www.youtube.com/watch?v=yH3_tTPv2bo&ab_channel=HALIDONMUSIC',
                            'https://www.youtube.com/watch?v=uk-DSogtQRo']
lofi_music_playlist = ['https://www.youtube.com/watch?v=81WBzpwK1Rk&ab_channel=Mr_MoMoMusic',
                       'https://www.youtube.com/watch?v=0xs-oaSZdqE&ab_channel=LittleSoul',
                       'https://www.youtube.com/watch?v=W6YI3ZFOL0A&ab_channel=Ambition']

def parse_youtube_link(col1,col2,col3,linkArray):
    col1.video(linkArray[0])
    col2.video(linkArray[1])
    col3.video(linkArray[2])

## def predict_stress_score(sentences):
    ##stress_count = 0
    ##prediction_array = predict(sentences)
    ##for prediction in prediction_array:
        ##if(prediction == 'stress'):
            ##stress_count += 1
    ##return stress_count


st.image("https://images-ext-2.discordapp.net/external/5vie2YzLq-_FaKLK0UsAx-1bMKHuMqV0tLfuoS2Mfe4/https/braincorebismarck.com/wp-content/uploads/2017/05/braincore_icons-02-e1495563799323.png")
st.title("Neuro Journal")
if app_mode == 'Home':
    journal_col, egg_col = st.columns([3,1.5])

    journal = journal_col.text_area("How are you feeling?",placeholder="natHack2022 is ending in 12 hours, but I haven't finished my code!")
    clicked = journal_col.button("Close journal")
    info = egg_col.info("Press 'Start recording' when you have put on your headset")
    record_started = egg_col.button("Start recording")
    if (record_started == True):
        egg_col.image("https://braincorebismarck.com/wp-content/uploads/2017/05/braincore_icons-02-e1495563799323.png")

    if (clicked == True):
        sentences = journal.split(".")
        stress_score = random.randint(1,5)
        if (stress_score < 3):
            st.markdown("It seems like you are stressed right now. We think these music playlists will help you de-stress.")
            tab1, tab2, tab3 = st.tabs(['Nature','Classical','lofi'])
            col1_1,col2_1,col3_1 = tab1.columns(3)
            parse_youtube_link(col1_1,col2_1,col3_1,sounds_of_nature_playlist)
            col1_2,col2_2,col3_2 = tab2.columns(3)
            parse_youtube_link(col1_2,col2_2,col3_2,classical_music_playlist)
            col1_3,col2_3,col3_3 = tab3.columns(3)
            parse_youtube_link(col1_3,col2_3,col3_3,lofi_music_playlist)
        else:
            st.markdown("It seems like you are having a hard time right now. We recommend you contacting the nearest therapist in your area.")
elif app_mode == 'About us':
    st.subheader("About us")
    st.markdown("We are a group of students and graduates who are attempting to create a journaling web app that can detect stress on a quantitative and qualitative level that clinicians as well as therapists can implement. We thought as individuals in academia who are subjected to the dread of stress, this would be an excellent tool to implement on a wider scale and improve care for those under distress.")
    st.subheader("What Neuro Journal does")
    st.markdown("This tool uses a combination of EEG data as well as Natural Language Processing (NLP) to not only biologically quantify points of stress, but also look at key words and phrases on a qualitative level. This can assist in therapy and other applications pertaining to stressful situations.")
    st.subheader("Meet the team")
