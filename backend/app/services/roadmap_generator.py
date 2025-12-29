# Roadmap generation service
import json

async def generate_learning_roadmap(
    self,
    skill_gaps,
    target_role,
    available_hours_per_week,
    deadline_weeks,
    difficulty_level
):
    total_hours = available_hours_per_week * deadline_weeks

    # Calculate module structure based on duration
    if deadline_weeks <= 4:
        num_modules = "2-3"
    elif deadline_weeks <= 8:
        num_modules = "3-4"
    elif deadline_weeks <= 12:
        num_modules = "4-6"
    # ...

    # AI prompt generates structured modules with resources
    prompt = (
        f"Create learning plan for {target_role}\n"
        f"- Skills: {skill_gaps}\n"
        f"- Duration: {deadline_weeks} weeks\n"
        f"- Hours: {total_hours} total\n"
        f"- Difficulty: {difficulty_level}\n\n"
        "Return JSON with modules, each containing:\n"
        "- title, description, skills_covered\n"
        "- estimated_hours\n"
        "- resources (title, url, type, hours)"
    )

    response = await self.client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"}
    )

    return json.loads(response.choices[0].message.content)
﻿# Roadmap generation service
# To be implemented
