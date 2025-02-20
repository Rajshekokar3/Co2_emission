# Handles model prediction

import pandas as pd 
import streamlit as st
import io
import sys
import os

# Get the parent directory (D:\Co2_emission_project)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Add BASE_DIR to sys.path so scripts can be found
sys.path.append(BASE_DIR)

# Now, import your script
from scripts.data_preprocessing import data_preprocess

def predict(vehicle_class, transmission, engine_size, cylinders, car_category, fuel_type, 
            fuel_consumption_city, fuel_consumption_hwy, fuel_consumption_comb, fuel_consumption_comb_mpg):
    
    # Creating a dictionary with user inputs
    data = {
        'vehicle class': vehicle_class,
        'transmission': transmission,
        'Engine size': engine_size,
        'cylinders': cylinders,
        'car_category': car_category,
        'fuel_type': fuel_type,
        'fuel_consumption_city': fuel_consumption_city,
        'fuel_consumption_hwy': fuel_consumption_hwy,
        'fuel_consumption_comb(l/100km)': fuel_consumption_comb,
        'fuel_consumption_comb(mpg)': fuel_consumption_comb_mpg
    }

    # Convert to DataFrame
    df = pd.DataFrame([data])

    # Display in Streamlit
    st.dataframe(df)
    st.write(df.shape)
    buffer = io.StringIO()
    df.info(buf=buffer)
    info_str = buffer.getvalue()
    st.text(info_str)
    data_preprocess(df)