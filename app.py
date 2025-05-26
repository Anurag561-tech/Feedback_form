from flask import Flask, render_template, request, redirect, url_for, send_file
import csv
import os

app = Flask(__name__)

CSV_FILE = "feedback.csv"

# Ensure CSV exists with headers
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode="w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Email", "Feedback", "Rating", "Improvement Suggestions"])

@app.route("/", methods=["GET", "POST"])
def feedback_form():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        feedback = request.form["feedback"]
        rating = request.form["rating"]
        improvement = request.form["improvement"]

        with open(CSV_FILE, mode="a", newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([name, email, feedback, rating, improvement])

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
