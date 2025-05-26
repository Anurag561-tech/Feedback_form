from flask import Flask, render_template, request, redirect, url_for, send_file
import csv
import os

app = Flask(__name__)
CSV_FILE = "feedback.csv"

# Initialize CSV with headers
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode="w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([
            "Name", "College", "Address",
            "Overall Experience", "Recommendation",
            "Content Relevance", "Content Depth",
            "Instructor Style", "Instructor Responsiveness",
            "Tech Quality", "Tech Issues", "Suggestions"
        ])

@app.route("/", methods=["GET", "POST"])
def feedback_form():
    if request.method == "POST":
        data = [
            request.form.get("name"),
            request.form.get("college"),
            request.form.get("address"),
            request.form.get("experience"),
            request.form.get("recommendation"),
            request.form.get("relevance"),
            request.form.get("depth"),
            request.form.get("style"),
            request.form.get("responsiveness"),
            request.form.get("quality"),
            request.form.get("issues"),
            request.form.get("suggestions")
        ]
        with open(CSV_FILE, mode="a", newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(data)
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
