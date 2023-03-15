from flask import *
import os
app = Flask(__name__)

#every article is within the news folder in another folder, with the article numbers counting up in order of priority (so #1 is most important, #2 second place etc.)
#ok markdown we use markdown to do bold italic and bolditalic
#and then png file is the cover image - so find every png image in folder and pick first of em; png file name will be used as credit
#jpg file is the author image - same as the png process; jpg file name will be used as author name
#This is very nicely and well structured and totally not flawed and can totally be expanded as I very much care about what happens to this site after the short project is done
#also for italic and bold text and ther text styling things you can use html tags

rubriques = []

def getHeadlines():
    headlines = []
    for item in os.listdir("data/news"):
        path = ""
        if item.startswith("article"):
            for i in os.listdir("data/news/"+item):
                if i.endswith(".txt"):
                    with open("data/news/"+item+"/"+i,"r",encoding="UTF8") as file:
                        headlines.append("/news/"+item)
                        headlines.append(file.readline().strip("\n"))
    print(headlines)
    return headlines    

@app.route("/uploads/<path:path>")
def uplod(path):
    print(path,"paaath")
    return send_file("data/"+path)
    
    
@app.route("/") #homepage with a few big news stories
def home():
    headlines = getHeadlines()
    links = [] #links to cover images
    for i in range(int(len(headlines)/2)):
        for file in os.listdir("data"+headlines[i*2]):
            if file.endswith(".png"):
                links.append("/uploads"+headlines[i*2]+"/"+file)
    bp = []
    with open("data/bulletin.txt","r",encoding="UTF8") as file:
        bp = [line for line in file.readlines()]    
    return render_template("default.html",headlines=getHeadlines(),links = links, bulletins = bp)
    
@app.route("/about") #about section
def about():
    return render_template("about.html",headlines=getHeadlines())
    
@app.route("/news") #list of all the news stories
def news():
    headlines = getHeadlines()
    links = [] #links to cover images
    for i in range(int(len(headlines)/2)):
        for file in os.listdir("data"+headlines[i*2]):
            if file.endswith(".png"):
                links.append("/uploads"+headlines[i*2]+"/"+file)
    return render_template("uudised.html",headlines=headlines,links = links)
    
@app.route("/news/<path:filename>") #generates the page for a news story on the spot
def article(filename):
    #something like the delfi article website, except without the date and actually most of the stuff
    #plink - picture link; psrc - picture source (aka file name of pic); authorp - author pic link; author - author name (name of authorp file)
    plink = ""
    psrc=""
    authorp=""
    author=""
    title=""
    text=""
    
    for i in os.listdir("data/news/"+filename+"/"):
        if i.endswith(".png"):
            plink = "/uploads/news/"+filename+"/"+i
            psrc = i.replace(".png","")
        elif i.endswith(".jpg"):
            authorp = "/uploads/news/"+filename+"/"+i
            author = i.replace(".jpg","")
        elif i.endswith(".txt"):
            with open("data/news/"+filename+"/"+i,"r",encoding="UTF8") as file:
                lines = file.readlines()
                title = lines.pop(0)
                text = "<br><br>".join(lines)
                print(text)
    return render_template("article.html",headlines=getHeadlines(),plink=plink,psrc=psrc,authorp=authorp,author=author,title=title,text=text)

@app.route("/bulletin") #bulletin board with ads, announcements etc
def bulletin():
    return render_template("bulletin.html",headlines=getHeadlines())
    
@app.route("/puzzles") #puzzles for children or something idk
def puzzles():
    dailyPuzzle = "/uploads/puzzles/"+os.listdir("data/puzzles")[0]
    return render_template("puzzles.html",headlines=getHeadlines(), puzzle=dailyPuzzle)

if __name__ == "__main__":
    app.run()