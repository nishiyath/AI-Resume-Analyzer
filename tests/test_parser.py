from resume_parser import extract_pdf_text


resume_text = extract_pdf_text("sample_resumes/sample_resume.pdf")

print("Extracted Resume Text:")
print(resume_text)