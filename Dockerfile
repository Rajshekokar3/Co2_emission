# Use official Python image
FROM python:3.9

# Set working directory inside the container
WORKDIR /app

# Copy files to container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Streamlit port (if using Flask, change to 5000)
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "app/main.py", "--server.port=8501", "--server.address=0.0.0.0"]
