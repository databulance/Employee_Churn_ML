# Use the official Python 3.11.5 slim image
FROM python:3.11.5-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Expose the port where Streamlit will run
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "app.py"]
