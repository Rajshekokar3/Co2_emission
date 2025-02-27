# Model Training Logic
import joblib
import streamlit as st
import pickle

@st.cache_resource
def load_model():
    with open("../scripts/best_model.pkl",'rb') as file:
        model=pickle.load(file)
    return model


model=load_model()

def model_traning(df):
    prediction=model.predict(df)
    return prediction