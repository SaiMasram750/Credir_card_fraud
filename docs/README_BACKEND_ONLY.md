# 🎯 Backend Only Deployment - Complete Guide

You want to deploy **just the backend** (FastAPI) to Google Cloud. Here's everything you need!

---

## 📋 Files You Need

We've created **4 different guides** depending on what you need:

| File | Purpose | Time | When to Use |
|------|---------|------|-----------|
| **DEPLOY_NOW.md** | 3 steps only | 2 min | I just want to deploy NOW! |
| **BACKEND_QUICK_DEPLOY.txt** | Copy/paste commands | 3 min | I want the exact commands |
| **BACKEND_DEPLOYMENT_SUMMARY.md** | Overview | 5 min | I want quick overview |
| **BACKEND_ONLY_DEPLOYMENT.md** | Full detailed guide | 15 min | I want to understand everything |

---

## 🚀 Fastest Way (Copy & Paste)

**If you just want to deploy RIGHT NOW:**

1. Open terminal/command prompt
2. Navigate to your project:
   ```bash
   cd /path/to/Shield.OS
   ```

3. Run this command:
   ```bash
   gcloud run deploy shield-backend --source . --platform managed --region us-central1 --timeout 900
   ```

4. Answer `y` when asked
5. Press Enter for region
6. Wait 5-10 minutes
7. ✅ Done! You get a URL

---

## 📖 Choose Your Guide

### Need Quick Reference?
→ Read **BACKEND_QUICK_DEPLOY.txt** (3 minutes)

### Need Just the Steps?
→ Read **DEPLOY_NOW.md** (2 minutes)

### Want Overview?
→ Read **BACKEND_DEPLOYMENT_SUMMARY.md** (5 minutes)

### Want Detailed Explanations?
→ Read **BACKEND_ONLY_DEPLOYMENT.md** (15 minutes)

---

## ✅ What Will Happen

### Before Deployment
```
Your Computer
└── Backend (only works when you run it)
    └── Accessible only to you at localhost:8000
```

### After Deployment
```
Google Cloud ☁️
└── Backend (always running)
    └── Accessible worldwide at https://shield-backend-xxxxx.a.run.app
```

---

## 🎯 Your Backend Will Have

✅ **REST API** with 3 endpoints:
- `GET /health` - Check if running
- `POST /predict/single` - Predict one transaction
- `POST /predict/batch` - Score CSV file

✅ **Auto Documentation** at `/docs`
- Interactive interface
- Test all endpoints
- See examples

✅ **24/7 Availability**
- No computer needed
- Runs even if you close laptop
- Worldwide access

✅ **Auto Scaling**
- 1 user = works great
- 1000 users = auto-scales
- You don't do anything

---

## 💻 Prerequisites

Before deploying, make sure you have:

- ✅ Google Cloud account (free with $300 credit)
- ✅ Project created
- ✅ Cloud Run enabled
- ✅ Cloud Build enabled
- ✅ `gcloud` CLI installed (Google Cloud SDK)

**Don't have these?**
→ See BACKEND_ONLY_DEPLOYMENT.md for setup instructions

---

## 📊 What Gets Deployed

These files are automatically deployed:

```
Your Project
├── Dockerfile ........................ Instructions for deployment
├── backend/app.py ................... FastAPI server code
├── backend/xgboost_model.pkl ........ ML model (trained)
├── backend/logistic_regression.pkl .. ML model (trained)
└── requirements.txt ................. Python packages needed
```

---

## 🔄 Deployment Process

When you run the deploy command:

```
1. Google Cloud reads Dockerfile
2. Builds Docker container with your code + models
3. Uploads to Cloud Run
4. Starts the backend server
5. Gives you a URL
6. Your API is live!
```

Total time: 5-10 minutes

---

## 🧪 After Deployment - Test It

### Test 1: Open in Browser
```
https://your-backend-url/docs
```
You'll see Swagger UI to test all endpoints

### Test 2: Health Check
```bash
curl https://your-backend-url/health
```

### Test 3: Make a Prediction
```bash
curl -X POST https://your-backend-url/predict/single \
  -H "Content-Type: application/json" \
  -d '{"Amount": 100, "Time": 3600, "Distance_From_Home": 25, "selected_model": "xgboost"}'
```

---

## 💰 Costs

**Google Cloud Free Tier:**
- 2 million requests/month = FREE
- 360,000 GB-seconds/month = FREE

**Your Estimated Cost:**
- Testing/Demo: $0
- Low usage: $0
- 100K requests/month: ~$2.40
- 1M requests/month: ~$24

---

## 🎓 Key Information to Save

After deployment, save these:

```
Backend URL: https://shield-backend-xxxxx-us-central1.a.run.app
API Docs: https://shield-backend-xxxxx-us-central1.a.run.app/docs
Region: us-central1
Status: ✅ Live & Running
```

---

## 🛠️ Common Tasks

### Update Backend Code
1. Edit `backend/app.py` locally
2. Run deploy command again
3. It redeploys automatically!

### View Logs & Metrics
1. Go to Google Cloud Console
2. Cloud Run → shield-backend
3. Click "Logs" or "Metrics"

### Stop the Backend
1. Google Cloud Console
2. Cloud Run → shield-backend
3. Click "Delete"

### Restart the Backend
1. Run deploy command again
2. It redeploys from scratch

---

## ❓ Frequently Asked Questions

**Q: Do I need the frontend?**
A: No! Just backend is fine. You can build any frontend later.

**Q: Can I connect a different frontend?**
A: Yes! The API works with any frontend (React, Vue, Flutter, etc.)

**Q: How many requests can it handle?**
A: Starts small, auto-scales to handle thousands/second.

**Q: Is it secure?**
A: Yes! HTTPS automatic, runs in secure Google Cloud infrastructure.

**Q: Can I revert to a previous version?**
A: Yes! Google Cloud keeps deployment history.

**Q: What if I want a custom domain?**
A: Yes! Google Cloud supports domain mapping.

---

## 📞 Troubleshooting

| Issue | Solution |
|-------|----------|
| Command not recognized | Install gcloud CLI first |
| Models not found | Check backend/ has .pkl files |
| Deployment fails | Read error message in logs |
| Timeout error | Wait 10 minutes, normal first time |
| Can't reach API | Check URL has https:// (not http://) |

---

## 🚀 Next Steps

### Right Now
1. Pick a guide above (DEPLOY_NOW.md for fastest)
2. Follow the instructions
3. Run deploy command

### After Deployment
1. Test using `/docs` endpoint
2. Save your URL
3. Share with team/frontend developers
4. Build your frontend to use this API

### Later
1. Monitor usage in Google Cloud Console
2. Optimize if needed
3. Add features to backend
4. Redeploy with updates

---

## 🎉 Congratulations!

You're about to deploy a production-grade API to Google Cloud!

**Which guide do you want?**
- Super fast? → **DEPLOY_NOW.md**
- Need commands? → **BACKEND_QUICK_DEPLOY.txt**
- Want overview? → **BACKEND_DEPLOYMENT_SUMMARY.md**
- Want details? → **BACKEND_ONLY_DEPLOYMENT.md**

Pick one and get started! 🚀

