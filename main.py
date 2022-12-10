import streamlit as st
import pandas as pd

header = st.container()
dataset = st.container()

with header:
    st.title('Digital Environmental Footprint Calculator')
    st.text('''
            Quantify the environmental impacts of your Internet consumption habits
            to determine whether and to what degree this could challenge
            a more environmentally sustainable lifestyle
            ''')


with dataset:
    lca_data = pd.read_csv('data/lca_data_digital_content.csv')
    st.write(lca_data)

