from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        position = request.form["position"]
        message = request.form["message"]

        send_email(name, email, position, message)
        return "✅ Submission Sent!"
    return render_template("form.html")


def send_email(name, email, position, message):
    sender_email = "vmsumpter20@gmail.com"
    receiver_email = "vmsumpter20@gmail.com"
    password = "hssk tfxq pfrq itur"

    subject = f"New Job Interest: {name}"
    body = (
        f"Name: {name}\n"
        f"Email: {email}\n"
        f"Position: {position}\n"
        f"Message: {message}"
    )

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())


if __name__ == "__main__":
    app.run(debug=True)
