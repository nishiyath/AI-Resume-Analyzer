# AI Resume Analyzer 

# Project Overview

An NLP-based application that analyzes resumes and compares their content with predefined job roles. It identifies technical skills, recommends matching roles, highlights skill gaps, and suggests a basic learning roadmap.

# Objectives

- Extract text from PDF and DOCX resumes.
- Identify technical skills from resume content.
- Recommend the top three matching job roles.
- Identify missing skills for a selected target role.
- Generate a learning roadmap based on identified skill gaps.

# Key Features

- Resume Parsing: Extracts text from PDF and DOCX files.

- Skill Extraction: Identifies technical skills using a predefined skill dictionary.

- Job Matching: Calculates match scores between resume content and job-role requirements.

- Role Recommendations: Displays the top three matching roles.

- Skill-Gap Analysis: Identifies skills missing for a selected role.

- Learning Roadmap: Suggests learning areas based on identified skill gaps.

- Downloadable Report: Allows users to download their analysis report.

# Job Roles Covered

The system compares resumes against five predefined roles:

- Data Analyst
- Machine Learning Engineer
- AI Engineer
- NLP Engineer
- Computer Vision Engineer

# Matching Approach

The application combines three techniques:

- Keyword Matching: Uses a predefined skill dictionary to identify technical skills in the resume.

- TF-IDF: Converts resume text and job-role descriptions into numerical vectors.

- Cosine Similarity: Measures textual similarity between the resume and each job-role description to calculate match scores.

# Project Workflow

1. Upload a resume.

2. Extract and clean the text.

3. Identify technical skills.

4. Compare the resume with predefined job roles using TF-IDF and cosine similarity.

5. Display the top three role recommendations and match scores.

6. Identify missing skills for the selected target role.

7. Generate a learning roadmap and downloadable analysis report.

# Technologies Used

Python
Streamlit
Pandas
Scikit-learn
pypdf
python-docx

# Installation and Usage

1. Create a virtual environment

python -m venv resume_env

2. Activate the environment

On Windows PowerShell:

.\resume_env\Scripts\Activate.ps1

3. Install dependencies

pip install -r requirements.txt

4. Run the application

streamlit run app.py

# Testing

The project includes test cases covering:

- PDF and DOCX text extraction
- Text cleaning
- Skill extraction
- Job-role matching
- Skill-gap analysis
- Learning roadmap generation
- Handling resumes with no detected skills

Test cases are documented in tests/test_cases.csv.

# Limitations

- Skill identification depends on the predefined dictionary.
- Job recommendations depend on the available job-role descriptions and requirements.

# Conclusion

The AI Resume Analyzer & Job Recommendation System demonstrates how Python, text processing, and traditional machine-learning techniques can be combined to support career exploration.

By extracting skills, comparing resumes with job-role descriptions, identifying skill gaps, and suggesting learning paths, the project provides a practical foundation for building more advanced career-support applications.

