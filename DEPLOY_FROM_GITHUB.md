# 🚀 Deploy from GitHub to Google Cloud Shell

Your code is now on GitHub! Here's how to deploy it from Google Cloud Shell.

---

## 📍 Your GitHub Repository
```
https://github.com/SaiMasram750/Credir_card_fraud.git
```

---

## 🚀 Deploy in Google Cloud Shell (3 Steps)

### Step 1: Open Google Cloud Shell

1. Go to: https://console.cloud.google.com
2. Click the **>_** icon (top right)
3. Terminal opens at the bottom

### Step 2: Clone Your Repository

In the Google Cloud Shell, run:

```bash
git clone https://github.com/SaiMasram750/Credir_card_fraud.git
cd Credir_card_fraud
```

### Step 3: Deploy Backend

```bash
gcloud run deploy shield-backend --source . --platform managed --region us-central1 --timeout 900
```

When prompted:
- `Allow unauthenticated?` → Type: `y`
- `Region?` → Press Enter

**Wait 5-10 minutes** for deployment...

✅ **Done!** You'll get your backend URL!

---

## 📋 What Gets Deployed

From the repository:

```
Credir_card_fraud/
├── Dockerfile ..................... Backend container
├── backend/
│   ├── app.py .................... FastAPI code
│   ├── xgboost_model.pkl ........ ML model
│   └── logistic_regression.pkl .. ML model
├── requirements.txt ............. Dependencies
└── All documentation
```

---

## 🧪 Test Your Deployment

After deployment completes:

### Test 1: Health Check
```bash
curl https://your-backend-url/health
```

### Test 2: API Docs
Open in browser:
```
https://your-backend-url/docs
```

### Test 3: Make Prediction
```bash
curl -X POST https://your-backend-url/predict/single \
  -H "Content-Type: application/json" \
  -d '{"Amount": 100, "Time": 3600, "Distance_From_Home": 25, "selected_model": "xgboost"}'
```

---

## 📊 What's in the Repository

### Application Code
- `backend/app.py` - FastAPI server
- `backend/xgboost_model.pkl` - XGBoost model
- `backend/logistic_regression.pkl` - Logistic Regression model
- `frontend/app.py` - Streamlit dashboard
- `requirements.txt` - Python packages

### Docker Setup
- `Dockerfile` - Backend container
- `streamlit_dockerfile` - Frontend container
- `.dockerignore` - Exclude files

### Documentation (Pick One)
- `00_READ_ME_FIRST_BACKEND.txt` - Start here
- `DEPLOY_NOW.md` - Fastest guide (2 min)
- `BACKEND_QUICK_DEPLOY.txt` - Commands (3 min)
- `BACKEND_ONLY_DEPLOYMENT.md` - Detailed (15 min)
- `README_BACKEND_ONLY.md` - Complete reference
- `BACKEND_DEPLOYMENT_CHECKLIST.md` - Step-by-step checklist

---

## 🔄 Full Workflow

### From Your Computer

1. **Clone repo locally**
   ```bash
   git clone https://github.com/SaiMasram750/Credir_card_fraud.git
   cd Credir_card_fraud
   ```

2. **Run locally (optional)**
   ```bash
   pip install -r requirements.txt
   python -m uvicorn backend.app:app --host 127.0.0.1 --port 8000
   ```

### From Google Cloud Shell

1. **Clone repo**
   ```bash
   git clone https://github.com/SaiMasram750/Credir_card_fraud.git
   cd Credir_card_fraud
   ```

2. **Deploy backend**
   ```bash
   gcloud run deploy shield-backend --source . --platform managed --region us-central1 --timeout 900
   ```

3. **Get URL and test**

---

## 💡 Tips

### Save Git Commands
```bash
# Pull latest changes
git pull origin main

# View logs
git log --oneline

# Check status
git status
```

### Update Code Later

1. Make changes locally
2. Commit and push:
   ```bash
   git add .
   git commit -m "Your message"
   git push origin main
   ```

3. In Google Cloud Shell:
   ```bash
   git pull origin main
   gcloud run deploy shield-backend --source . --platform managed --region us-central1 --timeout 900
   ```

---

## ✅ Checklist

- [ ] Repository cloned to GitHub
- [ ] Can access: https://github.com/SaiMasram750/Credir_card_fraud
- [ ] Google Cloud Shell ready
- [ ] Git clone works in Cloud Shell
- [ ] Deployment command runs successfully
- [ ] Backend URL received
- [ ] API tests pass
- [ ] Celebrate! 🎉

---

## 📞 Troubleshooting

| Problem | Solution |
|---------|----------|
| Clone fails | Check GitHub URL is correct |
| Deployment fails | Check Dockerfile exists in repo |
| Models not found | Verify .pkl files are in backend/ |
| Permission denied | Check GitHub authentication |

---

## 🎯 Next Steps

1. ✅ Code is on GitHub
2. ✅ Clone in Google Cloud Shell
3. ✅ Deploy using one command
4. ✅ Your backend is live!

**Ready to deploy from Google Cloud Shell? Start now!** 🚀

