# Use the official Python image as the base image
FROM python:3.13-slim

# Set the working directory in the container
WORKDIR /boilerplate

# Copy the application files into the container
COPY . /boilerplate

# Create folders and position files correctly
RUN mkdir -p /logs
RUN touch app/core/db/database.db
RUN cp app/conf/config_docker.ini app/conf/config.ini

# Install uv (package manager) and system dependencies
RUN pip install --no-cache-dir uv
RUN apt-get update
# These system packages are necessary per the mysqlclient python package documentation
RUN apt-get install default-libmysqlclient-dev build-essential pkg-config -y
RUN uv sync

# Ensure the database configuration is correct and initialize the database
RUN uv run app/utils/initDB.py

# Expose the port the app runs on
EXPOSE 8000

# Command to run the FastAPI application
CMD ["uv", "run", "fastapi", "run"]