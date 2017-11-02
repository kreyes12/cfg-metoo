from flask import Flask, render_template, request
import requests

app = Flask("MyApp")

@app.route("/")
def homepage():
    return "Homepage"

@app.route("/mail")
def mailpage():
    return render_template("mail.html")

@app.route("/submit", methods=["POST"])
def mail():
    form_data = request.form
    email = form_data["email"]
    username = form_data["username"]
    send_simple_message(email, username)
    print email
    print form_data["email"]
    return "Thanks for signing up!"

def send_simple_message(to_address, name):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox4f289fcc77644f7bb6764d69d584b272.mailgun.org/messages",
        auth=("api", "key-922e382bf32636ba9b44413b2224653d"),
        data={"from": "Mailgun Sandbox <postmaster@sandbox4f289fcc77644f7bb6764d69d584b272.mailgun.org>",
              "to": to_address,
              "subject": "Hey" + name,
              "html": render_template("hello.html")})

app.run(debug=True)
