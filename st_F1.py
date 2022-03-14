import streamlit as st
import pandas as pd
import numpy as np
from sklearn import datasets

st.title('Water Quality Analysis')
st.image("water.jpg")

ra=st.sidebar.radio('Select an option',['Analysis','Prediction'])
if ra == "Analysis":

    #    "Analysis"
    rad = st.sidebar.selectbox('Select a State', ['Andhra Pradesh', 'TamilNadu'])

    # This is for Ap data
    if rad == 'Andhra Pradesh':
        st.subheader("Andhra Pradesh Water Analysis")
        df = pd.read_csv("C:/Users/somas/OneDrive/Desktop/F_WQI_Ap_jan_2021.csv")
        # st.write(df)
        if st.checkbox('View dataset'):
            st.write(df)

        st.bar_chart(df)

    # This is for Tamilnadu
    if rad == 'TamilNadu':
        st.subheader("TamilNadu Water Analysis")
        df = pd.read_csv("C:/Users/somas/OneDrive/Desktop/F_WQI_Ap_jan_2021.csv")
        # st.write(df)
        if st.checkbox('View dataset'):
            st.write(df)
        st.line_chart(df)

if ra== "Prediction":
    st.write('Prediction')
    pre = st.sidebar.selectbox('Select a State', ['KNN', 'SVM','Random Forest','Desicion tress'])

    if pre == 'KNN':
        st.write('KNN')
        #fit the knn algorithm here


    if pre == 'SVM':
        st.write('SVM')
        ##fit the SVM algorithm here