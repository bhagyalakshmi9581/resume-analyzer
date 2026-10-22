from analyzer import analyze_resume
from app import app


def test_analyze_resume_reports_missing_skills():
    result = analyze_resume("Python Flask", "Python Flask SQL")

    assert result["score"] == 67
    assert result["matched_skills"] == ["flask", "python"]
    assert result["missing_skills"] == ["sql"]
    assert result["suggestions"] == ["Consider adding sql"]


def test_analyze_resume_handles_empty_job_description():
    result = analyze_resume("Python Flask", "")

    assert result == {
        "score": 0,
        "matched_skills": [],
        "missing_skills": [],
        "suggestions": [],
    }


def test_results_page_displays_missing_skill_count_and_list():
    response = app.test_client().post(
        "/",
        data={"resume": "Python", "job": "Python Flask"},
    )

    assert response.status_code == 200
    assert b"Missing Skills" in response.data
    assert b"(1)" in response.data
    assert b"<li>flask</li>" in response.data


def test_results_page_displays_message_when_no_skills_are_missing():
    response = app.test_client().post(
        "/",
        data={"resume": "Python Flask", "job": "Python Flask"},
    )

    assert b"No missing skills identified." in response.data