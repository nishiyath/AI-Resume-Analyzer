import pandas as pd


def find_skill_gap(resume_skills, job_roles_df, target_role):
    # Find the selected job role
    role = job_roles_df[
        job_roles_df["Job Role"] == target_role
    ]

    # Get the required skills for that role
    required_skills = role.iloc[0]["Required Skills"].split(",")

    # Remove extra spaces
    required_skills = [skill.strip() for skill in required_skills]

    # Find skills that are present in the resume
    found_skills = []

    # Find skills that are missing from the resume
    missing_skills = []

    for skill in required_skills:

        if skill.lower() in [s.lower() for s in resume_skills]:
            found_skills.append(skill)
        else:
            missing_skills.append(skill)

    return found_skills, missing_skills


def generate_learning_roadmap(missing_skills, roadmap_file):
    # Read the learning roadmap dataset
    roadmap_df = pd.read_csv(roadmap_file)

    # Store learning suggestions
    learning_plan = []

    # Find a learning roadmap for each missing skill
    for skill in missing_skills:

        roadmap = roadmap_df[
            roadmap_df["Skill"].str.lower() == skill.lower()
        ]

        if not roadmap.empty:
            learning_plan.append(
                f"{skill}: {roadmap.iloc[0]['Learning Roadmap']}"
            )

    return learning_plan