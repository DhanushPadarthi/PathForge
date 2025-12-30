import re

SECTION_HEADERS = {
    "skills": ["skills", "technical skills", "technologies"],
    "education": ["education", "academic background"],
    "experience": ["experience", "work experience", "internships", "projects"]
}

def parse_sections(text: str) -> dict:
    sections = {key: "" for key in SECTION_HEADERS}

    lines = text.split("\n")
    current_section = None

    for line in lines:
        line_clean = line.strip()

        for section, keywords in SECTION_HEADERS.items():
            if any(k in line_clean for k in keywords):
                current_section = section
                break

        if current_section:
            sections[current_section] += line_clean + "\n"

    return sections
