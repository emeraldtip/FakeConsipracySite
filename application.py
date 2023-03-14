from flask import *

app = Flask(__name__)

#ok markdown we use markdown to do bold italic and bolditalic
#and then png file is the cover image
#jpg file is the author image
#This is very nicely and well structured and totally not flawed and can totally be expanded as I very much care about what happens to this site after the short project is done

@app.route("/")
def home():
    return render_template("default.html")
@app.route("/uudised")
def news():
    return render_template("uudised.html")

if __name__ == "__main__":
    app.run()