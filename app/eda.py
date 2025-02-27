import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def explore():
# File uploader
    st.title("📊 EDA on Uploaded Dataset")
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])


    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)  # Read CSV
            st.write("📊 **Dataset Loaded Successfully!**")
            st.write(df.head())  # Display first few rows
        except Exception as e:
            st.error(f"❌ Error reading file: {e}")


        # Display the first few rows of the dataset
        st.subheader("🔍 Data Preview")
        st.write(df.head())

        # Show basic statistics
        st.subheader("📌 Data Summary")
        st.write(df.describe())

        # Choose EDA type
        st.subheader("📊 Select EDA Analysis")

        eda_option = st.selectbox("Choose EDA Graph Type",
                                  ["Histogram", "Pair Plot", "Correlation Heatmap"])

        # Plot based on selection
        if eda_option == "Histogram":
            st.subheader("📈 Histograms of Numerical Columns")
            for col in df.select_dtypes(include=['int64', 'float64']).columns:
                fig, ax = plt.subplots()
                sns.histplot(df[col], kde=True, bins=30, ax=ax)
                st.pyplot(fig)

        elif eda_option == "Pair Plot":
            st.subheader("📊 Pair Plot of Features")
            fig = sns.pairplot(df)
            st.pyplot(fig)

        elif eda_option == "Correlation Heatmap":
            st.subheader("🔥 Correlation Heatmap")
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.heatmap(df.corr(), annot=True, cmap="coolwarm", linewidths=0.5, ax=ax)
            st.pyplot(fig)
