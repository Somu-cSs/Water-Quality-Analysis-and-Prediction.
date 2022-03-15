import streamlit as st
import pandas as pd
import numpy as np


ra=st.sidebar.radio('Select an option',['Analysis','Prediction'])
if ra == "Analysis":
    st.title('Water Quality Analysis')
    st.image("water_quality_mason_jar.jpg")

    #    "Analysis"
    rad = st.sidebar.selectbox('Select a State', ['Andhra Pradesh', 'TamilNadu'])

    # This is for Ap data
    if rad == 'Andhra Pradesh':
        st.subheader("Andhra Pradesh Water Analysis")
        #st.markdown(“link copied from powerbi web service”,unsafe_allow_html=True) to load a PowerBi Dashboard
        #df = pd.read_csv("C:/Users/somas/OneDrive/Desktop/F_WQI_Ap_jan_2021.csv")
        df = pd.read_csv("https://github.com/Somu-uchisa/WQI_Streamlit/blob/main/AP_January_2021.csv")
        # st.write(df)
        if st.checkbox('View dataset'):
            st.write(df)

        st.bar_chart(df)

    # This is for Tamilnadu
    if rad == 'TamilNadu':
        st.subheader("TamilNadu Water Analysis")
        df = pd.read_csv("https://github.com/Somu-uchisa/WQI_Streamlit/blob/main/AP_January_2021.csv")
        # st.write(df)
        if st.checkbox('View dataset'):
            st.write(df)
        st.line_chart(df)

if ra== "Prediction":
    #st.title('Water Quality Prediction')
    st.image("pre.jpg")

    st.write('Prediction')
    pre = st.sidebar.selectbox('Select a State', ['KNN', 'SVM','Random Forest','Desicion tress'])

    if pre == 'KNN':
        st.write('KNN')
        #fit the knn algorithm here


    if pre == 'SVM':
        st.write('SVM')
        ##fit the SVM algorithm here
