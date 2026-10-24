from resume_parser import extract_pdf_text
from text_cleaner import clean_text
from job_matcher import load_job_roles, calculate_match_scores, get_top_roles


# Extract resume text
resume_text = extract_pdf_text(
    "sample_resumes/sample_resume.pdf"
)

# Clean the resume text
cleaned_text = clean_text(resume_text)

# Load job roles
job_roles = load_job_roles("data/job_roles.csv")

# Calculate match scores
results = calculate_match_scores(cleaned_text, job_roles)

print("Job Role Match Scores:")
print(results[["Job Role", "Match Score"]])


# Get the top 3 recommended job roles
top_roles = get_top_roles(results)

print("\nTop 3 Recommended Job Roles:")
print(top_roles[["Job Role", "Match Score"]])