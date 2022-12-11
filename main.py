import streamlit as st
import pandas as pd

header = st.container()
user_input = st.container()

with header:
    st.title('Digital Carbon Footprint Calculator')
    st.text('''
            Determine the climate impacts of your Internet consumption habits
            ''')

list_of_countries = ['Global', 'Brazil', 'Canada', 'China', 'India', 'United States', 'Norway',
                     'Switzerland', 'France', 'Denmark', 'Spain', 'Italy', 'Germany', 'Poland',
                     'United Kingdom', 'South Africa', 'Australia', 'Russia']

with user_input:
    st.header('Introduce your Internet consumption behavior')

    sel_col, disp_col = st.columns(2)

    # User location
    user_loc = sel_col.selectbox('Select your country', options = sorted(list_of_countries), index='Global')
    st.markdown('*If your country is not in the list, please select "Global"*')


    lca_data = pd.read_csv('data/lca_data_digital_content.csv')
    st.write(lca_data)

