from flask import Flask

app = Flask(__name__)

@app.route("/")
def chat():
    return "<p>Let's chat!</p>"