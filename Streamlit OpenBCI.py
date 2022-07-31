from ast import Import
from asyncore import write
from email import header
from tkinter import font
from turtle import position, width
from urllib.request import urlopen
import streamlit as st
import numpy as np
from PIL import Image
import pandas as pd
import os

st.set_page_config(layout="wide")

data1 = pd.read_csv(r'C:\Users\gurmo\OneDrive\Documents\GitHub\NatHacks2022\EEG_stress_test_bird_misson_8min.csv')

data2 = pd.read_csv(r"C:\Users\gurmo\OneDrive\Documents\GitHub\NatHacks2022\EEG_stress_test_tcmt_misson_round1.csv")
 
data3 = pd.read_csv(r'C:\Users\gurmo\OneDrive\Documents\GitHub\NatHacks2022\sai_resting.csv')
 
#data4 = pd.read_csv(r"C:\Users\gurmo\OneDrive\Desktop\Sait 2022\Capstone Project Anooka Health\python\controversialkneepain.csv")
 
col1, col2 = st.columns([6,4])
col1.table(data1)
col2.table(data2)

#col3, col4, col5 = st.columns([3,3,4])
#col3.table(data3)
#col4.table(data4)
#col5.table(data5)
 