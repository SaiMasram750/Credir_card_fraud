# 🎬 Visual Step-by-Step Deployment Guide

This guide shows you EXACTLY what to click and type.

---

## STEP 1: Create Google Cloud Account

### What to do:
1. Go to: https://console.cloud.google.com
2. Sign in with your Google account
3. Click **"Create a project"**

### What you'll see:
```
┌─────────────────────────────────────────┐
│   Google Cloud Console                  │
│                                         │
│   [☰] [Search bar]    [Notifications]  │
│                                         │
│   ┌────────────────────────────────┐   │
│   │ Select a project               │   │
│   │ ┌──────────────────────────────┤   │
│   │ │ ▼ NEW PROJECT              │   │
│   │ └──────────────────────────────┤   │
│   │                                │   │
│   │       [Create]  [Cancel]       │   │
│   └────────────────────────────────┘   │
└─────────────────────────────────────────┘
```

### Name your project:
```
Project name: shield-os-fraud-detection
Parent organization: (leave as default)
[Create]
```

✅ **Wait 2 minutes** for project creation

---

## STEP 2: Enable Services

### What to do:
1. In search bar, type: **"Cloud Run"**
2. Click **"Cloud Run"** option
3. If you see message, click **"ENABLE"**

### What you'll see:
```
┌─────────────────────────────────┐
│ Search: [Cloud Run           ]  │
│                                 │
│ Results:                        │
│ • Cloud Run (Compute)           │
│ • Cloud Run Admin API           │
│                                 │
└─────────────────────────────────┘
        ↓ Click on "Cloud Run"
┌─────────────────────────────────┐
│ Cloud Run                       │
│                                 │
│ [ENABLE]  or [Already enabled]  │
│                                 │
└─────────────────────────────────┘
```

### Repeat for Cloud Build:
1. Search: **"Cloud Build"**
2. Click **"Enable"**

✅ **Done!** Both services enabled

---

## STEP 3: Check Deployment Files

### What to do:
Make sure these 3 files exist in your project folder:

```
Your Folder
├── Dockerfile  ✅ (already created for you)
├── streamlit_dockerfile  ✅ (already created for you)
├── .dockerignore  ✅ (already created for you)
├── backend/
│   ├── app.py
│   ├── xgboost_model.pkl
│   └── logistic_regression.pkl
├── frontend/
│   └── app.py
└── requirements.txt
```

### How to verify on Windows:
```
Open File Explorer
Navigate to your Shield.OS folder
Look for: Dockerfile (no extension)
Look for: streamlit_dockerfile (no extension)
Look for: .dockerignore (starts with dot)
```

✅ **All files present?** Continue!

---

## STEP 4: Deploy Backend

### Open Google Cloud Console

1. Go to: https://console.cloud.google.com
2. Make sure right project is selected (top left)
3. Click menu ☰ → **"Cloud Run"**

### Click "Create Service"

```
┌─────────────────────────────────────┐
│ Cloud Run                           │
│                                     │
│ [+ CREATE SERVICE]  [Authentication]│
│                                     │
│ Services (0)                        │
│ (No services yet)                   │
└─────────────────────────────────────┘
```

### Deploy from source

```
┌─────────────────────────────────────────────┐
│ Create Service                              │
│                                             │
│ Source Type:                                │
│ ○ Deploy from existing container image     │
│ ● Deploy from source code  ← SELECT THIS   │
│   [Set up with Cloud Shell]                 │
│                                             │
└─────────────────────────────────────────────┘
```

### Click "Set up with Cloud Shell"

A terminal will open at the bottom

### Copy & Paste This Command:

```bash
cd /path/to/your/Shield.OS/folder
gcloud run deploy shield-backend --source . --platform managed --region us-central1 --timeout 900
```

**Replace** `/path/to/your/Shield.OS/folder` with your actual folder path

**Example on Windows:**
```bash
cd C:\Users\YourName\Desktop\Shield.OS
gcloud run deploy shield-backend --source . --platform managed --region us-central1 --timeout 900
```

### When asked:

```
? Allow unauthenticated invocations to [shield-backend]?
(y/N)  ← Type: y
```

```
Which region would you like to deploy to?
 1 - us-central1
 2 - europe-west1
 3 - ... etc

[Enter choice]  ← Press Enter (choose 1)
```

### Watch the progress:

```
Building using Buildpacks...
Starting build...
Step 1/3 : ...
Step 2/3 : ...
Step 3/3 : ...
Build completed successfully!
Deploying to Cloud Run...
Waiting for deployment...
```

### ✅ When complete, you'll see:

```
Service [shield-backend] revision [shield-backend-xxxxx-xx]
has been deployed and is serving 100% of traffic.

Service URL: https://shield-backend-xxxxx-us-central1.a.run.app
```

### 🎯 SAVE THIS URL! Copy it somewhere.

You'll need it in Step 5.

---

## STEP 5: Update Frontend Code

### Open your code editor

File: `frontend/app.py`

### Find this line (around line 13):

```python
API_URL = "http://127.0.0.1:8000"
```

### Replace with your backend URL from Step 4:

**Change from:**
```python
API_URL = "http://127.0.0.1:8000"
```

**Change to:**
```python
API_URL = "https://shield-backend-xxxxx-us-central1.a.run.app"
```

