import pandas as pd


def extract_skills(resume_text, skill_file):
    # Read the skill dictionary
    skills_df = pd.read_csv(skill_file)

    # Convert resume text to lowercase
    resume_text = resume_text.lower()

    found_skills = []

    # Check each skill from the dictionary
    for skill in skills_df["Skill"]:

        # Convert the skill to lowercase for comparison
        skill_lower = skill.lower()

        # Check whether the skill exists in the resume
        if skill_lower in resume_text:
            found_skills.append(skill)

    return found_skills