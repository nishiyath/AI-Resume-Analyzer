from text_cleaner import clean_text
from skill_extractor import extract_skills


# Read the test resume
with open("tests/test_no_skills.txt", "r") as file:
    resume_text = file.read()


# Clean the resume text
cleaned_text = clean_text(resume_text)


# Extract skills
found_skills = extract_skills(
    cleaned_text,
    "data/skill_dictionary.csv"
)


# Display the result
print("Skills Found:")
print(found_skills)


# Check whether no skills were found
if len(found_skills) == 0:

    print("TC09: PASS")

else:

    print("TC09: FAIL")