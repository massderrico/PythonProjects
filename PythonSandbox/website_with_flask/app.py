from flask import Flask
a = False
app = Flask(__name__)

@app.route("/")
def home():
    return ("hello <h1>Hello<h2>Hi</h2></h1>")

@app.route("/<name>")
def userlog(name):
    return (f"hello {name}")

@app.route("/fail")
def fail():
    return ("you blocked out")

@app.route("/admin")
def admin():
    if a == False:
        return redirect(url_for("fail"))
    else:
        return ("congrats ur in")

if __name__ == "__main__":
    app.run()