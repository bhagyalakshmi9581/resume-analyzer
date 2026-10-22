"""Utilities for comparing resumes with job descriptions."""


def analyze_resume(resume_text: str, job_description: str) -> dict:
    """Compare resume words with job-description words and return a match report."""
    job_words = set(job_description.lower().split())
    resume_words = set(resume_text.lower().split())

    matched = job_words.intersection(resume_words)
    missing = sorted(job_words - resume_words)
    score = round((len(matched) / len(job_words)) * 100) if job_words else 0

    return {
        "score": score,
        "matched_skills": sorted(matched),
        "missing_skills": missing,
        "suggestions": [f"Consider adding {skill}" for skill in missing[:5]],
    }
