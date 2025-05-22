import json

# Load job roles from a JSON file (or define them here)
def load_job_roles(filename="data/job_roles.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return [
            {"title": "Developer", "skills": ["Python", "JavaScript", "Git"], "qualifications": "BS in CS", "experience": "2+ years"},
            {"title": "Tester", "skills": ["QA", "Testing", "Agile"], "qualifications": "BS in any field", "experience": "1+ years"},
            {"title": "Data Analyst", "skills": ["SQL", "Excel", "Statistics"], "qualifications": "BS in Statistics", "experience": "3+ years"}
        ]

JOB_ROLES = load_job_roles()

def start_chat():
    """Starts the chatbot interaction."""

    print("Bot: Hi, I want to apply for a job.")
    response = input("You: ")

    if "yes" in response.lower() or "sure" in response.lower():
        list_job_roles()
        return True  # Indicate that the application process has started
    else:
        print("Bot: Okay, have a nice day!")
        return False  # Indicate that the application process has not started

def list_job_roles():
    """Lists available job roles."""

    print("Bot: Great! Here are some of our open positions:")
    for i, job in enumerate(JOB_ROLES):
        print(f"{i + 1}. {job['title']} (Skills: {', '.join(job['skills'])}, Qualifications: {job['qualifications']}, Experience: {job['experience']})")

def confirm_information(parsed_data):
    """Confirms extracted information with the user."""

    if not parsed_data:
        print("Bot: I couldn't extract any information from your resume.")
        return False

    print("Bot: Okay, I've extracted the following information:")
    print(f"   Name: {parsed_data.get('name', 'Not found')}")
    print(f"   Email: {parsed_data.get('email', 'Not found')}")
    print(f"   Phone: {parsed_data.get('phone', 'Not found')}")

    response = input("Bot: Is this information correct? (yes/no): ")
    return "yes" in response.lower()

def finalize_application():
    """Concludes the application process."""

    print("Bot: Thank you for your application! We will be in touch soon.")

if __name__ == '__main__':
    # Example Chatbot Interaction
    if start_chat():
        # Dummy parsed data for testing
        dummy_parsed_data = {"name": "Test User", "email": "test@example.com", "phone": "555-123-4567"}
        if confirm_information(dummy_parsed_data):
            finalize_application()