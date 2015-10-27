from flask import Flask, render_template
import os
#from os import listdir, chdir, path
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
import re
app = Flask(__name__)
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
@app.route("/")
def getImg():
    imglist = os.listdir("static/caps/img/");
    imglist = [filename for filename in imglist if isImg(filename)]
    print(imglist);
    return render_template("image.html", imglist=imglist);
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0');
