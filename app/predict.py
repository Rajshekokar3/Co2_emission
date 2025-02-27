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
from scripts.model_training import model_traning


def predict(vehicle_class, transmission, engine_size, cylinders, car_category, fuel_type,
            fuel_consumption_city, fuel_consumption_hwy, fuel_consumption_comb, fuel_consumption_comb_mpg):
    # Creating a dictionary with user inputs
    data = {
        'vehicle_class': vehicle_class,
        'engine_size': engine_size,
        'cylinders': cylinders,
        'transmission': transmission,
        'fuel_type': fuel_type,
        'fuel_consumption_city': fuel_consumption_city,
        'fuel_consumption_hwy': fuel_consumption_hwy,
        'fuel_consumption_comb(l/100km)': fuel_consumption_comb,
        'fuel_consumption_comb(mpg)': fuel_consumption_comb_mpg,
    }

    # Convert to DataFrame
    df = pd.DataFrame([data])
    st.write(df)
    # Display in Streamlit
    st.write("Verify DataFrame ")
    st.write(f" Shape of Data {df.shape}")
    data_preprocess(df)
    model_traning(df)
