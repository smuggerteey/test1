import logging
from flask import Flask, render_template

# Create a single Flask app instance
app = Flask(__name__)

# Set up logging before the first request
@app.before_first_request
def setup_logging():
    logging.basicConfig(level=logging.DEBUG)

# Example route
@app.route("/")
def home():
    app.logger.debug("Serving the home page")
    return render_template("index.html")

# Other routes
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

# Run the app if this script is executed
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

