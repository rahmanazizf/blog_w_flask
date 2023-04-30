from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/main")
def hello():
    return render_template("main.html")

@app.route("/")
@app.route("/login")
def login():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()