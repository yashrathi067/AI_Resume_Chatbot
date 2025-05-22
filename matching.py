def match_resume_to_job(resume_data, job_role):
    """Matches resume data to a job role and determines qualification."""

    if not resume_data:
        return False, "No resume data provided."

    qualified = True
    reasons = []

    # Check required skills
    if "skills" in job_role and "skills" in resume_data:
        for skill in job_role["skills"]:
            if skill.lower() not in [s.lower() for s in resume_data["skills"]]:
                qualified = False
                reasons.append(f"Missing required skill: {skill}")

    # Check qualifications (very basic string matching)
    if "qualifications" in job_role and "education" in resume_data:
        if job_role["qualifications"].lower() not in [edu.lower() for edu in resume_data["education"]]:
            qualified = False
            reasons.append(f"Qualification not met: {job_role['qualifications']}")

    # Check experience (very basic - needs more robust parsing)
    if "experience" in job_role and "experience" in resume_data:
        #  This is a placeholder -  Implement proper experience extraction and comparison
        if not resume_data["experience"]:
            qualified = False
            reasons.append("Experience not specified in resume")

    return qualified, reasons

def get_job_role_details(job_title, job_roles):
    """Retrieves details of a job role given its title."""
    for role in job_roles:
        if role["title"].lower() == job_title.lower():
            return role
    return None

if __name__ == '__main__':
    # Example Usage
    resume_data = {
        "skills": ["Python", "SQL", "Communication"],
        "education": ["B.S. in CS"],
        "experience": ["5 years"] # This needs better parsing to be useful
    }
    job_role = {
        "title": "Developer",
        "skills": ["Python", "SQL", "JavaScript"],
        "qualifications": "BS in CS",
        "experience": "2+ years"
    }

    qualified, reasons = match_resume_to_job(resume_data, job_role)
    print(f"Is qualified for {job_role['title']}?: {qualified}")
    if not qualified:
        print("Reasons:", reasons)

    job_roles = [
        {"title": "Developer", "skills": ["Python", "JavaScript", "Git"], "qualifications": "BS in CS", "experience": "2+ years"},
        {"title": "Tester", "skills": ["QA", "Testing", "Agile"], "qualifications": "BS in any field", "experience": "1+ years"},
        {"title": "Data Analyst", "skills": ["SQL", "Excel", "Statistics"], "qualifications": "BS in Statistics", "experience": "3+ years"}
    ]
    job_details = get_job_role_details("Tester", job_roles)
    print(f"Job Details for Tester: {job_details}")