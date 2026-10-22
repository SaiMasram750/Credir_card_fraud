# 🚀 Deploy Backend Only to Google Cloud - Simple Steps

Deploy just the FastAPI backend (without Streamlit frontend).

---

## ✅ Prerequisites

- Google Cloud account (free $300 credit)
- `gcloud` CLI installed (Google Cloud SDK)
- Your backend folder ready

---

## 🎯 3 Simple Steps

### STEP 1: Create Google Cloud Project (5 minutes)

1. Go to: https://console.cloud.google.com
2. Click **"Create a project"**
3. Name it: `shield-os-backend`
4. Wait for creation to complete

---

### STEP 2: Enable Cloud Run & Cloud Build

1. In search bar, type: **"Cloud Run"**
2. Click **"Enable"**
3. Search for **"Cloud Build"**
4. Click **"Enable"**

---

### STEP 3: Deploy Backend (10 minutes)

**Open Cloud Shell or Terminal and run:**

```bash
cd /path/to/your/Shield.OS/folder

gcloud run deploy shield-backend --source . --platform managed --region us-central1 --timeout 900
```

**Replace** `/path/to/your/Shield.OS/folder` with your actual path.

**Example on Windows:**
```bash
cd C:\Users\YourName\Desktop\Shield.OS
gcloud run deploy shield-backend --source . --platform managed --region us-central1 --timeout 900
```

---

### When Prompted:

**Question 1:** Allow unauthenticated invocations?
```
(y/N)?  → Type: y
```

**Question 2:** Which region?
```
[Enter to choose]  → Press Enter (us-central1 is default)
```

---

### ✅ You'll Get This Message:

```
Service [shield-backend] revision [shield-backend-xxxxx-us-central1]
has been deployed and is serving 100% of traffic.

Service URL: https://shield-backend-xxxxx-us-central1.a.run.app
```

🎯 **Save this URL!** This is your API endpoint.

---

## 🧪 Test Your Backend

### Test 1: Health Check
```bash
curl https://shield-backend-xxxxx-us-central1.a.run.app/health
```

**Should return:**
```json
{
  "status": "operational",
  "logistic_regression_loaded": true,
  "xgboost_loaded": true
}
```

---

### Test 2: Make a Prediction

```bash
curl -X POST https://shield-backend-xxxxx-us-central1.a.run.app/predict/single \
  -H "Content-Type: application/json" \
  -d '{
    "Amount": 100.50,
    "Time": 3600,
    "Distance_From_Home": 25.0,
    "selected_model": "xgboost"
  }'
```

**Should return:**
```json
{
  "is_fraud": false,
  "fraud_probability": 0.15,
  "status": "CLEARED"
}
```

---

### Test 3: Interactive API Docs

Open in browser:
```
https://shield-backend-xxxxx-us-central1.a.run.app/docs
```

You'll see interactive Swagger UI where you can:
- Test all endpoints
- See request/response examples
- Try predictions directly

---

## 📊 API Endpoints Available

### 1. Health Check
```
GET /health
```
Returns server status and loaded models

### 2. Single Prediction
```
POST /predict/single
```
Accepts transaction data, returns fraud prediction

### 3. Batch Prediction
```
POST /predict/batch
```
Upload CSV file, returns summary statistics

---

## 💻 Using Your Backend

### From Your Application
```python
import requests

# Your backend URL
API_URL = "https://shield-backend-xxxxx-us-central1.a.run.app"

# Make a prediction
response = requests.post(
    f"{API_URL}/predict/single",
    json={
        "Amount": 150.0,
        "Time": 3600,
        "Distance_From_Home": 30.0,
        "selected_model": "xgboost"
    }
)

result = response.json()
print(f"Fraud: {result['is_fraud']}")
print(f"Probability: {result['fraud_probability']}")
print(f"Status: {result['status']}")
```

### From Frontend (Any Tech Stack)
```javascript
// JavaScript/React example
const API_URL = "https://shield-backend-xxxxx-us-central1.a.run.app";

const response = await fetch(`${API_URL}/predict/single`, {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    Amount: 150,
    Time: 3600,
    Distance_From_Home: 30,
    selected_model: "xgboost"
  })
});

const result = await response.json();
console.log(result);
```

---

## 🔧 Troubleshooting

| Problem | Solution |
|---------|----------|
| Deployment fails | Make sure `Dockerfile` is in root folder |
| "Models not found" | Check `backend/xgboost_model.pkl` exists |
| "Application error" | View logs in Cloud Run console |
| Too slow to load | First request takes time (cold start), subsequent requests are fast |

---

## 📈 Monitor Your Deployment

1. Go to Google Cloud Console
2. Cloud Run → Select `shield-backend`
3. You can see:
   - Request count
   - Error rate
   - Response time
   - CPU/Memory usage

---

## 💰 Costs

**Free Tier:** 2,000,000 requests/month
- Testing: $0
- Small usage: $0
- Estimated cost for 10K requests: $0.24

Check billing: Google Cloud Console → Billing

---

## 🎯 Save This Information

After successful deployment, save:

```
Backend URL: https://shield-backend-xxxxx-us-central1.a.run.app
API Docs: https://shield-backend-xxxxx-us-central1.a.run.app/docs
Region: us-central1
Status: ✅ Running 24/7
```

---

## 🚀 What You Now Have

✅ **24/7 Backend Server** - Runs without your computer
✅ **Global Access** - Anyone can call your API
✅ **Auto-Scaling** - Handles 1 to 1000 requests/second
✅ **HTTPS Security** - Automatic encryption
✅ **REST API** - Standard format for any frontend

---

## 📱 Next Steps

1. **Test thoroughly** - Use the health check & prediction endpoints
2. **Share the URL** - Send to your team/frontend developers
3. **Build Frontend** - Connect any frontend (React, Vue, Flutter, etc.)
4. **Monitor** - Check Cloud Run metrics regularly
5. **Update** - When you change code, redeploy using same command

---

## 🔄 Update & Redeploy

When you make changes to `backend/app.py` or models:

```bash
gcloud run deploy shield-backend --source . --platform managed --region us-central1 --timeout 900
```

Same command - it will redeploy automatically!

---

## ✨ Your Backend is Live!

```
BEFORE:
- Backend runs only on your computer
- Stops when you close laptop
- Only you can access

AFTER:
- Backend runs on Google Cloud
- Runs 24/7 without you
- Anyone in the world can access
- Auto-scales for traffic
- Professional deployment
```

**Congratulations! Your API is live!** 🎉

---

## 📞 Quick Reference

| What | Command |
|------|---------|
| Deploy | `gcloud run deploy shield-backend --source . --platform managed --region us-central1 --timeout 900` |
| Health Check | `curl https://YOUR-URL/health` |
| View Logs | Google Cloud Console → Cloud Run → shield-backend → Logs |
| Stop Service | Google Cloud Console → Cloud Run → shield-backend → Delete |
| Redeploy | Use deploy command again |

---

**Backend Only Setup Complete!** ✅

Your FastAPI backend is now running on Google Cloud and ready to serve predictions 24/7.

