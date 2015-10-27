from flask import Flask
from os import listdir
import re
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World!"
def isImg(filename):
    try:
        regexpr = ".+\.([a-z]{2,4})$"
        extension = re.search(regexpr, filename).group(1)
        imglist = ["png", "jpg"]
        if(extension in imglist):
            return True;
        else:
            return False;
    except:
        return False;
@app.route("/img")
def getImg():
    imglist = listdir("caps/img/");
    imglist = [filename for filename in imglist if isImg(filename)]
    print(imglist);
    return Flask.render_template("imglist.html", imglist=imglist);
if __name__ == "__main__":
    app.run(debug=True);
