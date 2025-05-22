# AI-Powered Resume Parser and Job Application Chatbot

## Overview

This project implements an intelligent chatbot system designed to streamline the job application process. [cite: 8] It leverages AI to parse resumes, extract key information, match candidate profiles with suitable job roles, and provide a user-friendly conversational experience. [cite: 8] The system aims to simulate a human-like interaction flow, making the application process more efficient for both candidates and recruiters.

## Features

* **Chatbot Interaction:**
    * A conversational chatbot guides users through the application process. [cite: 9, 10, 11]
    * The bot greets users and inquires about their interest in applying for a job. [cite: 9, 10, 11]
    * It presents a list of available job roles (e.g., Developer, Tester, Data Analyst) with details on required skills, qualifications, and experience. [cite: 9, 10, 11]
    * NLP techniques are employed to handle diverse user inputs. [cite: 12]
* **Resume Processing:**
    * Accepts resumes in both PDF and text formats. [cite: 13, 14]
    * Parses resumes to extract essential information, including:
        * Name
        * Email
        * Phone Number
        * Skills
        * Education
        * Experience [cite: 13, 14]
    * Matches the extracted resume data with the attributes of the selected job role to assess candidate suitability. [cite: 14]
* **Application Finalization:**
    * If a candidate is deemed qualified, the system presents the extracted information for confirmation. [cite: 15]
    * It asks for the user's consent to be contacted using the provided details. [cite: 15]
    * The system handles both positive and negative responses from the user. [cite: 16]
    * The conversation concludes with a friendly message upon application completion. [cite: 16]
* **System Architecture:**
    * The codebase follows a modular design to ensure maintainability. [cite: 17, 18, 19]
    * Clear separation of concerns is maintained for:
        * Resume parsing
        * Chatbot logic
        * Job-role matching [cite: 17, 18, 19]
    * APIs are provided for key functionalities (e.g., resume upload, data processing). [cite: 19]

## Technologies Used

* Python 3.9+ [cite: 25]
* NLP Libraries: \[List the specific libraries you used, e.g., spaCy, NLTK, transformers] [cite: 25]
* PDF Parsing: \[List the libraries you used, e.g., PyMuPDF, pdfplumber] [cite: 25]
* Frontend: Streamlit / Flask (or specify which one you used) [cite: 25]
* Chatbot Framework: Custom NLP pipeline (or specify if you used Rasa/Dialogflow) [cite: 25]



