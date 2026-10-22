# 🚀 Deploy Shield.OS to Google Cloud - Simple Steps

This guide explains how to deploy Shield.OS to Google Cloud in simple terms.

---

## 📋 What You Need Before Starting

1. **Google Account** - Create one at https://google.com
2. **Google Cloud Project** - Free $300 credit for new users
3. **Git installed** - To upload your code (optional)
4. **Your Shield.OS folder** - All the files we created

---

## 🎯 Step-by-Step Deployment

### STEP 1: Create Google Cloud Account & Project (5 minutes)

**What:** Set up a Google Cloud account to host your app

**How:**
1. Go to https://console.cloud.google.com
2. Click **"Create a project"** or use existing one
3. Name it: `shield-os-fraud-detection`
4. Click **"Create"** and wait 1-2 minutes

✅ **Done!** You now have a Google Cloud project

---

### STEP 2: Enable Required Services (3 minutes)

**What:** Turn on the services Google Cloud needs to run your app

**How:**
1. In Google Cloud Console, search for **"Cloud Run"**
2. Click **"Cloud Run"** → It will ask to enable the API
3. Click **"Enable"** and wait 30 seconds
4. Repeat for **"Cloud Build"** (search and enable)

✅ **Done!** Services are enabled

---

### STEP 3: Prepare Your Code for Deployment (5 minutes)

**What:** Add 3 special files that Google Cloud needs

**File 1: Create `Dockerfile` (for Backend)**

This tells Google Cloud how to run your backend:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY backend/xgboost_model.pkl /app/
COPY backend/logistic_regression.pkl /app/
COPY backend/app.py /app/
COPY requirements.txt /app/

RUN pip install -r requirements.txt

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

**Where to save:** In your project root folder (same level as `backend/` and `frontend/`)

---

**File 2: Create `streamlit_dockerfile` (for Frontend)**

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY frontend/app.py /app/
COPY requirements.txt /app/

RUN pip install -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

**Where to save:** In your project root folder

---

**File 3: Create `.dockerignore`**

This tells Docker to ignore certain files (speed up deployment):

```
__pycache__
*.pyc
.git
.gitignore
.env
*.egg-info
.streamlit
.pytest_cache
venv
env
```

**Where to save:** In your project root folder

---

### STEP 4: Update Frontend to Connect to Cloud Backend (2 minutes)

**What:** Tell Streamlit frontend where the backend is hosted

**How:**
1. Open `frontend/app.py`
2. Find this line (around line 13):
```python
API_URL = "http://127.0.0.1:8000"
```

