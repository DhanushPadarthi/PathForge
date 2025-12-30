import json
from typing import List, Dict
from fastapi import HTTPException
from app.models.resource import Resource
from app.services.ai_service import groq_client


class ResourceRecommenderService:
    """
    Generates learning resource recommendations using Groq LLM
    """

    @staticmethod
    def _build_prompt(skills: List[str]) -> str:
        skills_text = ", ".join(skills)

        return f"""
You are an expert learning advisor.

For the following skills:
{skills_text}

Recommend 2 high-quality learning resources PER skill.

Rules:
- Beginner to intermediate friendly
- Prefer official docs, reputable platforms
- Return ONLY valid JSON
- Do NOT include markdown or explanations

Strict JSON format:
{{
  "resources": [
    {{
      "skill": "Python",
      "title": "Official Python Docs",
      "link": "https://docs.python.org/3/",
      "estimated_time_minutes": 45
    }}
  ]
}}
"""

    @staticmethod
    def recommend_resources(input_data: Dict) -> Dict:
        if "skills" not in input_data or not isinstance(input_data["skills"], list):
            raise HTTPException(status_code=400, detail="'skills' must be a list")

        skills = input_data["skills"]
        prompt = ResourceRecommenderService._build_prompt(skills)

        try:
            response = groq_client.chat.completions.create(
                model="llama-3.1-8b-instant",  # ✅ FIXED MODEL
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.1,
            )
        except Exception as e:
            raise HTTPException(
                status_code=502,
                detail=f"Groq API error: {str(e)}"
            )

        raw_output = response.choices[0].message.content.strip()

        try:
            parsed = json.loads(raw_output)
        except json.JSONDecodeError:
            raise HTTPException(
                status_code=502,
                detail="Invalid JSON returned by Groq"
            )

        validated_resources = []

        for item in parsed.get("resources", []):
            try:
                resource = Resource(
                    skill=item["skill"],
                    title=item["title"],
                    link=item["link"],
                    estimated_time_minutes=item["estimated_time_minutes"]
                )
                validated_resources.append(resource.dict())
            except Exception:
                continue

        return {
            "count": len(validated_resources),
            "resources": validated_resources
        }
