import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_job_roles(job_file):
    # Read the job role dataset
    job_roles_df = pd.read_csv(job_file)

    return job_roles_df


def calculate_match_scores(resume_text, job_roles_df):
    # Create a TF-IDF vectorizer
    vectorizer = TfidfVectorizer()

    # Create a list containing the resume and all job descriptions
    documents = [resume_text] + job_roles_df["Required Skills"].tolist()

    # Convert all text into TF-IDF numerical vectors
    tfidf_matrix = vectorizer.fit_transform(documents)

    # The first vector is the resume
    resume_vector = tfidf_matrix[0]

    # Store the match scores
    scores = []

    # Compare the resume with each job role
    for i in range(1, len(documents)):
        job_vector = tfidf_matrix[i]

        # Calculate cosine similarity
        similarity = cosine_similarity(resume_vector, job_vector)[0][0]

        # Convert similarity to percentage
        score = similarity * 100

        scores.append(score)

    # Add scores to the job-role DataFrame
    job_roles_df["Match Score"] = scores

    return job_roles_df


def get_top_roles(job_roles_df, number_of_roles=3):
    # Sort job roles from highest score to lowest score
    sorted_roles = job_roles_df.sort_values(
        by="Match Score",
        ascending=False
    )

    # Select the top roles
    top_roles = sorted_roles.head(number_of_roles)

    return top_roles