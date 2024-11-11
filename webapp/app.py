from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    """
    Landing page
    """
    return render_template("index.html")

@app.route("/registration")
def registration():
    return render_template("registration.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/admin")
def admin():
    return render_template("admin.html")


@app.route("/artwork")
def artwork():
    return render_template("artwork.html")


@app.route("/marketplace")
def marketplace():
    return render_template("marketplace.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
