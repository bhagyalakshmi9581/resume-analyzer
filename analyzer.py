# Create a function that compares resume text with job description and returns score and missing skills

def analyze_resume(resume_text, job_description):
    job_words = set(job_description.lower().split())
    resume_words = set(resume_text.lower().split())

    matched = job_words.intersection(resume_words)

    score = 0

    if job_words:
        score = round((len(matched) / len(job_words)) * 100)

    return {
        "score": score,
        "missing_skills": list(job_words - resume_words)
    }