import re
import PyPDF2
import spacy

# Load the English language model for spaCy
nlp = spacy.load("en_core_web_sm")  # You might want to use a larger model for better accuracy

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file."""
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page_num in range(len(reader.pages)):
                text += reader.pages[page_num].extract_text() or ""
    except Exception as e:
        print(f"Error reading PDF: {e}")
    return text

def extract_text_from_txt(txt_path):
    """Extracts text from a TXT file."""
    try:
        with open(txt_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading TXT file: {e}")
        return ""

def extract_name(text):
    """Extracts name from text."""
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    # Simple fallback (can be improved with more sophisticated regex or NLP)
    match = re.search(r"(?:[A-Z][a-z]+)\s+(?:[A-Z][a-z]+)", text)
    if match:
        return match.group(0)
    return None

def extract_email(text):
    """Extracts email address from text."""
    match = re.search(r"[\w\.-]+@[\w\.-]+", text)
    if match:
        return match.group(0)
    return None

def extract_phone_number(text):
    """Extracts phone number from text."""
    match = re.search(r"(\d{3}[-\s]?\d{3}[-\s]?\d{4})", text)
    if match:
        return match.group(0)
    return None

def extract_skills(text):
    """Extracts skills from text (very basic)."""
    # This is a placeholder; a real-world implementation would use a predefined skill list or NLP techniques
    skills = ["Python", "Java", "SQL", "JavaScript", "Communication"]
    found_skills = [skill for skill in skills if skill.lower() in text.lower()]
    return found_skills

def extract_education(text):
    """Extracts education information (very basic)."""
    # This is a placeholder; a real-world implementation needs more robust NLP
    education_keywords = ["B.S.", "M.S.", "Bachelor", "Master", "Ph.D."]
    found_education = [keyword for keyword in education_keywords if keyword.lower() in text.lower()]
    return found_education

def extract_experience(text):
    """Extracts work experience (very basic)."""
    # This is a placeholder; needs NLP or rule-based extraction for years of experience, job titles, etc.
    experience_keywords = ["years of experience", "Experience", "Job Title", "Responsibilities"]
    found_experience = [keyword for keyword in experience_keywords if keyword.lower() in text.lower()]
    return found_experience

def parse_resume(file_path):
    """Parses a resume file (PDF or TXT) and extracts information."""

    if file_path.lower().endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    elif file_path.lower().endswith(".txt"):
        text = extract_text_from_txt(file_path)
    else:
        raise ValueError("Unsupported file format. Please provide a PDF or TXT file.")

    if not text:
        return None  # Or raise an exception

    data = {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone_number(text),
        "skills": extract_skills(text),
        "education": extract_education(text),
        "experience": extract_experience(text)
    }
    return data

if __name__ == '__main__':
    #  Example usage (for testing)
    #  Create dummy files for testing
    with open("test_resume.txt", "w") as f:
        f.write("John Doe\njohn.doe@example.com\n123-456-7890\nSkills: Python, Java\nEducation: B.S. in CS\nExperience: 5 years")

    with open("test_resume.pdf", "w") as f:
        f.write("Jane Smith\njane.smith@example.com\n987 654 3210\nSkills: SQL, JavaScript\nEducation: M.S. in Data Science\nExperience: 3 years")

    resume_data_txt = parse_resume("test_resume.txt")
    resume_data_pdf = parse_resume("test_resume.pdf")

    print("Parsed TXT Resume Data:", resume_data_txt)
    print("Parsed PDF Resume Data:", resume_data_pdf)