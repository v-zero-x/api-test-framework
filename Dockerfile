# Base image for the application
FROM python:3.8-slim as base

WORKDIR /app
COPY . /app

# Install Flask
RUN pip install --no-cache-dir flask

# Application stage
FROM base as application
EXPOSE 5000
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
CMD ["flask", "run"]

# Testing stage
FROM base as tester
RUN pip install pytest requests
COPY --from=application /app /app
CMD ["pytest", "test_api.py"]
