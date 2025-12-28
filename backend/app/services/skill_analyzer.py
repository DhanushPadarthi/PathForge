from typing import List, Dict
import logging
from .ai_service import ai_service
from ..config.mongodb import db

logger = logging.getLogger(__name__)

class SkillAnalyzer:
    
    async def analyze_resume_skills(self, resume_text: str) -> List[str]:
        """
        Extract and analyze skills from resume text
        """
        try:
            # Use AI service to extract skills
            skills = await ai_service.extract_skills_from_text(resume_text)
            
            # Clean and normalize skills
            cleaned_skills = self._clean_skills(skills)
            
            return cleaned_skills
            
        except Exception as e:
            logger.error(f"Error analyzing resume skills: {e}")
            return []
    
    async def compare_with_career_role(self, user_skills: List[str], career_role_id: str) -> Dict:
        """
        Compare user skills with career role requirements
        """
        try:
            # Get career role from database
            career_roles_collection = db.get_collection("career_roles")
            career_role = await career_roles_collection.find_one({"_id": career_role_id})
            
            if not career_role:
                raise ValueError(f"Career role not found: {career_role_id}")
            
            required_skills = career_role.get("required_skills", [])
            
            # Use AI service to analyze gap
            gap_analysis = await ai_service.analyze_skill_gap(user_skills, required_skills)
            
            return {
                "career_role": career_role.get("name"),
                "user_skills": user_skills,
                "required_skills": required_skills,
                "gap_analysis": gap_analysis
            }
            
        except Exception as e:
            logger.error(f"Error comparing skills: {e}")
            raise
    
    def _clean_skills(self, skills: List[str]) -> List[str]:
        """
        Clean and normalize skill names
        """
        cleaned = []
        for skill in skills:
            # Remove extra whitespace
            cleaned_skill = ' '.join(skill.split())
            # Capitalize properly
            if cleaned_skill and len(cleaned_skill) > 1:
                cleaned.append(cleaned_skill)
        
        # Remove duplicates (case-insensitive)
        seen = set()
        unique_skills = []
        for skill in cleaned:
            skill_lower = skill.lower()
            if skill_lower not in seen:
                seen.add(skill_lower)
                unique_skills.append(skill)
        
        return unique_skills

# Global analyzer instance
skill_analyzer = SkillAnalyzer()