### Example:
```python
API_URL = "https://shield-backend-abc123-us-central1.a.run.app"
```

### Save the file

✅ **Done!** Frontend updated with correct backend URL

---

## STEP 6: Deploy Frontend

### Back in Cloud Shell

```bash
cd /path/to/your/Shield.OS/folder
gcloud run deploy shield-frontend --source . --platform managed --region us-central1 --timeout 3600
```

### When asked:

```
Source location: (press Enter for default)

Name of Dockerfile to build: 
(just press Enter first, if it asks again type: streamlit_dockerfile)
```

### If it asks for Dockerfile location:

```
Dockerfile location: streamlit_dockerfile  ← Type this
```

### When asked about unauthenticated:

```
? Allow unauthenticated invocations to [shield-frontend]?
(y/N)  ← Type: y
```

### Watch the progress:

```
Building using Buildpacks...
...
Deploying to Cloud Run...
Waiting for deployment...
```

### ✅ When complete:

```
Service [shield-frontend] revision [shield-frontend-xxxxx-xx]
has been deployed and is serving 100% of traffic.

Service URL: https://shield-frontend-xxxxx-us-central1.a.run.app
```

### 🎯 SAVE THIS URL TOO!

---

## STEP 7: Test Your Deployed App

### Open your frontend URL in browser

```
https://shield-frontend-xxxxx-us-central1.a.run.app
```

### You should see:

```
┌──────────────────────────────────┐
│     🛡️ Shield.OS                │
│ Fraud Detection System           │
│                                  │
│ Configuration   [xgboost ▼]     │
│                                  │
│ ┌─────────────────────────────┐ │
│ │ Single Prediction           │ │
│ │ Live Stream Simulator       │ │
│ │ Batch CSV Audit             │ │
│ └─────────────────────────────┘ │
└──────────────────────────────────┘
```

### Try making a prediction:

1. Go to **"Single Prediction"** tab
2. Enter values:
   - Amount: **100**
   - Distance From Home: **10**
   - Time Elapsed: **3600**
   - Model: **xgboost**
3. Click **"Predict"** button

### You should see:

```
Fraud Probability  0.15

Status: CLEARED

✓ LEGITIMATE
```

### ✅ It works! Try other tabs:

- Click **"Load Sample Fraud Transaction"**
- Go to **"Live Stream Simulator"**
- Try uploading a CSV in **"Batch CSV Audit"**

---

## ✅ DONE! Your App is Deployed! 🎉

### Save these URLs:

```
Frontend: https://shield-frontend-xxxxx-us-central1.a.run.app
Backend:  https://shield-backend-xxxxx-us-central1.a.run.app
API Docs: https://shield-backend-xxxxx-us-central1.a.run.app/docs
```

### Share your app:

1. Copy frontend URL
2. Send to friends/team
3. They can use it immediately!

---

## 🔧 Common Issues & Fixes

### Issue: "Application Error"

**Fix:**
1. Go to Cloud Run → select service → Logs tab
2. Read error message
3. Usually means wrong Dockerfile or missing files

### Issue: "Connection refused"

**Fix:**
1. Check API_URL in frontend/app.py
2. Make sure it has `https://` (not `http://`)
3. Redeploy frontend

### Issue: "Timeout error"

**Fix:**
- Normal on first deployment
- Wait 10-15 minutes
- Try again

### Issue: Can't find files

**Fix:**
```
Make sure these files exist in your project root:
- Dockerfile
- streamlit_dockerfile  
- .dockerignore
- requirements.txt
- backend/app.py
- backend/xgboost_model.pkl
- backend/logistic_regression.pkl
- frontend/app.py
```

---

## 📊 What's Now Running on Google Cloud

```
┌─ Google Cloud ─────────────────────┐
│                                    │
│  Backend                           │
│  ├─ URL: shield-backend-xxx       │
│  ├─ Port: 8000 (internal)         │
│  ├─ Models: XGBoost + Logistic    │
│  └─ Status: ✅ Running 24/7        │
│                                    │
│  Frontend                          │
│  ├─ URL: shield-frontend-xxx      │
│  ├─ Port: 8501 (internal)         │
│  └─ Status: ✅ Running 24/7        │
│                                    │
└────────────────────────────────────┘
```

---

## 🎓 Next Steps (Optional)

### 1. Monitor Your App
- Go to Cloud Run → select service
- Click "Metrics" tab
- See requests, errors, latency

### 2. Add Custom Domain
- Cloud Run → Domain Mappings
- Add your domain name
- (e.g., fraud-detection.com)

### 3. Set Budget Alerts
- Google Cloud Console → Billing
- Click "Budgets and alerts"
- Set limit (e.g., $50/month)

### 4. Update App Code
- Change code locally
- Push to Cloud Run
- Automatically redeployed!

---

## 💰 Costs

Your current setup:
- **Free Tier:** 2 million requests/month included
- **Likely Cost:** $0 for demo/testing
- **Production Estimate:** $10-50/month

Check billing anytime:
- Google Cloud Console → Billing → Overview

---

## 🎉 Congratulations!

You successfully deployed Shield.OS to Google Cloud!

Your app is:
- ✅ Live on the internet
- ✅ Accessible worldwide
- ✅ Running 24/7
- ✅ Auto-scaling for traffic
- ✅ Protected by Google's security

**Share your app with the world!** 🌍