3. Replace with (we'll get exact URL later):
```python
API_URL = "https://shield-backend-xxxx-xx.a.run.app"  # We'll update this later
```

**Note:** Don't worry about exact URL yet - we'll get it after deployment

---

### STEP 5: Deploy Backend First (10 minutes)

**What:** Upload backend to Google Cloud

**How:**

**Option A: Using Google Cloud Console (Easiest)**

1. Go to Google Cloud Console
2. Click **"Cloud Run"** in left menu
3. Click **"Create Service"**
4. Choose **"Deploy from source code"**
5. Click **"Set up with Cloud Shell"**
6. In the terminal that opens, paste:

```bash
cd /path/to/your/Shield.OS/folder
gcloud run deploy shield-backend --source . --platform managed --region us-central1 --timeout 900
```

7. When asked:
   - **Allow unauthenticated invocations:** Choose `Y` (Yes)
   - **Region:** Press Enter (default us-central1 is fine)

8. Wait 3-5 minutes for deployment

✅ **You'll get a URL like:** `https://shield-backend-xxxxx-xx.a.run.app`

**Important:** Save this URL! You'll need it for the frontend.

---

**Option B: Using GitHub (If you know Git)**

1. Push your code to GitHub:
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/shield-os.git
git push -u origin main
```

2. Go to Google Cloud Console → Cloud Run
3. Click **"Create Service"**
4. Select **"Deploy from GitHub"**
5. Connect your GitHub account
6. Select your `shield-os` repository
7. Choose `Dockerfile` for backend
8. Click **"Deploy"**

---

### STEP 6: Update Frontend with Backend URL (2 minutes)

**What:** Tell frontend where to find the backend

**How:**
1. Open `frontend/app.py`
2. Find line with `API_URL = "https://shield-backend-xxxx-xx.a.run.app"`
3. Replace `xxxx-xx` with the actual URL from Step 5
4. Save the file

**Example:**
```python
API_URL = "https://shield-backend-xyz12345-us-central1.a.run.app"
```

---

### STEP 7: Deploy Frontend (10 minutes)

**What:** Upload frontend to Google Cloud

**How:**

1. Go to Google Cloud Console → Cloud Run
2. Click **"Create Service"**
3. Choose **"Deploy from source code"**
4. Click **"Set up with Cloud Shell"**
5. In terminal, paste:

```bash
cd /path/to/your/Shield.OS/folder
gcloud run deploy shield-frontend --source . --platform managed --region us-central1 --timeout 3600 --set-cloudsql-instances=""
```

6. When asked:
   - **Dockerfile location:** Type `streamlit_dockerfile`
   - **Allow unauthenticated:** Choose `Y` (Yes)
   - **Region:** Press Enter

7. Wait 3-5 minutes

✅ **You'll get another URL like:** `https://shield-frontend-xxxxx-xx.a.run.app`

---

### STEP 8: Test Your Deployed App (5 minutes)

**What:** Make sure everything works on Google Cloud

**How:**

1. Open the frontend URL in your browser:
```
https://shield-frontend-xxxxx-xx.a.run.app
```

2. Try making a prediction:
   - Go to **"Single Prediction"** tab
   - Enter some values
   - Click **"Predict"**
   - You should see a result!

3. Try **"Live Stream"** and **"Batch Upload"** tabs

✅ **Everything works? Great! You're deployed!**

---

## 🎬 What You Now Have on Google Cloud

```
Your Shield.OS App (Google Cloud)
│
├── Backend Service (Cloud Run)
│   ├── URL: https://shield-backend-xxxxx-xx.a.run.app
│   ├── Models: XGBoost + Logistic Regression
│   └── Port: 8000 (internal)
│
└── Frontend Service (Cloud Run)
    ├── URL: https://shield-frontend-xxxxx-xx.a.run.app
    ├── Dashboard with 3 tabs
    └── Port: 8501 (internal)
```

---

## 💰 Costs (Important!)

**Good News:** Google Cloud gives free credit!

- **Free Tier:** 180,000 vCPU seconds per month
- **Your Usage:** Very small (Streamlit is lightweight)
- **Estimated Cost:** $0 for testing/demo, maybe $10-50/month for production

**To Check Costs:**
1. Go to Google Cloud Console
2. Click **"Billing"** → **"Overview"**
3. See your current usage

---

## 🔧 Troubleshooting

| Problem | Solution |
|---------|----------|
| Backend won't deploy | Make sure `Dockerfile` is in root folder |
| Frontend can't connect | Check API_URL is correct with `https://` |
| Deployment takes too long | Cloud Run can take 5-10 minutes first time |
| See "Application Error" | Check logs: Cloud Run → Select service → "Logs" |
| Model loading error | Make sure `.pkl` files are in `backend/` folder |

**View Logs:**
1. Go to Cloud Run service
2. Click on your service name
3. Scroll down to see error messages

---

## 📊 After Deployment

### Monitor Your App
1. Google Cloud Console → Cloud Run
2. Click your service name
3. See metrics:
   - Request count
   - Error rate
   - Response time

### Stop Your App (Save Money)
1. Cloud Run → Select service
2. Click **"Delete"**
3. Confirm deletion

### Keep Using for Free
- First 2 million requests per month = FREE
- That's enough for demo/testing

---

## 🔐 Security Notes

**Current Setup:**
- ✅ Anyone can access your app (good for demo)
- ✅ No authentication needed

**If You Want to Add Security Later:**
1. Add Google Cloud IAM authentication
2. Use environment variables for secrets
3. Enable HTTPS (automatic with Cloud Run)

---

## 📱 After Deployment - Useful Links

Save these links for future reference:

1. **Your Frontend:** `https://shield-frontend-xxxxx-xx.a.run.app`
2. **Your Backend API:** `https://shield-backend-xxxxx-xx.a.run.app`
3. **Backend Docs:** `https://shield-backend-xxxxx-xx.a.run.app/docs`
4. **Google Cloud Console:** `https://console.cloud.google.com`

---

## ❓ FAQ

**Q: Can I stop the app and restart it later?**
A: Yes! You can delete and redeploy anytime. Code stays safe.

**Q: How many users can it handle?**
A: Google Cloud auto-scales. Start with 1 user, grows to 1000+ automatically.

**Q: Can I add a custom domain name?**
A: Yes! In Cloud Run → Domain mappings → Add your domain

**Q: What if I want to update the code?**
A: Push new code and redeploy using same steps. Old version disappears.

**Q: Is it safe?**
A: Yes! Google Cloud handles security. HTTPS automatic.

---

## 🎓 Next Steps (Optional)

After successful deployment:

1. **Add Custom Domain** - Make it look professional
2. **Add Authentication** - Require login
3. **Monitor Usage** - Use Google Cloud dashboards
4. **Set Budget Alerts** - Get notified if costs spike
5. **Optimize Models** - Improve fraud detection accuracy

---

## 📞 Need Help?

1. Check Google Cloud Documentation: https://cloud.google.com/docs
2. Stack Overflow: Search your error message
3. Google Cloud Support: Available in Console

---

**Congratulations! Your Shield.OS app is now live on the internet!** 🎉

Visit your frontend URL to see your fraud detection system in action!

