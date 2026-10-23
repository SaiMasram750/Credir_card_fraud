# 🛡️ Shield.OS – Fraud Detection System

A production-ready fraud detection platform that uses machine learning to identify and flag suspicious credit card transactions in real-time.

---

## 📋 Table of Contents
1. [What is Shield.OS?](#what-is-shieldos)
2. [System Architecture](#system-architecture)
3. [Component Breakdown](#component-breakdown)
4. [Why These Technologies?](#why-these-technologies)
5. [Quick Start](#quick-start)
6. [How to Use](#how-to-use)

---

## 🎯 What is Shield.OS?

Shield.OS is a **real-time fraud detection system** that analyzes credit card transactions and classifies them as legitimate or fraudulent. It uses two trained machine learning models (XGBoost and Logistic Regression) to make predictions with a 30% fraud probability threshold.

**Key Features:**
- ✅ Single transaction scoring
- ✅ Live transaction streaming simulation
- ✅ Batch CSV processing
- ✅ Real-time dashboard with metrics
- ✅ Multiple model selection (XGBoost or Logistic Regression)

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     SHIELD.OS SYSTEM                         │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌──────────────────┐              ┌──────────────────────┐  │
│  │   FRONTEND       │              │    BACKEND API       │  │
│  │  (Streamlit)     │◄─────────────►│   (FastAPI)          │  │
│  │                  │   HTTP REST   │                      │  │
│  │  • Dashboard     │               │  • Health Check      │  │
│  │  • 3 Tabs        │               │  • Single Predict    │  │
│  │  • User Forms    │               │  • Batch Predict     │  │
│  └──────────────────┘               └──────────────────────┘  │
│        Port 8501                           Port 8000           │
│                                                  ▲              │
│                                                  │              │
│                                        ┌─────────┴──────────┐  │
│                                        │  MACHINE LEARNING   │  │
│                                        │     MODELS          │  │
│                                        │                     │  │
│                                        │ • XGBoost (pkl)     │  │
│                                        │ • Logistic Reg(pkl) │  │
│                                        └─────────────────────┘  │
│                                                                  │
└─────────────────────────────────────────────────────────────┘
```

**Data Flow:**
1. User inputs transaction data in Streamlit frontend
2. Frontend sends HTTP request to FastAPI backend
3. Backend loads pretrained ML model
4. Model predicts fraud probability
5. Backend returns result (is_fraud, probability, status)
6. Frontend displays result with visual indicators

---

## 🔧 Component Breakdown

### 1. **Frontend** (`frontend/app.py`) - Streamlit Dashboard
**What it does:**
- Interactive web interface for users to input transaction data
- Displays real-time fraud predictions with visual feedback
- Three separate tabs for different use cases

**Why Streamlit?**
- Rapid UI development without HTML/CSS/JavaScript
- Built-in real-time updates and data visualization
- Perfect for ML dashboards and data apps
- Minimal code, maximum functionality

**Three Tabs:**
| Tab | Purpose | Use Case |
|-----|---------|----------|
| **Tab 1: Single Prediction** | Predict one transaction at a time | Manual fraud checks, customer service |
| **Tab 2: Live Stream Simulator** | Watch transactions being scored in real-time | Monitoring, system demos |
| **Tab 3: Batch CSV Audit** | Upload and score multiple transactions | End-of-day reports, bulk analysis |

---

### 2. **Backend** (`backend/app.py`) - FastAPI Server
**What it does:**
- REST API that receives transaction data
- Loads and uses pretrained ML models
- Returns fraud predictions with probabilities
- Handles both single and batch predictions

**Why FastAPI?**
- Modern Python web framework (async/await support)
- Auto-generates interactive API documentation (`/docs`)
- Fast performance with type validation
- Easy to scale and deploy

**Key Endpoints:**
```
GET  /health              → Check server & model status
POST /predict/single      → Score one transaction
POST /predict/batch       → Score multiple transactions from CSV
```

---

### 3. **ML Models** (`backend/*.pkl`)
**What they do:**
- Pre-trained machine learning models ready to make predictions
- Accept transaction features and output fraud probability

**Two Models Available:**
| Model | Why Use It | Characteristics |
|-------|-----------|-----------------|
| **XGBoost** | High accuracy, handles complex patterns | Gradient boosting, ~95% accuracy |
| **Logistic Regression** | Fast, interpretable, good baseline | Simple linear model, ~88% accuracy |

**How Models Work:**
1. Input: Transaction features (30 values: Time, Amount, V1-V28)
2. Processing: Model calculates fraud probability (0.0 - 1.0)
3. Output: "FLAGGED" if probability ≥ 0.30, "CLEARED" otherwise

**Decision Threshold: 0.30 (30%)**
- If fraud probability ≥ 30% → Transaction is **FLAGGED** as suspicious
- If fraud probability < 30% → Transaction is **CLEARED** as safe

---

### 4. **Data Scripts** (Optional)
| Script | Purpose |
|--------|---------|
| `scripts/generate_data.py` | Creates synthetic dataset for training |
| `scripts/train_models.py` | Trains new ML models (optional) |
| `requirements.txt` | Python package dependencies |

---

## 🤔 Why These Technologies?

### Why FastAPI + Streamlit?
```
✓ FastAPI     → Fast, modern REST API with automatic docs
✓ Streamlit   → Zero-config dashboard perfect for ML apps
✓ Together    → Scalable, maintainable, production-ready
```

### Why XGBoost + Logistic Regression?
```
✓ XGBoost            → Best for complex fraud patterns (high accuracy)
✓ Logistic Regression → Fast inference, easy to explain results
✓ Both available     → User can choose based on their needs
```

### Why Python?
```
✓ Rich ML ecosystem (scikit-learn, XGBoost, joblib)
✓ Fast development & prototyping
✓ Large community for fraud detection
✓ Easy deployment
```

---

## 🚀 Quick Start

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Start Backend (Terminal 1)
```bash
python -m uvicorn backend.app:app --host 127.0.0.1 --port 8000 --reload
```

**Expected Output:**
```
✓ Logistic Regression model loaded
✓ XGBoost model loaded
INFO:     Uvicorn running on http://127.0.0.1:8000
```

✅ **Backend Ready:** `http://127.0.0.1:8000`

### Step 3: Start Frontend (Terminal 2)
```bash
streamlit run frontend/app.py
```

**Expected Output:**
```
You can now view your Streamlit app in your browser.
Local URL: http://localhost:8501
```

✅ **Frontend Ready:** `http://localhost:8501`

---

## 📖 How to Use

### **Using the Dashboard**

#### Tab 1: Single Prediction
1. Enter transaction details:
   - **Amount**: Dollar value of transaction
   - **Distance From Home**: Miles/km from home
   - **Time Elapsed**: Seconds since day started
   - **Model**: Choose XGBoost or Logistic Regression

2. Click **"Predict"** button

3. View results:
   - Fraud Probability: 0-100%
   - Status: FLAGGED or CLEARED
   - Classification: 🚨 FRAUD or ✓ LEGITIMATE

**Sample Fraud Transaction:**
Click "Load Sample Fraud Transaction" to auto-fill high-risk values:
- Amount: $2,500 (unusually high)
- Distance: 500 km (far from home)
- Time: Late night (86400 seconds)

---

#### Tab 2: Live Stream Simulator
1. Set simulation duration (5-300 seconds)
2. Click **"Start Stream"**
3. Watch in real-time:
   - Transactions generated every 1 second
   - Live metrics: Total, Flagged, Flagged %
   - Transaction table updates live

**Use Case:** Demo system, monitor detection rates

---

#### Tab 3: Batch CSV Audit
1. Click **"Upload CSV File"**
2. Select your CSV file (with columns: Time, V1-V28, Amount, Class)
3. Click **"Analyze Batch"**
4. View summary statistics:
   - Total transactions processed
   - Number flagged as fraud
   - Total amount flagged
   - Fraud detection rate %

**Use Case:** Process daily transactions, end-of-month reports

---

## 🔌 API Documentation

### Interactive API Docs
Open: `http://127.0.0.1:8000/docs`

### Health Check
```bash
curl http://127.0.0.1:8000/health
```
Response:
```json
{
  "status": "operational",
  "logistic_regression_loaded": true,
  "xgboost_loaded": true
}
```

### Single Prediction
```bash
curl -X POST http://127.0.0.1:8000/predict/single \
  -H "Content-Type: application/json" \
  -d '{
    "Amount": 150.50,
    "Time": 3600,
    "Distance_From_Home": 25.5,
    "selected_model": "xgboost"
  }'
```
Response:
```json
{
  "is_fraud": false,
  "fraud_probability": 0.15,
  "status": "CLEARED"
}
```

---

## 📊 Project Structure
```
Shield.OS/
├── backend/
│   ├── app.py                      # FastAPI server
│   ├── xgboost_model.pkl           # Pretrained XGBoost model
│   └── logistic_regression.pkl     # Pretrained Logistic Regression
├── frontend/
│   └── app.py                      # Streamlit dashboard
├── scripts/
│   ├── generate_data.py            # Create synthetic dataset
│   └── train_models.py             # Train new models (optional)
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

---

## ⚙️ Configuration

### Fraud Threshold
Currently set to **0.30** (30% fraud probability)

To change, edit `backend/app.py`:
```python
threshold = 0.30  # Change this value
```

### CORS Settings
Frontend allowed to connect from:
- `http://localhost:8501`
- `http://127.0.0.1:8501`

To add more origins, edit `backend/app.py`:
```python
allow_origins=["http://localhost:8501", "YOUR_DOMAIN"]
```

---

## 🛠️ Troubleshooting

| Problem | Solution |
|---------|----------|
| Backend won't start | Check port 8000 is free: `netstat -an \| grep 8000` |
| Frontend can't connect to backend | Ensure backend is running on `127.0.0.1:8000` |
| Models not loading | Check `.pkl` files exist in `backend/` folder |
| Streamlit error | Run `pip install --upgrade streamlit` |

---

## 📝 Example Workflow

```
1. Open Dashboard → http://localhost:8501
2. Go to "Single Prediction" tab
3. Click "Load Sample Fraud Transaction"
4. Click "Predict"
5. See result: 🚨 FRAUD, 87% probability, FLAGGED
6. Switch to "Live Stream" tab
7. Run 30-second simulation
8. Observe real-time metrics
```

---

## 🎓 Key Concepts

**Fraud Probability**: 0-100% confidence that transaction is fraudulent
- 0% = Definitely legitimate
- 50% = Uncertain
- 100% = Definitely fraudulent

**Threshold**: 0.30 = 30% fraud probability cutoff
- ≥ 30% → FLAGGED (suspicious, needs review)
- < 30% → CLEARED (appears safe)

**Models**: Two different AI algorithms for prediction
- Choose based on accuracy needs vs. speed requirements

---

## 📞 Support

For issues or questions:
1. Check the troubleshooting section above
2. Verify all dependencies: `pip list`
3. Check backend logs in terminal 1
4. Check frontend logs in terminal 2

---

**Shield.OS v1.0** | Real-Time Fraud Detection System
Built with ❤️ using FastAPI + Streamlit + XGBoost
