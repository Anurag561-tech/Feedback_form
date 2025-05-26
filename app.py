from flask import Flask, render_template, request, redirect, url_for, send_file
import csv
import os

app = Flask(__name__)

CSV_FILE = "feedback.csv"

# Create CSV with headers if it doesn't exist
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode="w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([
            "Name",
            "College Name",
            "Address",
            "Overall Experience",
            "Recommend Course",
            "Content Relevance",
            "Content Depth",
            "Instructor Style",
            "Instructor Responsiveness",
            "Technical Quality",
            "Technical Issues",
            "Additional Comments"
        ])

@app.route("/", methods=["GET", "POST"])
def feedback_form():
    if request.method == "POST":
        name = request.form["name"]
        college = request.form["college"]
        address = request.form["address"]
        overall_experience = request.form["overall_experience"]
        recommend_course = request.form["recommend_course"]
        content_relevance = request.form["content_relevance"]
        content_depth = request.form["content_depth"]
        instructor_style = request.form["instructor_style"]
        instructor_responsiveness = request.form["instructor_responsiveness"]
        technical_quality = request.form["technical_quality"]
        technical_issues = request.form["technical_issues"]
        additional_comments = request.form["additional_comments"]

        with open(CSV_FILE, mode="a", newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                name,
                college,
                address,
                overall_experience,
                recommend_course,
                content_relevance,
                content_depth,
                instructor_style,
                instructor_responsiveness,
                technical_quality,
                technical_issues,
                additional_comments
            ])

        return redirect(url_for("thank_you"))

    return render_template("form.html")

@app.route("/thank-you")
def thank_you():
    return render_template("Thankyou.html")

@app.route("/download-feedback")
def download_feedback():
    return send_file(CSV_FILE, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
