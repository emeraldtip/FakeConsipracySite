from flask import *

messages = {}

app = Flask(__name__)

@app.route("/")
def message():
    return render_template("default.html")

if __name__ == "__main__":
    app.run()