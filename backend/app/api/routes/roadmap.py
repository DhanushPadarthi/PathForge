# API routes for roadmap generation
from fastapi import APIRouter, HTTPException 
from typing import List 
from bson import ObjectId 
from datetime import datetime, timedelta 
import uuid 
import logging 

from models.roadmap import Roadmap, Module, LearningResource, ResourceStatus, ModuleSummary 
from models.skill import SkillGapAnalysis 
from database.connection import get_collection 
from services.ai_service import AIService 
from pydantic import BaseModel 
from typing import Optional 
from logger_config import roadmap_logger, resource_logger, time_logger, combined_logger 

router = APIRouter() 
ai_service = AIService() 

class GenerateRoadmapRequest(BaseModel): 
    user_id: str 
    target_role_id: Optional[str] = None 
    deadline_weeks: int = 12 
    preferences: Optional[dict] = None  # For additional preferences like difficulty 

@router.post("/generate") 
async def generate_roadmap(request: GenerateRoadmapRequest): 
    """Generate personalized learning roadmap for user""" 
    try: 
        print("\n" + "="*80) 
        print("🚀 [ROADMAP GENERATION] Starting...") 
        print(f"   User ID: {request.user_id}") 
        print(f"   Target Role ID: {request.target_role_id}") 
        print(f"   Deadline: {request.deadline_weeks} weeks") 
        print("="*80) 
        
        # Get user data 
        users_collection = await get_collection("users") 
        user = await users_collection.find_one({"_id": ObjectId(request.user_id)}) 
        
        if not user: 
            print("❌ [ERROR] User not found") 
            raise HTTPException(status_code=404, detail="User not found") 
        
        print(f"✅ [USER] Found user: {user.get('name', 'N/A')}") 
        
        # Use target_role_id from request or user profile 
        target_role_id = request.target_role_id or user.get("target_role_id") 
        if not target_role_id: 
            raise HTTPException(status_code=400, detail="User must set a target role first") 
        
        # Get career role requirements 
        roles_collection = await get_collection("career_roles") 
        career_role = await roles_collection.find_one({"_id": ObjectId(target_role_id)}) 
        
        if not career_role: 
            raise HTTPException(status_code=404, detail="Career role not found") 
        
        # Extract skill names from user skills (which are now objects) 
        user_skills = user.get("current_skills", []) 
        skills_collection = await get_collection("skills") 
        
        current_skill_names = [] 
        for user_skill in user_skills: 
            skill = await skills_collection.find_one({"_id": ObjectId(user_skill["skill_id"])}) 
            if skill: 
                current_skill_names.append(skill["name"]) 
        
        print(f"📚 [SKILLS] Current skills: {current_skill_names}") 
        
        required_skills = career_role.get("required_skills", []) 
        print(f"📚 [SKILLS] Required skills: {required_skills}") 
        
        # Analyze skill gap 
        print("📊 [SKILL GAP] Starting analysis...") 
        skill_gap_analysis = await ai_service.analyze_skill_gap( 
            current_skills=current_skill_names, 
            target_role=career_role["title"], 
            required_skills=required_skills 
        ) 
        print("📊 [SKILL GAP] Analysis result:") 
        print(f"   Skill gaps count: {len(skill_gap_analysis.get('skill_gaps', []))}") 
        print(f"   Sample gap: {skill_gap_analysis.get('skill_gaps', [])[0] if skill_gap_analysis.get('skill_gaps') else 'None'}") 
        print(f"   Recommendations: {skill_gap_analysis.get('recommendations', [])}") 
        
        # Generate roadmap using AI 
        available_hours = user.get("available_hours_per_week", 10) 
        
        # Extract preferences 
        preferences = request.preferences or {} 
        difficulty_level = preferences.get("difficulty", "intermediate") 
        duration_str = preferences.get("duration", "12 weeks") 
        
        # Parse weeks from duration string (e.g., "12 weeks" -> 12) 
        deadline_weeks = request.deadline_weeks 
        if duration_str: 
            try: 
                deadline_weeks = int(duration_str.split()[0]) 
            except: 
                pass 
        
        print("🤖 [AI] Generating roadmap:") 
        print(f"   Skill gaps: {len(skill_gap_analysis.get('skill_gaps', []))}") 
        print(f"   Duration: {deadline_weeks} weeks") 
        print(f"   Difficulty: {difficulty_level}") 
        
        roadmap_data = await ai_service.generate_learning_roadmap( 
            skill_gaps=skill_gap_analysis["skill_gaps"], 
            target_role=career_role["title"], 
            available_hours_per_week=available_hours, 
            deadline_weeks=deadline_weeks, 
            difficulty_level=difficulty_level 
        ) 
        
        # Validate roadmap data 
        if not roadmap_data.get("modules"): 
            raise HTTPException( 
                status_code=500, 
                detail="AI service failed to generate roadmap modules. Please try again or check OpenAI API status." 
            ) 
        
        # Structure the roadmap with weekly organization 
        modules = [] 
        total_weeks = deadline_weeks or 12 
        total_modules = len(roadmap_data.get("modules", [])) 
        
        # Calculate week assignment for each module to evenly distribute across duration 
        # Each module gets a proportional week range 
        weeks_per_module = total_weeks / total_modules if total_modules > 0 else 1 
        
        for idx, module_data in enumerate(roadmap_data.get("modules", [])): 
            # Calculate module hours 
            module_hours = module_data.get("estimated_hours") 
            if module_hours is None: 
                # Estimate from resources 
                module_hours = sum(r.get("estimated_hours", 0) for r in module_data.get("resources", [])) 
            
            module_hours = float(module_hours) if module_hours else 0.0 
            
            # Assign week number based on even distribution 
            current_week = int(idx * weeks_per_module) + 1 
            previous_week = int((idx - 1) * weeks_per_module) + 1 if idx > 0 else 1 
            
            # Now create resources with correct week-based unlocking 
            resources = [] 
            for r_idx, resource_data in enumerate(module_data.get("resources", [])): 
                # Unlock first resource of first module in each week 
                is_week_start = (idx == 0 or current_week != previous_week) 
                should_unlock = is_week_start and r_idx == 0 
                
                resource = LearningResource( 
                    id=str(uuid.uuid4()), 
                    title=resource_data["title"], 
                    url=resource_data["url"], 
                    description=resource_data.get("description", ""), 
                    estimated_hours=resource_data["estimated_hours"], 
                    resource_type=resource_data["resource_type"], 
                    status=ResourceStatus.UNLOCKED if should_unlock else ResourceStatus.LOCKED, 
                    order=r_idx, 
                    time_spent_seconds=0 
                ) 
                resources.append(resource) 
            
            module = Module( 
                id=str(uuid.uuid4()), 
                title=module_data["title"], 
                description=module_data["description"], 
                skills_covered=module_data["skills_covered"], 
                resources=resources, 
                estimated_total_hours=module_hours, 
                week_number=current_week, 
                order=idx, 
                is_completed=False 
            ) 
            modules.append(module) 
        
        # Calculate total hours 
        total_hours = sum(m.estimated_total_hours for m in modules) 
        
        # Create roadmap 
        roadmap = Roadmap( 
            user_id=request.user_id, 
            target_role=career_role["title"], 
            skill_gaps=skill_gap_analysis["skill_gaps"], 
            modules=modules, 
            total_estimated_hours=total_hours, 
            deadline=datetime.utcnow() + timedelta(weeks=request.deadline_weeks), 
            progress_percentage=0.0, 
            current_module_index=0 
        ) 
        
        print("💾 [ROADMAP] Created roadmap object:") 
        print(f"   Target role: {roadmap.target_role}") 
        print(f"   Skill gaps count: {len(roadmap.skill_gaps)}") 
        print(f"   Modules count: {len(roadmap.modules)}") 
        print(f"   First skill gap: {roadmap.skill_gaps[0] if roadmap.skill_gaps else 'None'}") 
        
        # Save to database 
        roadmaps_collection = await get_collection("roadmaps") 
        
        # Insert new roadmap (keeping existing ones) 
        result = await roadmaps_collection.insert_one(roadmap.dict(by_alias=True, exclude={"id"})) 
        
        print(f"✅ [ROADMAP] Saved to database with ID: {result.inserted_id}") 
        print("="*80 + "\n") 
        
        return { 
            "message": "Roadmap generated successfully", 
            "_id": str(result.inserted_id), 
            "roadmap_id": str(result.inserted_id), 
            "total_modules": len(modules), 
            "total_hours": total_hours, 
            "skill_gaps": skill_gap_analysis["skill_gaps"] 
        } 
        
    except Exception as e: 
        import traceback 
        print("\n❌ [ERROR] Roadmap generation failed!") 
        print(f"   Error type: {type(e).__name__}") 
        print(f"   Error message: {str(e)}") 
        print(f"   Traceback:") 
        traceback.print_exc() 
        raise HTTPException(status_code=500, detail=f"Roadmap generation failed: {str(e)}") 
﻿# API routes for roadmap generation
# To be implemented
