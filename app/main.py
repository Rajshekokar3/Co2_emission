import streamlit as st 
import pandas as pd 
import numpy as np  

st.title("CO2-EMISSION")
st.header("This is a predictive model with user input")

st.sidebar.header("Feature Details")

# Variables
vehicle_class = st.sidebar.selectbox('Vehicle Class',
    ('COMPACT', 'SUV - SMALL', 'MID-SIZE', 'TWO-SEATER', 'MINICOMPACT',
     'SUBCOMPACT', 'FULL-SIZE', 'STATION WAGON - SMALL',
     'SUV - STANDARD', 'VAN - CARGO', 'VAN - PASSENGER',
     'PICKUP TRUCK - STANDARD', 'MINIVAN', 'SPECIAL PURPOSE VEHICLE',
     'STATION WAGON - MID-SIZE', 'PICKUP TRUCK - SMALL'),
    key="vehicle_class_select1"
)

engine_size = st.sidebar.slider("Engine Size", 1, 9)
cylinders =int( st.sidebar.slider("Cylinders", 3, 16))
transmission = str(st.sidebar.selectbox("Transmission", ('AS', 'M', 'AV', 'AM', 'A'), key="transmission_select2"))
fuel_type = str(st.sidebar.selectbox("Fuel Type", ('Z', 'D', 'X', 'E', 'N'), key="fuel_type_select3"))

# Fixed selectbox format
car_category = st.sidebar.selectbox(
    "Car Categories",
    ["Small Car (Compact)", "Midsize Car", "SUV / Crossover", "Heavy-Duty / Truck"],
    key="car_category_select4"
)

fuel_consumption_city = int(st.sidebar.slider("Fuel consumption city", 4, 35))
fuel_consumption_hwy = int(st.sidebar.slider("Fuel consumption hwy", 4, 35))  # Fixed missing argument
fuel_consumption_comb = int(st.sidebar.slider("Fuel consumption comb(l/100km)", 4, 30))
fuel_consumption_comb_mpg =int(st.sidebar.slider("Fuel consumption comb(mpg)", 11, 70))



if st.button("Predict"):
    from model_predict import predict
    predict(vehicle_class, transmission, engine_size, cylinders, car_category, fuel_type, 
            fuel_consumption_city, fuel_consumption_hwy, fuel_consumption_comb, fuel_consumption_comb_mpg)
