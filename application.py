from flask import *
import time
import traceback

messages = {}

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def message():
    return render_template("default.html",title=Title,artist=Artist,album=Album)

if __name__ == "__main__":
    app.run()