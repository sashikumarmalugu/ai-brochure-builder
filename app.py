

import streamlit as st
import requests
from bs4 import BeautifulSoup
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
import io

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2"

st.set_page_config(
    page_title="AI Company Brochure Builder",
    page_icon="📘",
    layout="wide"
)

st.markdown(
    """
    <style>
        body {
            background: linear-gradient(to bottom, #f8fafc, #eef2ff);
        }
        .hero {
            background: linear-gradient(90deg, #6366f1, #4f46e5);
            padding: 40px;
            border-radius: 20px;
            color: white;
            text-align: center;
            margin-bottom: 30px;
        }
        .hero h1 {
            font-size: 46px;
            font-weight: 800;
        }
        .hero p {
            font-size: 18px;
            opacity: 0.95;
        }
        .scroll-banner {
            overflow: hidden;
            white-space: nowrap;
            background: #111827;
            color: white;
            padding: 12px;
            border-radius: 12px;
            margin-bottom: 25px;
        }
        .scroll-text {
            display: inline-block;
            animation: scroll-left 18s linear infinite;
            font-weight: 500;
        }
        @keyframes scroll-left {
            from { transform: translateX(100%); }
            to { transform: translateX(-100%); }
        }
        .card {
            padding: 28px;
            border-radius: 18px;
            background: white;
            box-shadow: 0 12px 30px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        .cta-btn button {
            background: linear-gradient(90deg, #6366f1, #4f46e5);
            color: white;
            font-weight: 700;
            border-radius: 12px;
            height: 48px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

def extract_website_text(url: str, max_chars: int = 8000) -> str:
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        for tag in soup(["script", "style", "noscript"]):
            tag.decompose()
        text = " ".join(soup.stripped_strings)
        return text[:max_chars]
    except:
        return ""


def call_ollama(prompt: str) -> str:
    payload = {"model": MODEL_NAME, "prompt": prompt, "stream": False}
    response = requests.post(OLLAMA_URL, json=payload)
    return response.json().get("response", "")


def generate_pdf(company_name: str, brochure_text: str) -> bytes:
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=LETTER)
    width, height = LETTER

    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(50, height - 50, f"{company_name} – Company Brochure")

    pdf.setFont("Helvetica", 11)
    y = height - 90

    for line in brochure_text.split("\n"):
        if y < 50:
            pdf.showPage()
            pdf.setFont("Helvetica", 11)
            y = height - 50
        pdf.drawString(50, y, line[:110])
        y -= 14

    pdf.save()
    buffer.seek(0)
    return buffer.getvalue()

st.markdown(
    """
    <div class="hero">
        <h1>📘 AI Company Brochure Builder</h1>
        <p>Investor-ready • Client-ready • Recruiter-ready — in seconds</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="scroll-banner">
        <div class="scroll-text">
            🚀 Private AI • 📄 Executive-grade Output • 🔒 No Data Leaves Your System • ⚡ Instant PDF • 💼 Built for Founders & Teams
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        company_name = st.text_input("🏢 Company Name", placeholder="e.g. Stripe")
    with col2:
        website_url = st.text_input("🌐 Company Website", placeholder="https://stripe.com")

    target_audience = st.multiselect(
        "🎯 Target Audience",
        ["Prospective Clients", "Investors", "Potential Recruits"],
        default=["Prospective Clients", "Investors"]
    )

    tone = st.selectbox(
        "🖋️ Brochure Tone",
        ["Professional", "Visionary", "Friendly", "Bold & Confident"]
    )

    generate_btn = st.button("🚀 Generate Brochure", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

if generate_btn and company_name and website_url:
    with st.spinner("Analyzing company and crafting brochure..."):
        website_text = extract_website_text(website_url)

        prompt = f"""
You are a senior marketing strategist.

Create a polished business brochure.

Company Name: {company_name}
Website Content: {website_text}
Target Audience: {', '.join(target_audience)}
Tone: {tone}

Structure:
1. Company Overview
2. Problem We Solve
3. Products / Services
4. Differentiators
5. Market Vision
6. Culture & Careers
7. Call to Action

Write in a crisp, executive brochure format.
"""

        brochure = call_ollama(prompt)

    st.success("Brochure generated successfully!")

    # Display
    st.markdown("### 📄 Generated Brochure")
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown(brochure)
    st.markdown("</div>", unsafe_allow_html=True)

    # Downloads
    pdf_bytes = generate_pdf(company_name, brochure)

    col1, col2 = st.columns(2)
    with col1:
        st.download_button(
            "⬇️ Download as PDF",
            data=pdf_bytes,
            file_name=f"{company_name}_brochure.pdf",
            mime="application/pdf"
        )
    with col2:
        st.download_button(
            "⬇️ Download as Text",
            data=brochure,
            file_name=f"{company_name}_brochure.txt",
            mime="text/plain"
        )

st.markdown("---")
st.caption("Built with Streamlit • Ollama • Executive-grade Private AI")
