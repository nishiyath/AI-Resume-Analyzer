from resume_parser import extract_pdf_text
from text_cleaner import clean_text
from skill_extractor import extract_skills


# Step 1: Extract text from the PDF
resume_text = extract_pdf_text(
    "sample_resumes/sample_resume.pdf"
)

# Step 2: Clean the extracted text
cleaned_text = clean_text(resume_text)

# Step 3: Extract skills from the resume
found_skills = extract_skills(
    cleaned_text,
    "data/skill_dictionary.csv"
)

print("Skills Found in Resume:")
print(found_skills)