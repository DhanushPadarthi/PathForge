# AI service for skill analysis and roadmap generation
from groq import Groq
import os
import json
from typing import List, Dict
from dotenv import load_dotenv

load_dotenv()

class AIService:
    """Service to interact with Groq API for skill extraction and roadmap
    generation"""

    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.model = "llama-3.3-70b-versatile"

    async def extract_skills_from_resume(self, resume_text: str) -> Dict:
        """Extract skills and experience from resume text using AI"""
        prompt = f"""
        Analyze the following resume and extract structured information.

        Resume Text:
        {resume_text}

        Extract and return ONLY a JSON object with the following
        structure:
        {{
            "skills": ["skill1", "skill2", ...],
            "experience_years": <number>,
            "education": "highest degree",
            "job_titles": ["title1", "title2", ...]
        }}

        Focus on technical skills, frameworks, programming languages, and
        tools.
        """

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3,
                response_format={"type": "json_object"}
            )

            result = json.loads(response.choices[0].message.content)
            return result
        except Exception as e:
            print(f"Error in AI skill extraction: {e}")
            return {
                "skills": [],
                "experience_years": 0,
                "education": "",
                "job_titles": []
            }

    async def analyze_skill_gap(
        self,
        current_skills: List[str],
        target_role: str,
        required_skills: List[str]
    ) -> Dict:
        """Analyze skill gaps for a target role"""
        prompt = f"""
        Analyze the skill gap for a student targeting the role:
        {target_role}

        Current Skills: {', '.join(current_skills) if current_skills else 'None'}
        Required Skills for {target_role}: {', '.join(required_skills)}

        For each missing skill, determine the current level, required
        level, gap severity, and learning priority.

        Return ONLY a JSON object with this EXACT structure:
        {{
            "skill_gaps": [
                {{
                    "skill": "skill name",
                    "current_level": "None" or "Beginner" or
                    "Intermediate" or "Advanced",
                    "required_level": "Beginner" or "Intermediate" or
                    "Advanced" or "Expert",
                    "gap_severity": "High" or "Medium" or "Low",
                    "learning_priority": "High" or "Medium" or "Low"
                }}
            ],
            "matching_skills": ["skill1", "skill2"],
            "match_percentage": <number 0-100>,
            "priority_skills": ["most important skill to learn first"],
            "recommendations": ["recommendation 1", "recommendation 2"]
        }}
        """

        try:
            print("\n🤖 [AI SKILL GAP] Calling Groq API...")
            print(f"   Current skills: {current_skills}")
            print(f"   Required skills: {required_skills}")

            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3,
                response_format={"type": "json_object"}
            )

            result = json.loads(response.choices[0].message.content)

            print("✅ [AI SKILL GAP] Response received:")
            print(f"   Skill gaps: {len(result.get('skill_gaps', []))}")
            print(
                f"   Sample: "
                f"{result.get('skill_gaps', [])[0] if result.get('skill_gaps') else 'None'}"
            )

            return result

        except Exception as e:
            print(f"❌ [AI SKILL GAP] Error: {e}")
            print("   Using fallback data...")

            missing_skills = list(set(required_skills) - set(current_skills))
            fallback = {
                "skill_gaps": [
                    {
                        "skill": skill,
                        "current_level": "None",
                        "required_level": "Intermediate",
                        "gap_severity": "Medium",
                        "learning_priority": "Medium"
                    }
                    for skill in missing_skills
                ],
                "matching_skills": list(set(required_skills) & set(current_skills)),
                "match_percentage": 0,
                "priority_skills": (
                    missing_skills[:3]
                    if len(missing_skills) >= 3
                    else missing_skills
                ),
                "recommendations": [
                    "Focus on foundational skills first",
                    "Practice with hands-on projects",
                    "Join online communities for support"
                ]
            }

            print(f"   Fallback skill gaps: {len(fallback['skill_gaps'])}")
            return fallback

    async def generate_learning_roadmap(
        self,
        skill_gaps: List,
        target_role: str,
        available_hours_per_week: int,
        deadline_weeks: int,
        difficulty_level: str = "intermediate"
    ) -> Dict:
        """Generate a personalized learning roadmap"""

        if available_hours_per_week is None:
            available_hours_per_week = 10
        if deadline_weeks is None:
            deadline_weeks = 12

        total_hours = available_hours_per_week * deadline_weeks

        if skill_gaps and isinstance(skill_gaps[0], dict):
            skill_names = [gap['skill'] for gap in skill_gaps]
        else:
            skill_names = skill_gaps

        print("\n🤖 [AI ROADMAP] Generating roadmap...")
        print(f"   Skills to learn: {skill_names}")
        print(f"   Available hours: {total_hours}")
        print(f"   Duration: {deadline_weeks} weeks")
        print(f"   Difficulty: {difficulty_level}")

        difficulty_guidance = {
            "beginner": """Focus on fundamentals and step-by-step tutorials.
Include more introductory content, basic concepts, and foundational
knowledge. Use beginner-friendly resources with detailed explanations.
Start with absolute basics.""",

            "intermediate": """Balance between theory and practice. Include
intermediate tutorials and hands-on projects. Assume basic programming
knowledge. Cover standard industry practices and common patterns.""",

            "advanced": """Focus on advanced concepts, best practices, and
complex projects. Include deep-dive content, architecture patterns,
production-ready implementations, and cutting-edge techniques."""
        }

        guidance = difficulty_guidance.get(
            difficulty_level,
            difficulty_guidance["intermediate"]
        )

        prompt = f"""
        Create a detailed learning roadmap for someone targeting:
        {target_role}

        PARAMETERS:
        - Skills to learn: {', '.join(skill_names)}
        - Total Duration: {deadline_weeks} WEEKS
        - Study Time: {available_hours_per_week} hours/week
          (Total: {total_hours} hours)
        - Difficulty Level: {difficulty_level.upper()}

        DIFFICULTY LEVEL REQUIREMENTS:
        {guidance}
        """

        try:
            print("   Calling Groq API for roadmap generation...")
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                response_format={"type": "json_object"}
            )

            result = json.loads(response.choices[0].message.content)

            print(
                f"✅ [AI ROADMAP] Generated "
                f"{len(result.get('modules', []))} modules"
            )

            if not result.get("modules"):
                raise ValueError("AI did not return any modules")

            return result

        except Exception as e:
            print(f"❌ [AI ROADMAP] Error: {e}")
            print("   Using fallback modules...")

            return {
                "modules": [
                    {
                        "title": "Learn Fundamentals",
                        "description": "Get started with the basics",
                        "skills_covered": skill_names,
                        "estimated_hours": 20,
                        "order": 0,
                        "resources": []
                    }
                ]
            }

