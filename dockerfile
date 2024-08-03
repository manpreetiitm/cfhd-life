# Use the official Python image
FROM python:3.9

# Set the working directory
WORKDIR /usr/src/app

# Copy the requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app.py ./

# Expose the application port
EXPOSE 5000

# Start the Flask application
CMD ["python", "app.py"]
