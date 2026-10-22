FROM python:3.11-slim

WORKDIR /app

# Copy model files
COPY backend/xgboost_model.pkl ./
COPY backend/logistic_regression.pkl ./

# Copy backend app
COPY backend/app.py ./

# Copy requirements
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8000

# Run the backend server
CMD exec uvicorn app:app --host 0.0.0.0 --port ${PORT:-8000}
