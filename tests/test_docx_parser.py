from resume_parser import extract_docx_text


# Extract text from the DOCX resume
resume_text = extract_docx_text(
    "sample_resumes/sample_resume.docx"
)


# Display the extracted text
print("DOCX Resume Text:")
print(resume_text)