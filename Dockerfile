# Use an official Python runtime as the base image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python and opencv dependencies
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set Roboflow API key
ENV ROBOFLOW_API_KEY set_via_docker_run
ENV FRAMES_PATH=/frames

# Folder for images
RUN mkdir ${FRAMES_PATH}

# Set the command to run your application
CMD [ "python", "main.py" ]