# Use the official Python image as the base image
FROM python:3.13-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application files into the container
COPY . /app

# Install uv (package manager) and dependencies
RUN pip install --no-cache-dir uv
RUN uv sync

# Ensure the database configuration is correct and initialize the database
RUN cp app/conf/config_template.ini app/conf/config.ini \
    && sed -i 's|path/to/logs|/app/logs|g' app/conf/config.ini \
    && sed -i 's|path/to/log/conf|/app/app/conf/logging.ini|g' app/conf/config.ini \
    && sed -i 's|your/path/to/app/db/database.db|/app/app/db/database.db|g' app/conf/config.ini \
    && mkdir -p /app/logs \
    && python app/utils/initDB.py

# Expose the port the app runs on
EXPOSE 8000

# Command to run the FastAPI application
CMD ["uv", "run", "fastapi", "dev"]