import streamlit as st

from resume_parser import extract_uploaded_resume
from text_cleaner import clean_text
from skill_extractor import extract_skills
from job_matcher import (
    load_job_roles,
    calculate_match_scores,
    get_top_roles
)
from skill_gap import (
    find_skill_gap,
    generate_learning_roadmap
)


# --------------------------------------------------
# PAGE TITLE
# --------------------------------------------------

st.title("AI Resume Analyzer")

st.write(
    "Analyze your resume against different job roles "
    "and identify your skill gaps."
)


# --------------------------------------------------
# STEP 1: UPLOAD RESUME
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload your resume",
    type=["pdf", "docx"]
)


# --------------------------------------------------
# CONTINUE ONLY IF RESUME IS UPLOADED
# --------------------------------------------------

if uploaded_file is not None:

    st.success("Resume uploaded successfully!")

    st.write("File name:", uploaded_file.name)


    # --------------------------------------------------
    # STEP 2: EXTRACT RESUME TEXT
    # --------------------------------------------------

    resume_text = extract_uploaded_resume(
        uploaded_file
    )


    # --------------------------------------------------
    # STEP 3: CLEAN RESUME TEXT
    # --------------------------------------------------

    cleaned_text = clean_text(
        resume_text
    )


    # --------------------------------------------------
    # STEP 4: EXTRACT SKILLS
    # --------------------------------------------------

    resume_skills = extract_skills(
        cleaned_text,
        "data/skill_dictionary.csv"
    )


    # --------------------------------------------------
    # SECTION 1: SKILLS FOUND
    # --------------------------------------------------

    st.header("Skills Found in Resume")

    if resume_skills:

        for skill in resume_skills:
            st.write("✓", skill)

    else:

        st.write("No skills found.")


    # --------------------------------------------------
    # STEP 5: LOAD JOB ROLES
    # --------------------------------------------------

    job_roles = load_job_roles(
        "data/job_roles.csv"
    )


    # --------------------------------------------------
    # STEP 6: CALCULATE MATCH SCORES
    # --------------------------------------------------

    results = calculate_match_scores(
        cleaned_text,
        job_roles
    )


    # --------------------------------------------------
    # ROUND MATCH SCORES
    # --------------------------------------------------

    results["Match Score"] = results[
        "Match Score"
    ].round(2)


    # --------------------------------------------------
    # SECTION 2: JOB ROLE MATCHING
    # --------------------------------------------------

    st.header("Job Role Match Scores")

    display_results = results.copy()

    display_results["Match Score"] = (
        display_results["Match Score"].map(
            lambda score: f"{score:.2f}%"
        )
    )

    st.dataframe(
        display_results[
            ["Job Role", "Match Score"]
        ],
        use_container_width=True,
        hide_index=True
    )


    # --------------------------------------------------
    # SECTION 3: MATCH SCORE CHART
    # --------------------------------------------------

    st.subheader("Match Score Comparison")

    chart_data = results.set_index(
        "Job Role"
    )[["Match Score"]]

    st.bar_chart(chart_data)


    # --------------------------------------------------
    # STEP 7: GET TOP 3 ROLES
    # --------------------------------------------------

    top_roles = get_top_roles(
        results
    )


    # --------------------------------------------------
    # SECTION 4: TOP 3 RECOMMENDED ROLES
    # --------------------------------------------------

    st.header("Top 3 Recommended Roles")

    top_roles_display = top_roles.copy()

    top_roles_display["Match Score"] = (
        top_roles_display["Match Score"].map(
            lambda score: f"{score:.2f}%"
        )
    )

    st.dataframe(
        top_roles_display[
            ["Job Role", "Match Score"]
        ],
        use_container_width=True,
        hide_index=True
    )


    # --------------------------------------------------
    # STEP 8: SELECT TARGET ROLE
    # --------------------------------------------------

    st.header("Target Job Role")

    target_role = st.selectbox(
        "Choose the role you want to analyze:",
        results["Job Role"].tolist(),
        index=None,
        placeholder="Select a job role"
    )


    # --------------------------------------------------
    # STEP 9: TARGET ROLE ANALYSIS
    # --------------------------------------------------

    if target_role is not None:

        found_skills, missing_skills = find_skill_gap(
            resume_skills,
            results,
            target_role
        )


        # --------------------------------------------------
        # SECTION 5: SKILLS FOUND
        # --------------------------------------------------

        st.subheader(
            f"Skills Found for {target_role}"
        )

        if found_skills:

            for skill in found_skills:
                st.write("✓", skill)

        else:

            st.write(
                "No required skills found."
            )


        # --------------------------------------------------
        # SECTION 6: MISSING SKILLS
        # --------------------------------------------------

        st.subheader("Missing Skills")

        if missing_skills:

            for skill in missing_skills:
                st.write("•", skill)

        else:

            st.write(
                "No missing skills found for this role."
            )


        # --------------------------------------------------
        # STEP 10: LEARNING ROADMAP
        # --------------------------------------------------

        learning_plan = generate_learning_roadmap(
            missing_skills,
            "data/learning_roadmap.csv"
        )


        # --------------------------------------------------
        # SECTION 7: LEARNING ROADMAP
        # --------------------------------------------------

        st.subheader("Learning Roadmap")

        if learning_plan:

            for item in learning_plan:
                st.write("→", item)

        else:

            st.write(
                "No learning roadmap is required "
                "for the selected role."
            )


        # --------------------------------------------------
        # STEP 11: CREATE DOWNLOADABLE REPORT
        # --------------------------------------------------

        st.header("Download Analysis Report")


        # Create report text
        report = ""

        report += "AI RESUME ANALYZER\n"
        report += "==================\n\n"

        report += "Resume File\n"
        report += "-----------\n"
        report += f"{uploaded_file.name}\n\n"


        # Skills found in resume
        report += "SKILLS FOUND IN RESUME\n"
        report += "----------------------\n"

        for skill in resume_skills:
            report += f"- {skill}\n"

        report += "\n"


        # Job role scores
        report += "JOB ROLE MATCH SCORES\n"
        report += "---------------------\n"

        for _, row in results.iterrows():

            report += (
                f"{row['Job Role']}: "
                f"{row['Match Score']:.2f}%\n"
            )

        report += "\n"


        # Top 3 roles
        report += "TOP 3 RECOMMENDED ROLES\n"
        report += "------------------------\n"

        for _, row in top_roles.iterrows():

            report += (
                f"{row['Job Role']}: "
                f"{row['Match Score']:.2f}%\n"
            )

        report += "\n"


        # Target role
        report += "TARGET JOB ROLE\n"
        report += "---------------\n"
        report += f"{target_role}\n\n"


        # Found skills
        report += "SKILLS FOUND FOR TARGET ROLE\n"
        report += "----------------------------\n"

        if found_skills:

            for skill in found_skills:
                report += f"- {skill}\n"

        else:

            report += "No required skills found.\n"

        report += "\n"


        # Missing skills
        report += "MISSING SKILLS\n"
        report += "--------------\n"

        if missing_skills:

            for skill in missing_skills:
                report += f"- {skill}\n"

        else:

            report += "No missing skills found.\n"

        report += "\n"


        # Learning roadmap
        report += "LEARNING ROADMAP\n"
        report += "----------------\n"

        if learning_plan:

            for item in learning_plan:
                report += f"- {item}\n"

        else:

            report += (
                "No learning roadmap is required "
                "for the selected role.\n"
            )


        # --------------------------------------------------
        # DOWNLOAD BUTTON
        # --------------------------------------------------

        st.download_button(
            label="Download Report",
            data=report,
            file_name="resume_analysis_report.txt",
            mime="text/plain"
        )