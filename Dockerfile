# Start with the base Python 3.8 slim image
FROM python:3.8-slim

# Set the working directory inside the container
RUN mkdir -p /app && chown -R 1001:0 /app
WORKDIR /app

# (Switch to non-root user if applicable)
#USER 1001

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies from the requirements.txt file
RUN pip install --use-deprecated=legacy-resolver -r requirements.txt

# Copy the rest of the application files into the container
COPY . .

# Command to run the application (you can modify this based on your project)
CMD ["python", "bot.py"]  