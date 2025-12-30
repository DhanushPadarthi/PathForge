KNOWN_SKILLS = {
    "programming": [
        "python", "java", "c", "c++"
    ],
    "web": [
        "html", "css", "javascript", "react", "node", "fastapi"
    ],
    "database": [
        "mysql", "mongodb", "firebase"
    ],
    "core_cs": [
        "data structures", "oops", "operating systems", "computer networks"
    ],
    "tools": [
        "git", "github"
    ]
}

def extract_skills(text: str) -> dict:
    found = {}

    for category, skills in KNOWN_SKILLS.items():
        found[category] = []
        for skill in skills:
            if skill in text:
                found[category].append(skill)

    return found

def gap_analysis(resume_skills: dict, required_skills: list[str]) -> dict:
    flat_resume_skills = {s for v in resume_skills.values() for s in v}

    matched = []
    missing = []

    for skill in required_skills:
        if skill.lower() in flat_resume_skills:
            matched.append(skill)
        else:
            missing.append(skill)

    score = round((len(matched) / len(required_skills)) * 100, 2) if required_skills else 0

    return {
        "matched_skills": matched,
        "missing_skills": missing,
        "match_percentage": score
    }
