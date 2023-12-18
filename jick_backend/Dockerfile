# Use an official Python runtime as a parent image
FROM python:3.10
# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that FastAPI will run on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
