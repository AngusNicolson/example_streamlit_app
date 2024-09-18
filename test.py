import numpy as np
import pandas as pd
import streamlit as st 
from sklearn import preprocessing
import pickle

model = lambda x: 42

def main(): 
    st.title("Income Predictor")
    html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Income Prediction App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)
    
    data = st.file_uploader("Accelerometer Data", "csv")
    if st.button("Predict"): 
        
        features = []
        print(data)

 
        prediction = model(features)
    
        output = int(prediction)
        if output == 1:
            text = ">50K"
        else:
            text = "<=50K"

        st.success('Employee Income is {}'.format(text))
      
if __name__=='__main__': 
    main()
