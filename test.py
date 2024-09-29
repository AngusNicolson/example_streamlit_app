import numpy as np
import pandas as pd
import streamlit as st 
import joblib
import features
# If streamlit doesn't have a package by default, you will need to create a requirements.txt file in your github and add the package name to it. 
# See the requirements.txt file in this github repository for an example.

# 3. Replace this with code to load our model! 
# hint: use joblib
# You will need to upload the model to your github before it can be loaded in the app
model = lambda x: 42

def main(): 
    # This section just makes the app look prettier
    # Replace the titles with something more appropriate
    # Feel free to play around with the style if you want to change how it looks
    st.title("Income Predictor")
    html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Income Prediction App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)

    # 1. This line uploads the accelerometer data from the user
    # This is done. 
    # For now, when you want to test the app, just upload one of the .csv files from Capture24
    data = st.file_uploader("Accelerometer Data", "csv")

    # This code only runs once the button labelled "Predict" is clicked in the app
    if st.button("Predict"): 

        # 2. Here is where you need to add code to convert the raw xyz data into features
        # hint: use the method features.extract_features. To do this you will need to upload features.py (its on our shared drive) to your github
        features = []

        # 4. This is where the model actually makes its predictions
        # You will need to change this to model.predict, once you've setup the 
        prediction = model(features)

        # 5. Here is where we create an output to display to the user
        # Currently, it just returns some text. 
        # Instead, we want to create the figures showing participant activity over time (Similar to plot_compare() in the notebook)
        # I don't actually know how to display images in streamlit yet, you will need to look this up
        output = int(prediction)
        if output == 1:
            text = ">50K"
        else:
            text = "<=50K"

        st.success('Employee Income is {}'.format(text))
      
if __name__=='__main__': 
    main()
