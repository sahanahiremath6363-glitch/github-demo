import json

def analyse_resume(resume_text, user_goal):
    return {
        "skills": ["Python", "SQL", "Flask"],
        "missing_skills": ["Machine Learning", "Docker"],
        "roadmap": [
            "Learn Pandas",
            "Learn NumPy",
            "Build ML Projects"
        ],
        "interview_questions": [
            "What is Flask?",
            "What is SQLAlchemy?",
            "Explain REST APIs."
        ]
    }