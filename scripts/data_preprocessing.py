# Data Preprocessing Logic

import joblib 


def load_models():
    """Load the pre-trained scaler and label encoders."""
    scaler = joblib.load("../models/scaler.pkl")
    encoders = joblib.load("../models/label_ecoder.pkl")  # ✅ Fixed filename #
    return scaler, encoders 

# Load models once
scaler, encoders = load_models()


def data_preprocess(df):
    for col in df.columns:
        if col in encoders:  # Check if the column has an encoder
            df[col] = df[col].apply(lambda x: encoders[col].transform([x])[0] if x in encoders[col].classes_ else -1)
    input=scaler.transform(df)
    return(input)