# 🚀 Deployment Guide

This guide will help you deploy your LangGraph Chatbot to Streamlit Cloud for free.

## Prerequisites

- GitHub account
- Streamlit Cloud account (free - sign up at [streamlit.io/cloud](https://streamlit.io/cloud))
- Google AI API key

## Method 1: Streamlit Cloud (Recommended - FREE)

### Step 1: Prepare Your Repository

1. **Push to GitHub:**
```bash
git init
git add .
git commit -m "Initial commit: LangGraph Chatbot"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/LangGraph_Chatbot.git
git push -u origin main
```

2. **Verify Files:**
Ensure these files are in your repository:
- `streamlit_frontend_database.py`
- `langgraph_database_backend.py`
- `requirements.txt`
- `.gitignore`
- `README.md`

⚠️ **Important:** Do NOT commit your `.env` file!

### Step 2: Deploy to Streamlit Cloud

1. **Sign in to Streamlit Cloud:**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with your GitHub account

2. **Create New App:**
   - Click "New app"
   - Select your repository: `YOUR_USERNAME/LangGraph_Chatbot`
   - Choose branch: `main`
   - Set main file path: `streamlit_frontend_database.py`

3. **Configure Secrets:**
   - Click "Advanced settings"
   - In the "Secrets" section, add:
   ```toml
   GOOGLE_API_KEY = "your_actual_google_api_key_here"
   ```
   - Click "Save"

4. **Deploy:**
   - Click "Deploy!"
   - Wait 2-3 minutes for deployment to complete

5. **Your App is Live! 🎉**
   - You'll get a URL like: `https://your-app-name.streamlit.app`
   - Share this URL in your project submission

### Step 3: Update .env for Streamlit Cloud

Streamlit Cloud reads secrets differently. Update your backend file:

```python
import os
from dotenv import load_dotenv

load_dotenv()

# This works both locally and on Streamlit Cloud
api_key = os.getenv("GOOGLE_API_KEY") or st.secrets.get("GOOGLE_API_KEY")
```

## Method 2: Render (Alternative - FREE)

### Step 1: Create `render.yaml`

Create a file named `render.yaml` in your project root:

```yaml
services:
  - type: web
    name: langgraph-chatbot
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: streamlit run streamlit_frontend_database.py --server.port $PORT --server.address 0.0.0.0
    envVars:
      - key: GOOGLE_API_KEY
        sync: false
```

### Step 2: Deploy to Render

1. Go to [render.com](https://render.com)
2. Sign up/Sign in with GitHub
3. Click "New +" → "Web Service"
4. Connect your repository
5. Set environment variable `GOOGLE_API_KEY`
6. Click "Create Web Service"

## Method 3: Railway (Alternative)

1. Go to [railway.app](https://railway.app)
2. Sign in with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your repository
5. Add environment variable: `GOOGLE_API_KEY`
6. Railway will auto-detect Streamlit and deploy

## Post-Deployment Checklist

✅ App loads without errors  
✅ Can create new chats  
✅ AI responds correctly  
✅ Chat persistence works  
✅ Rename/delete features work  
✅ UI looks good on mobile and desktop  

## Troubleshooting

### Issue: "API Key not found"
**Solution:** Check that `GOOGLE_API_KEY` is correctly set in Streamlit Cloud secrets

### Issue: "Module not found"
**Solution:** Ensure all dependencies are listed in `requirements.txt`

### Issue: Database errors
**Solution:** Streamlit Cloud has ephemeral storage. The database will reset on redeployment. This is expected behavior.

### Issue: App won't start
**Solution:** 
1. Check the logs in Streamlit Cloud
2. Verify `streamlit_frontend_database.py` path is correct
3. Ensure all imports are available in `requirements.txt`

## Updating Your Deployed App

Any push to your GitHub repository will automatically redeploy your app:

```bash
git add .
git commit -m "Update: Added new feature"
git push origin main
```

Streamlit Cloud will detect the changes and redeploy within 1-2 minutes.

## Custom Domain (Optional)

1. In Streamlit Cloud, go to App Settings
2. Click "Custom domain"
3. Follow instructions to add your domain
4. Update DNS records as specified

## Monitoring and Analytics

- **Streamlit Cloud Dashboard:** View app metrics and logs
- **Error Tracking:** Check logs for any runtime errors
- **Usage Stats:** Monitor visitor count and app performance

## Cost

- **Streamlit Cloud:** FREE (1 private app, unlimited public apps)
- **Render Free Tier:** 750 hours/month
- **Railway Free Tier:** $5 credit/month

## Security Best Practices

✅ Never commit `.env` file  
✅ Use Streamlit secrets for API keys  
✅ Keep dependencies updated  
✅ Monitor API usage to avoid overages  
✅ Use `.gitignore` properly  

## Support

If you encounter issues:
1. Check Streamlit Cloud documentation
2. Review deployment logs
3. Verify all environment variables
4. Test locally first

---

**Congratulations! Your app is now live and accessible worldwide! 🌍**

Share your deployment URL in your project submission for extra marks! ⭐
