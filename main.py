from resume_parser import extract_pdf_text
from text_cleaner import clean_text
from skill_extractor import extract_skills
from job_matcher import load_job_roles, calculate_match_scores, get_top_roles
from skill_gap import find_skill_gap, generate_learning_roadmap


# --------------------------------------------------
# STEP 1: Extract resume text
# --------------------------------------------------

resume_text = extract_pdf_text("sample_resume.pdf")


# --------------------------------------------------
# STEP 2: Clean the resume text
# --------------------------------------------------

cleaned_text = clean_text(resume_text)


# --------------------------------------------------
# STEP 3: Extract skills from the resume
# --------------------------------------------------

resume_skills = extract_skills(
    cleaned_text,
    "data/skill_dictionary.csv"
)


# --------------------------------------------------
# STEP 4: Load job roles
# --------------------------------------------------

job_roles = load_job_roles(
    "data/job_roles.csv"
)


# --------------------------------------------------
# STEP 5: Calculate match scores
# --------------------------------------------------

results = calculate_match_scores(
    cleaned_text,
    job_roles
)


# --------------------------------------------------
# STEP 6: Get top 3 recommended roles
# --------------------------------------------------

top_roles = get_top_roles(results)


# --------------------------------------------------
# --------------------------------------------------
# STEP 7: Select a target role
# --------------------------------------------------

target_role = "Machine Learning Engineer"

# --------------------------------------------------
# STEP 8: Find skill gap
# --------------------------------------------------

found_skills, missing_skills = find_skill_gap(
    resume_skills,
    results,
    target_role
)


# --------------------------------------------------
# STEP 9: Generate learning roadmap
# --------------------------------------------------

learning_plan = generate_learning_roadmap(
    missing_skills,
    "data/learning_roadmap.csv"
)


# --------------------------------------------------
# DISPLAY RESULTS
# --------------------------------------------------

print("\n==============================")
print("AI RESUME ANALYZER")
print("==============================")


print("\nSkills Found in Resume:")
print(resume_skills)


print("\nJob Role Match Scores:")
print(
    results[["Job Role", "Match Score"]]
)


print("\nTop 3 Recommended Roles:")
print(
    top_roles[["Job Role", "Match Score"]]
)


print("\nSelected Target Role:")
print(target_role)


print("\nSkills Found for Target Role:")
print(found_skills)


print("\nMissing Skills:")
print(missing_skills)


print("\nLearning Roadmap:")

for item in learning_plan:
    print("-", item)