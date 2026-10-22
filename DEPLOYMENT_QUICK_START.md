# 🚀 Deploy to Google Cloud - 30 Seconds Overview

## The 8 Simple Steps

### 1️⃣ **Create Google Cloud Account**
- Go to https://console.cloud.google.com
- Create new project named `shield-os-fraud-detection`

### 2️⃣ **Enable Services**
- Search for "Cloud Run" → Enable
- Search for "Cloud Build" → Enable

### 3️⃣ **Files Already Created For You**
✅ `Dockerfile` - For backend
✅ `streamlit_dockerfile` - For frontend
✅ `.dockerignore` - Ignore unnecessary files

### 4️⃣ **Deploy Backend**
```bash
gcloud run deploy shield-backend --source . --platform managed --region us-central1
```
- Answer `Y` for unauthenticated access
- **Save the URL you get!**

### 5️⃣ **Update Frontend**
- Open `frontend/app.py`
- Change line 13:
```python
API_URL = "https://shield-backend-YOUR-URL.a.run.app"  # Paste your URL from Step 4
```

### 6️⃣ **Deploy Frontend**
```bash
gcloud run deploy shield-frontend --source . --platform managed --region us-central1 --timeout 3600
```
- Answer `streamlit_dockerfile` when asked for Dockerfile
- Answer `Y` for unauthenticated access

### 7️⃣ **Test It**
- Open the frontend URL in browser
- Try making predictions
- Check all 3 tabs work

### 8️⃣ **Done!** 🎉
Your app is live on the internet!

---

## Important URLs

Save these after deployment:

```
Frontend: https://shield-frontend-XXXXX-xx.a.run.app
Backend:  https://shield-backend-XXXXX-xx.a.run.app
Docs:     https://shield-backend-XXXXX-xx.a.run.app/docs
```

---

## Costs

- **Free Tier:** 2 million requests/month
- **Your Usage:** Probably $0 for demo
- **Check Cost:** Google Cloud Console → Billing

---

## Common Issues

| Error | Fix |
|-------|-----|
| Deployment fails | Make sure `Dockerfile` exists in root folder |
| Frontend can't connect | Check API_URL in `frontend/app.py` has `https://` |
| Shows "Application Error" | View logs in Cloud Run → Logs tab |

---

## Need Full Guide?

Read `DEPLOYMENT_GUIDE.md` for detailed explanations

---

**That's it! You're deployed!** 🚀
