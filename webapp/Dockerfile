# Use the official Python image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements.txt for dependency installation
COPY requirements.txt ./ 

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set environment variable to tell Flask it's in production mode
ENV FLASK_ENV=production

# Set the port to 8080, which is what Cloud Run expects
ENV PORT 8080

# Expose port 8080 to the container
EXPOSE 8080

# Set the default command to run when the container starts
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
