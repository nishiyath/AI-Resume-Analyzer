
from resume_parser import extract_pdf_text
from text_cleaner import clean_text


# Extract text from the resume
resume_text = extract_pdf_text("sample_resumes/sample_resume.pdf")

# Clean the extracted text
cleaned_text = clean_text(resume_text)

print("Cleaned Resume Text:")
print(cleaned_text)