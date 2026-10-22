FROM python:3.11-slim

WORKDIR /app

# Copy model files
COPY backend/xgboost_model.pkl /app/
COPY backend/logistic_regression.pkl /app/

# Copy backend app
COPY backend/app.py /app/

# Copy requirements
COPY requirements.txt /app/

# Install dependencies with retry and specific build tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && pip install --no-cache-dir --upgrade pip setuptools wheel \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get remove -y build-essential \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

# Expose port
EXPOSE 8000

# Run the backend server
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
