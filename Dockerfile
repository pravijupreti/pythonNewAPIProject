# Use the official Python image as base
FROM python:3.11.0

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file into the container at /code
COPY requirements.txt .

# Install dependencies
RUN apt-get update && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt


# Copy the entire project directory into the container at /code
COPY . .

# Expose port 1234 to the outside world
EXPOSE 1234

# Command to run the application
CMD ["uvicorn", "index:app", "--host", "0.0.0.0", "--port", "1234"]
