# Data Preprocessing Logic
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import joblib  
from sklearn.preprocessing import StandardScaler



def load_models():
    """Load the pre-trained scaler and label encoders."""
    scaler = joblib.load("../models/Scaler.pkl")  
    encoders = joblib.load("../models/label_ecoder.pkl")  # ✅ Fixed filename
    print("Loaded encoders:", encoders.keys())  #
    return scaler, encoders

# Load models once
scaler, encoders = load_models()

def data_preprocess(df):
    """Preprocess data: Apply label encoding and scaling."""


    # Display processed data
    st.write("✅ Data Preprocessing Done!")
    st.dataframe(pd.DataFrame(df_scaled, columns=df.columns))  

    return df_scaled  # Return preprocessed data
