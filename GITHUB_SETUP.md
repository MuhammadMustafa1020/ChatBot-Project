# 📦 GitHub Setup & Submission Instructions

## Step-by-Step Guide to Submit Your Project

### Step 1: Create GitHub Repository

1. **Go to GitHub:**
   - Visit [github.com](https://github.com)
   - Sign in to your account

2. **Create New Repository:**
   - Click the "+" icon → "New repository"
   - Repository name: `LangGraph_Chatbot` (or your preferred name)
   - Description: "AI Chatbot with LangGraph state management and persistent memory"
   - Select **Public** (required for submission)
   - ❌ Do NOT initialize with README (we already have one)
   - Click "Create repository"

### Step 2: Prepare Your Local Repository

1. **Open Terminal/PowerShell** in your project folder:
```bash
cd "C:\Users\Ammar Khan\Desktop\LangGraph_Chatbot"
```

2. **Initialize Git** (if not already done):
```bash
git init
```

3. **Check what files will be committed:**
```bash
git status
```

**Important:** Verify that `.env` and `chatbot.db` are NOT listed (they should be ignored by `.gitignore`)

### Step 3: Commit Your Code

1. **Add all files:**
```bash
git add .
```

2. **Commit with a message:**
```bash
git commit -m "Initial commit: LangGraph AI Chatbot with persistent memory"
```

### Step 4: Push to GitHub

1. **Add remote repository:**
```bash
git remote add origin https://github.com/YOUR_USERNAME/LangGraph_Chatbot.git
```

Replace `YOUR_USERNAME` with your actual GitHub username.

2. **Set main branch:**
```bash
git branch -M main
```

3. **Push to GitHub:**
```bash
git push -u origin main
```

If prompted, enter your GitHub credentials or use a personal access token.

### Step 5: Verify Repository

1. **Visit your repository:** `https://github.com/YOUR_USERNAME/LangGraph_Chatbot`

2. **Check that these files are present:**
   - ✅ README.md
   - ✅ requirements.txt
   - ✅ .gitignore
   - ✅ GROUP_DETAILS.md
   - ✅ DEPLOYMENT.md
   - ✅ UNIQUE_FEATURES.md
   - ✅ DEMO_VIDEO_SCRIPT.md
   - ✅ streamlit_frontend_database.py
   - ✅ langgraph_database_backend.py
   - ✅ All other Python files

3. **Verify these files are NOT present:**
   - ❌ .env (should be in .gitignore)
   - ❌ chatbot.db (should be in .gitignore)
   - ❌ .venv/ folder
   - ❌ __pycache__/

### Step 6: Update GROUP_DETAILS.md

1. **Edit GROUP_DETAILS.md** on GitHub or locally
2. **Fill in your actual information:**
   - Full names
   - Student IDs
   - Emails
   - Roles/contributions

3. **Commit changes:**
```bash
git add GROUP_DETAILS.md
git commit -m "Updated group member details"
git push
```

### Step 7: Optional - Deploy the App

Follow the instructions in [DEPLOYMENT.md](DEPLOYMENT.md) to deploy on Streamlit Cloud.

**Benefits of deployment:**
- ⭐ Extra marks
- 🌐 Live demo for instructors
- 📱 Access from anywhere
- 💼 Portfolio piece

### Step 8: Record Demo Video

1. **Follow the script** in [DEMO_VIDEO_SCRIPT.md](DEMO_VIDEO_SCRIPT.md)
2. **Upload to YouTube/Google Drive**
3. **Update README.md** with video link:

```bash
# Edit README.md and add video link under "Demo Video" section
git add README.md
git commit -m "Added demo video link"
git push
```

### Step 9: Final Submission Checklist

Before submitting, verify:

✅ **Repository is PUBLIC**  
✅ **README.md is complete and professional**  
✅ **GROUP_DETAILS.md has all member information**  
✅ **requirements.txt lists all dependencies**  
✅ **.gitignore is working** (no .env or .db files in repo)  
✅ **Code is clean and well-commented**  
✅ **Demo video is uploaded and linked**  
✅ **Deployment URL added** (if deployed)  
✅ **All files are committed and pushed**  

### Step 10: Submit

Submit the following to your instructor:

1. **GitHub Repository URL:**
   ```
   https://github.com/YOUR_USERNAME/LangGraph_Chatbot
   ```

2. **Deployed App URL** (if applicable):
   ```
   https://your-app-name.streamlit.app
   ```

3. **Demo Video Link:**
   ```
   https://youtu.be/YOUR_VIDEO_ID
   or
   https://drive.google.com/file/d/YOUR_FILE_ID/view
   ```

4. **Group Details:**
   - Already in the repository as GROUP_DETAILS.md

---

## Common Git Commands Reference

### First Time Setup
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Daily Workflow
```bash
# Check status
git status

# Add files
git add .

# Commit changes
git commit -m "Description of changes"

# Push to GitHub
git push

# Pull latest changes
git pull
```

### Fixing Mistakes

**Forgot to add a file:**
```bash
git add filename.py
git commit --amend --no-edit
git push -f
```

**Want to undo last commit (keep changes):**
```bash
git reset --soft HEAD~1
```

**Accidentally committed .env:**
```bash
git rm --cached .env
git commit -m "Removed .env from tracking"
git push
```

---

## Troubleshooting

### Issue: "Permission denied (publickey)"
**Solution:** Set up SSH key or use HTTPS with personal access token
- [GitHub SSH Setup](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)

### Issue: "Repository not found"
**Solution:** Check the repository URL and ensure it's public

### Issue: ".env file in repository"
**Solution:**
```bash
git rm --cached .env
git commit -m "Removed .env"
git push
```

### Issue: "Large file warning"
**Solution:** chatbot.db might be too large. It should be in .gitignore
```bash
git rm --cached chatbot.db
git commit -m "Removed database file"
git push
```

---

## Tips for Success

1. **Commit often** with meaningful messages
2. **Test locally** before pushing
3. **Don't commit sensitive data** (.env files, API keys)
4. **Write clear documentation**
5. **Make README attractive** with badges and emojis
6. **Deploy if possible** for extra marks
7. **Make a good demo video** - this is what instructors will watch!

---

## Submission Format Example

**Email/Submission Portal:**

```
Subject: Semester Project Submission - LangGraph AI Chatbot

Dear [Instructor Name],

Please find our semester project submission below:

Project Name: LangGraph AI Chatbot with Persistent Memory

GitHub Repository: https://github.com/YOUR_USERNAME/LangGraph_Chatbot
Deployed Application: https://langgraph-chatbot.streamlit.app
Demo Video: https://youtu.be/YOUR_VIDEO_ID

Group Members:
- [Member 1 Name] - [Student ID]
- [Member 2 Name] - [Student ID]

Key Features:
- LangGraph state management
- Persistent conversation storage
- Real-time streaming responses
- ChatGPT-like professional UI

All required files including README, GROUP_DETAILS, and deployment instructions are in the repository.

Thank you!

Best regards,
[Your Name]
```

---

**You're all set! Good luck with your submission! 🚀**
