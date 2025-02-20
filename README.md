# 🚗 CO2 Emission Prediction

This project predicts **CO2 emissions** based on vehicle specifications such as engine size, fuel type, transmission, and vehicle class.

## 📌 Features
- Data preprocessing with **label encoding & scaling**
- Machine learning model to predict CO2 emissions
- **Streamlit** interface for easy interaction
- **Deployed model** for real-time predictions

## 🛠️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/CO2-Emission-Prediction.git
   cd CO2-Emission-Prediction

CO2-Emission-Prediction/
│── app/

│   ├── main.py                # Streamlit UI
│   ├── model_predict.py        # Model prediction script
│── scripts/
│   ├── data_preprocessing.py   # Data preprocessing logic
│── models/
│   ├── Scaler.pkl              # Pre-trained scaler
│   ├── label_encoder.pkl       # Label encoders
│── data/
│   ├── dataset.csv             # Training dataset
│── requirements.txt            # Dependencies
│── README.md                   # Project documentation

## 📊 Model Training
The model was trained using Random Forest for optimal accuracy.
The dataset includes 7385 rows with 12 features.
## 🎯 Usage
Upload a dataset or enter values manually.
The model processes inputs and predicts CO2 emissions.
View results and analyze trends.
## 💡 Future Enhancements
Add more ML models for comparison.
Deploy using Flask/Django for API integration.
Improve UI with better data visualization.
## 🤝 Contributing
Pull requests are welcome! Fork the repo and submit your PR.
