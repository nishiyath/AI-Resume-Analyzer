from resume_parser import extract_pdf_text


# Extract text from the PDF resume
resume_text = extract_pdf_text(
    "sample_resumes/sample_resume.pdf"
)


# Display the extracted text
print("Resume Text:")
print(resume_text)