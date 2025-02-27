import streamlit as st 
import pandas as pd 
import numpy as np

from eda import explore
from predict import predict
import pathlib

def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Load the external CSS
css_path = pathlib.Path("../static/css/styles.css")
load_css(css_path)


st.title("CO2-EMISSION")
st.html(
    '<p class="custom-markdown">This project predicts CO₂ emissions using machine learning models based on car engine features.</p>'
)
if "show inputs" not in st.session_state:
    st.session_state.show_inputs= False


def show_input():
    st.session_state.show_inputs=True

st.button("User Input",on_click=show_input())



if st.session_state.show_inputs:
        st.sidebar.header("Feature Details")

        # Variables
        vehicle_class = st.sidebar.selectbox('Vehicle Class',
                                             ('COMPACT', 'SUV - SMALL', 'MID-SIZE', 'TWO-SEATER', 'MINICOMPACT',
                                              'SUBCOMPACT', 'FULL-SIZE', 'STATION WAGON - SMALL',
                                              'SUV - STANDARD', 'VAN - CARGO', 'VAN - PASSENGER',
                                              'PICKUP TRUCK - STANDARD', 'MINIVAN', 'SPECIAL PURPOSE VEHICLE',
                                              'STATION WAGON - MID-SIZE', 'PICKUP TRUCK - SMALL'),
                                             key="vehicle_class_select1",index=None,placeholder="Select"
                                             )

        engine_size = st.sidebar.slider("Engine Size", 1, 9,value=None)
        cylinders = int(st.sidebar.slider("Cylinders", 3, 16,value=None))
        transmission = str(st.sidebar.selectbox("Transmission", ('AS', 'M', 'AV', 'AM', 'A'), key="transmission_select2",index=None,placeholder="Select "))
        fuel_type = str(st.sidebar.selectbox("Fuel Type", ('Z', 'D', 'X', 'E', 'N'), key="fuel_type_select3",index=None,placeholder="Select"))

        # Fixed selectbox format
        car_category = st.sidebar.selectbox(
            "Car Categories",["Small Car (Compact)", "Midsize Car", "SUV / Crossover", "Heavy-Duty / Truck"],key="car_category_select4",index=None,placeholder="Select")

        fuel_consumption_city = int(st.sidebar.slider("Fuel consumption city", 4, 35,value=None))
        fuel_consumption_hwy = int(st.sidebar.slider("Fuel consumption hwy", 4, 35,value=None))  # Fixed missing argument
        fuel_consumption_comb = int(st.sidebar.slider("Fuel consumption comb(l/100km)", 4, 30,value=None))
        fuel_consumption_comb_mpg = int(st.sidebar.slider("Fuel consumption comb(mpg)", 11, 70,value=None))

        # mapping
        car_category_mapping = {
            "Small Car (Compact)": 0,"Midsize Car": 1,"SUV / Crossover": 2,"Heavy-Duty / Truck": 3}
        transmission_mapping = {'AS': 0,'M': 1,'AV': 2,'AM': 3,'A': 4}
        vehicle_class_mapping = {
            'COMPACT': 0,'SUV - SMALL': 1,'MID-SIZE': 2,'TWO-SEATER': 3,'MINICOMPACT': 4,'SUBCOMPACT': 5,'FULL-SIZE':6,'STATION WAGON - SMALL': 7,'SUV - STANDARD': 8,'VAN - CARGO': 9,'VAN - PASSENGER': 10,'PICKUP TRUCK - STANDARD': 11,'MINIVAN': 12,'SPECIAL PURPOSE VEHICLE': 13,'STATION WAGON - MID-SIZE': 14,'PICKUP TRUCK - SMALL': 15}
        fuel_type = {
            'Z': 0,
            'D': 1,
            'X': 2,
            'E': 3,
            'N': 4
        }

        numeric_vehicle = vehicle_class_mapping.get(vehicle_class, 1)
        numeric_trans = transmission_mapping.get(vehicle_class, 1)
        numeric_car = car_category_mapping.get(vehicle_class, 1)
        numeric_type = fuel_type.get(vehicle_class, 1)

        if st.button("Predict",key="wheat"):
            predict(numeric_vehicle,numeric_trans, engine_size, cylinders,numeric_car,numeric_type,fuel_consumption_city, fuel_consumption_hwy, fuel_consumption_comb, fuel_consumption_comb_mpg)


#if st.button("EDA",key="grey"):
    #explore()
