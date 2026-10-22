from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd
from pathlib import Path
from typing import Optional, List
import io

app = FastAPI(title="Shield.OS Fraud Detection API")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8501", "127.0.0.1:8501"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load models from backend directory
BACKEND_DIR = Path(__file__).parent
lr_model = None
xgb_model = None

print(f"Loading models from: {BACKEND_DIR}")
print(f"Files in directory: {list(BACKEND_DIR.glob('*.pkl'))}")

try:
    lr_path = BACKEND_DIR / "logistic_regression.pkl"
    if lr_path.exists():
        lr_model = joblib.load(lr_path)
        print("✓ Logistic Regression model loaded successfully")
    else:
        print(f"⚠ Logistic Regression file not found at {lr_path}")
except Exception as e:
    print(f"⚠ Error loading Logistic Regression: {e}")

try:
    xgb_path = BACKEND_DIR / "xgboost_model.pkl"
    if xgb_path.exists():
        xgb_model = joblib.load(xgb_path)
        print("✓ XGBoost model loaded successfully")
    else:
        print(f"⚠ XGBoost file not found at {xgb_path}")
except Exception as e:
    print(f"⚠ Error loading XGBoost: {e}")

# Request/Response models
class TransactionRequest(BaseModel):
    Amount: float
    Time: float
    Distance_From_Home: float = 0.0
    selected_model: str = "xgboost"
    V1: Optional[float] = 0.0
    V2: Optional[float] = 0.0
    V3: Optional[float] = 0.0
    V4: Optional[float] = 0.0
    V5: Optional[float] = 0.0
    V6: Optional[float] = 0.0
    V7: Optional[float] = 0.0
    V8: Optional[float] = 0.0
    V9: Optional[float] = 0.0
    V10: Optional[float] = 0.0
    V11: Optional[float] = 0.0
    V12: Optional[float] = 0.0
    V13: Optional[float] = 0.0
    V14: Optional[float] = 0.0
    V15: Optional[float] = 0.0
    V16: Optional[float] = 0.0
    V17: Optional[float] = 0.0
    V18: Optional[float] = 0.0
    V19: Optional[float] = 0.0
    V20: Optional[float] = 0.0
    V21: Optional[float] = 0.0
    V22: Optional[float] = 0.0
    V23: Optional[float] = 0.0
    V24: Optional[float] = 0.0
    V25: Optional[float] = 0.0
    V26: Optional[float] = 0.0
    V27: Optional[float] = 0.0
    V28: Optional[float] = 0.0

class PredictionResponse(BaseModel):
    is_fraud: bool
    fraud_probability: float
    status: str

class HealthResponse(BaseModel):
    status: str
    logistic_regression_loaded: bool
    xgboost_loaded: bool

class BatchPredictionResponse(BaseModel):
    total_transactions: int
    flagged_count: int
    flagged_amount: float

@app.get("/health", response_model=HealthResponse)
def health_check():
    return {
        "status": "operational",
        "logistic_regression_loaded": lr_model is not None,
        "xgboost_loaded": xgb_model is not None,
    }

@app.post("/predict/single", response_model=PredictionResponse)
def predict_single(request: TransactionRequest):
    if xgb_model is None and lr_model is None:
        raise HTTPException(status_code=503, detail="Models not loaded")
    
    # Construct feature vector
    features = [request.Time] + [getattr(request, f'V{i}', 0.0) for i in range(1, 29)] + [request.Amount]
    X = np.array(features).reshape(1, -1)
    
    # Select model
    model = xgb_model if request.selected_model.lower() == "xgboost" else lr_model
    
    if model is None:
        raise HTTPException(status_code=503, detail=f"Model {request.selected_model} not loaded")
    
    # Get prediction and probability
    prediction = model.predict(X)[0]
    probability = model.predict_proba(X)[0][1]
    
    # Decision threshold: 0.30
    threshold = 0.30
    is_fraud = probability >= threshold
    status = "FLAGGED" if is_fraud else "CLEARED"
    
    return {
        "is_fraud": bool(is_fraud),
        "fraud_probability": float(probability),
        "status": status,
    }

@app.post("/predict/batch", response_model=BatchPredictionResponse)
async def predict_batch(file: UploadFile = File(...)):
    if xgb_model is None:
        raise HTTPException(status_code=503, detail="XGBoost model not loaded")
    
    try:
        contents = await file.read()
        df = pd.read_csv(io.StringIO(contents.decode('utf-8')))
        
        # Extract features
        X = df.drop('Class', axis=1, errors='ignore')
        
        # Get predictions
        predictions = xgb_model.predict(X)
        probabilities = xgb_model.predict_proba(X)[:, 1]
        
        # Apply threshold
        threshold = 0.30
        flagged = probabilities >= threshold
        
        # Calculate statistics
        total_transactions = len(df)
        flagged_count = int(np.sum(flagged))
        flagged_amount = float(df[flagged]['Amount'].sum()) if flagged_count > 0 else 0.0
        
        return {
            "total_transactions": total_transactions,
            "flagged_count": flagged_count,
            "flagged_amount": flagged_amount,
        }
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing file: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
