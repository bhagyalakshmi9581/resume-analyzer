from flask import Flask, render_template, request
from analyzer import analyze_resume

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        resume = request.form["resume"]
        job = request.form["job"]

        result = analyze_resume(resume, job)

    return render_template(
        "index.html",
        result=result
    )

if __name__ == "__main__":
    app.run(debug=True)
