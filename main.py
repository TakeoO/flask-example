import json

from flask import Flask, render_template, request

app = Flask(__name__, template_folder="views")


@app.route("/")
def index():
    users = [
        {
            "id": 1,
            "name": "vid"
        },
        {
            "id": 2,
            "name": "david"
        },
    ]
    return render_template("index.html", users=users, appName="Smartninja")


@app.route("/contact", methods=["POST"])
def contact():
    email = request.form.get('email')
    message = request.form.get('message')
    # send email to "info@mizarstvo.si"
    # send email to "email" -> that we received their contact
    return json.dumps({
        "email": email,
        "message": message,
    })


if __name__ == '__main__':
    app.run(use_reloader=True)
