# ✅ Backend Deployment Checklist

Complete this checklist before and during deployment.

---

## 📋 Before You Start

### Google Cloud Setup
- [ ] Google account created
- [ ] Google Cloud project created (name: shield-os-backend)
- [ ] Cloud Run service enabled
- [ ] Cloud Build service enabled
- [ ] `gcloud` CLI installed on your computer

### Files Ready
- [ ] `Dockerfile` exists in root folder
- [ ] `backend/app.py` exists
- [ ] `backend/xgboost_model.pkl` exists
- [ ] `backend/logistic_regression.pkl` exists
- [ ] `requirements.txt` exists

### Everything OK?
- [ ] All checks above are complete
- [ ] Terminal/command prompt open
- [ ] Ready to deploy!

---

## 🚀 During Deployment

### Step 1: Navigate to Project
```bash
cd /path/to/Shield.OS
```
- [ ] Successfully navigated to folder
- [ ] Can see Dockerfile, backend/ folder, requirements.txt

### Step 2: Run Deploy Command
```bash
gcloud run deploy shield-backend --source . --platform managed --region us-central1 --timeout 900
```
- [ ] Command running
- [ ] See "Building..." messages
- [ ] See "Deploying..." messages

### Step 3: Respond to Prompts
- [ ] "Allow unauthenticated?" → Typed `y` → Pressed Enter
- [ ] Region prompt → Pressed Enter (chose default)
- [ ] Waiting for deployment to complete

### Step 4: Deployment Complete
- [ ] See success message
- [ ] Got URL: `https://shield-backend-xxxxx-us-central1.a.run.app`

---

## ✅ After Deployment

### Save URLs
- [ ] Copied backend URL from deployment output
- [ ] Saved to safe location
- [ ] Have full URL starting with `https://`

### Test Health Check
```bash
curl https://your-backend-url/health
```
- [ ] Received JSON response
- [ ] Status says "operational"
- [ ] Both models show as loaded

### Test API Docs
```
https://your-backend-url/docs
```
- [ ] Opened in browser
- [ ] See Swagger UI interface
- [ ] Can see endpoints listed

### Test Single Prediction
In Swagger UI or with curl:
- [ ] Sent prediction request
- [ ] Received fraud_probability
- [ ] Received status (FLAGGED or CLEARED)
- [ ] Response looks reasonable

### Test Batch Endpoint
- [ ] See batch endpoint in docs
- [ ] Know how to upload CSV

---

## 📊 Monitor & Maintain

### Check Status
- [ ] Go to Google Cloud Console
- [ ] Cloud Run → shield-backend
- [ ] Can see request count
- [ ] Can see error rate
- [ ] Status shows as "OK"

### Check Logs
- [ ] In Cloud Run console
- [ ] Click "Logs" tab
- [ ] Can see recent requests
- [ ] No error messages

### Check Costs
- [ ] In Google Cloud Console
- [ ] Billing → Overview
- [ ] Verify within free tier
- [ ] Set budget alert if desired

---

## 🔄 Update Backend

When you change code:

### Make Changes
- [ ] Edited `backend/app.py` locally
- [ ] Tested locally if needed
- [ ] Ready to redeploy

### Redeploy
```bash
gcloud run deploy shield-backend --source . --platform managed --region us-central1 --timeout 900
```
- [ ] Ran deploy command
- [ ] Waited for completion
- [ ] Got new/updated URL (if region changed)
- [ ] Tested new version

---

## 🎉 Success Indicators

Check all of these are true:

- [ ] Backend URL is publicly accessible
- [ ] `/health` endpoint returns "operational"
- [ ] `/docs` endpoint shows Swagger UI
- [ ] Can make predictions successfully
- [ ] HTTPS certificate is valid (green lock in browser)
- [ ] Google Cloud shows deployment status as OK
- [ ] No error messages in logs
- [ ] Costs are within free tier

---

## 📞 Troubleshooting Checklist

If something went wrong:

### Deployment Failed
- [ ] Check Dockerfile exists in root
- [ ] Check all paths are correct
- [ ] Check models exist in backend/ folder
- [ ] Read error message in console
- [ ] Try running command again

### Can't Connect to API
- [ ] Check URL starts with `https://`
- [ ] Check URL doesn't have typo
- [ ] Check internet connection
- [ ] Wait 2-3 minutes for deployment to fully propagate
- [ ] Check Google Cloud Console status

### Models Not Loading
- [ ] Go to Cloud Run → Logs
- [ ] Search for error message
- [ ] Check if .pkl files are in root of Docker image
- [ ] Check file names are spelled correctly

### Endpoint Errors
- [ ] Open `/docs` endpoint
- [ ] Try test request with sample data
- [ ] Check error message returned
- [ ] Look at backend logs in Cloud Run

### Still Broken?
- [ ] Read BACKEND_ONLY_DEPLOYMENT.md troubleshooting section
- [ ] Check Google Cloud status page
- [ ] Ask in Stack Overflow with error message

---

## 🎯 Final Checklist

Before considering deployment complete:

- [ ] Backend URL saved
- [ ] Tested health check
- [ ] Tested prediction endpoint
- [ ] Shared URL with team (if applicable)
- [ ] Documented URL in team channel
- [ ] Set monitoring alert (optional)
- [ ] All checklists above completed
- [ ] Celebrate! 🎉

---

## 📝 Notes Section

Use this to save important info:

```
Backend URL: _________________________________
API Docs URL: _________________________________
Deployed Date: _________________________________
Deployed By: _________________________________
Last Updated: _________________________________
Notes: _________________________________
      _________________________________
```

---

**✅ Ready to deploy? Start with DEPLOY_NOW.md**

