
import pdfplumber
from docx import Document
import re

def extract_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def extract_docx(file):
    doc = Document(file)
    return "\n".join(p.text for p in doc.paragraphs)

def parse_resume_sections(text: str):
    text = text.lower()

    sections = {"skills": "", "experience": "", "education": ""}

    patterns = {
        "skills": r"(skills|technical skills)(.*?)(experience|education|projects|$)",
        "experience": r"(experience)(.*?)(skills|education|projects|$)",
        "education": r"(education)(.*?)(skills|experience|projects|$)"
    }

    for key, pattern in patterns.items():
        match = re.search(pattern, text, re.S)
        if match:
            sections[key] = match.group(2)

    return sections
