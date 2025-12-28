from openai import OpenAI
from typing import List, Dict
import json
import logging
from ..config.settings import settings

logger = logging.getLogger(__name__)

class AIService:
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.model = settings.OPENAI_MODEL
    
    async def extract_skills_from_text(self, resume_text: str) -> List[str]:
        """
        Extract technical skills from resume text using ChatGPT
        """
        try:
            prompt = f"""
            Extract all technical skills from the following resume text.
            Return ONLY a JSON array of skills (no explanations).
            Focus on: programming languages, frameworks, tools, databases, cloud platforms.
            
            Resume:
            {resume_text[:3000]}  # Limit to avoid token limits
            
            Return format: ["Python", "JavaScript", "React", "MongoDB", "AWS"]
            """
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a technical recruiter expert at identifying skills from resumes. Return only valid JSON arrays."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=500
            )
            
            skills_text = response.choices[0].message.content.strip()
            # Parse JSON response
            skills = json.loads(skills_text)
            
            logger.info(f"Extracted {len(skills)} skills from resume")
            return skills
            
        except Exception as e:
            logger.error(f"Error extracting skills: {e}")
            return []
    
    async def analyze_skill_gap(self, current_skills: List[str], required_skills: List[str]) -> Dict:
        """
        Analyze the gap between current and required skills
        """
        try:
            current_set = set([s.lower() for s in current_skills])
            required_set = set([s.lower() for s in required_skills])
            
            # Skills the user already has
            matching_skills = list(current_set.intersection(required_set))
            
            # Skills the user needs to learn
            missing_skills = list(required_set - current_set)
            
            # Calculate completion percentage
            if required_skills:
                completion_percentage = (len(matching_skills) / len(required_skills)) * 100
            else:
                completion_percentage = 0
            
            return {
                "matching_skills": matching_skills,
                "missing_skills": missing_skills,
                "completion_percentage": round(completion_percentage, 2),
                "total_required": len(required_skills),
                "total_current": len(current_skills)
            }
            
        except Exception as e:
            logger.error(f"Error analyzing skill gap: {e}")
            return {
                "matching_skills": [],
                "missing_skills": required_skills,
                "completion_percentage": 0
            }
    
    async def generate_learning_path(self, missing_skills: List[str], learning_time: str, deadline: str) -> List[Dict]:
        """
        Generate a structured learning path using AI
        """
        try:
            prompt = f"""
            Create a learning roadmap for these skills: {', '.join(missing_skills)}
            Available learning time: {learning_time} per day
            Deadline: {deadline}
            
            Return a JSON array of learning modules with this structure:
            [{{
                "module_name": "Module name",
                "skills_covered": ["skill1", "skill2"],
                "duration_days": 7,
                "topics": ["topic1", "topic2"]
            }}]
            
            Order modules from beginner to advanced.
            """
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are an expert learning path designer. Return only valid JSON."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.5,
                max_tokens=1500
            )
            
            modules_text = response.choices[0].message.content.strip()
            modules = json.loads(modules_text)
            
            return modules
            
        except Exception as e:
            logger.error(f"Error generating learning path: {e}")
            return []

# Global AI service instance
ai_service = AIService()
# Module summary generation
