from flask import *
import os
app = Flask(__name__)

#every article is within the news folder in another folder, with the article numbers counting up in order of priority (so #1 is most important, #2 second place etc.)
#ok markdown we use markdown to do bold italic and bolditalic
#and then png file is the cover image - so find every png image in folder and pick first of em
#jpg file is the author image - same as the png process
#This is very nicely and well structured and totally not flawed and can totally be expanded as I very much care about what happens to this site after the short project is done
def getHeadlines():
    headlines = []
    for item in os.listdir("data/news"):
        path = ""
        if item.startswith("article"):
            for i in "data/news/"+item:
                if i.endswith(".txt"):
                    with open(i,"w") as file:
                        headlines.append(file.readline())
    return headlines
@app.route("/") #homepage with a few big news stories
def home():
    return render_template("default.html",headlines=getHeadlines())

@app.route("/uudised") #list of all the news stories
def news():
    return render_template("uudised.html",headlines=getHeadlines())
    
@app.route("/uudised/") #generates the page for a news story on the spot
def article():
    #something like the delfi article website, except without the date and actually most of the stuff
    return render_template("article.html",headlines=getHeadlines())

if __name__ == "__main__":
    app.run()