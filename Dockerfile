FROM python:3.11-slim

WORKDIR /app

# Copy model files
COPY backend/xgboost_model.pkl /app/
COPY backend/logistic_regression.pkl /app/

# Copy backend app
COPY backend/app.py /app/

# Copy requirements
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8000

# Run the backend server
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
