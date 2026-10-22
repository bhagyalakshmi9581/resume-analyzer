# AI Resume Analyzer

A simple Flask application that compares a resume against a job description and provides:

- Match Score
- Skill Gap Analysis
- Improvement Suggestions

## Technologies

- Python
- Flask
- GitHub Copilot
- Git
- GitHub Actions
- Pytest

## Run

pip install -r requirements.txt

python app.py

To analyze a resume, upload a text-based PDF or a Word `.docx` file. Text is
extracted from PDF pages and Word document paragraphs and tables. You can also
paste resume text directly. Legacy `.doc` files are not supported.