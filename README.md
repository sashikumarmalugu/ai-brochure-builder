# 📘 AI Company Brochure Builder
<img width="1512" height="982" alt="Screenshot 2026-02-01 at 9 30 50 PM" src="https://github.com/user-attachments/assets/8797d36f-f9a6-4815-a631-f71fc3bdb4b0" />


An AI-powered web app that turns a company’s website into an **investor-ready, client-ready, and recruiter-ready business brochure** — complete with a downloadable PDF.

Built as a focused product experiment to explore how **AI + opinionated workflows** can produce real, usable business artifacts (not just raw text).

---

## ✨ What This App Does

Given a company name and website URL, the app:

- Extracts and cleans website content
- Uses the **latest OpenAI OSS model** to generate a structured company brochure
- Enforces a professional, business-safe format
- Produces output that can be **downloaded as a PDF or text**
- Requires **no prompt engineering** from the user

This is designed for **business stakeholders** who want a finished deliverable, not a chat interface.

---

## 🤔 Why Not Just Use ChatGPT?

ChatGPT is a powerful general-purpose tool, but business users often need:

- A guided workflow
- Consistent structure
- Predictable output
- Shareable artifacts (PDFs)
- Zero prompt iteration

**ChatGPT helps you write.  
This app helps you ship.**

---

## 🧠 Key Features

- 🏢 Company website analysis
- 🎯 Audience-specific brochures (Investors, Clients, Recruits)
- 🖋️ Tone control (Professional, Visionary, Friendly, Bold)
- 📄 One-click PDF download
- 🎨 Premium, executive-style UI
- ⚡ Fast, lightweight, low-infra architecture

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **AI Model:** OpenAI (latest OSS-compatible model)
- **PDF Generation:** ReportLab
- **Web Scraping:** BeautifulSoup
- **Deployment:** Streamlit Cloud (recommended)

---

<img width="1512" height="982" alt="Screenshot 2026-02-01 at 9 30 50 PM" src="https://github.com/user-attachments/assets/1f1c6067-99e9-4685-bd52-3bac40bd70ea" />

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/ai-brochure-builder.git
cd ai-brochure-builder
