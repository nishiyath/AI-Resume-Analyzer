from resume_parser import extract_pdf_text
from text_cleaner import clean_text
from skill_extractor import extract_skills
from job_matcher import load_job_roles
from skill_gap import find_skill_gap, generate_learning_roadmap


# Step 1: Extract resume text
resume_text = extract_pdf_text(
    "sample_resumes/sample_resume.pdf"
)

# Step 2: Clean the resume text
cleaned_text = clean_text(resume_text)

# Step 3: Extract skills from the resume
resume_skills = extract_skills(
    cleaned_text,
    "data/skill_dictionary.csv"
)

# Step 4: Load job roles
job_roles = load_job_roles("data/job_roles.csv")

# Step 5: Select the target job role
target_role = "Machine Learning Engineer"

# Step 6: Find found and missing skills
found_skills, missing_skills = find_skill_gap(
    resume_skills,
    job_roles,
    target_role
)

# Step 7: Generate the learning roadmap
learning_plan = generate_learning_roadmap(
    missing_skills,
    "data/learning_roadmap.csv"
)


print("Target Job Role:")
print(target_role)

print("\nSkills Found:")
print(found_skills)

print("\nSkills Missing:")
print(missing_skills)

print("\nLearning Roadmap:")
for item in learning_plan:
    print("-", item)