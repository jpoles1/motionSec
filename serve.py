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
        imgextlist = ["png", "jpg"]
        if(extension in imgextlist):
            return True;
        else:
            return False;
    except:
        return False;
def isVid(filename):
    try:
        regexpr = ".+\.([a-z]{2,4})$"
        extension = re.search(regexpr, filename).group(1)
        vidextlist = ["ogg"]
        if(extension in vidextlist):
            return True;
        else:
            return False;
    except:
        return False;
@app.route("/")
@app.route("/<int:preload>")
@app.route("/<int:preload>/<int:pos>")
@app.route("/<int:preload>/<int:pos>/<int:interval>")
def getImg(preload=0, pos=0, interval=5):
    filelist = os.listdir("static/caps/");
    filelist = sorted(filelist, reverse=True)[pos:pos+interval]
    print(filelist);
    filelist = [{"filename": filename, "isimg": isImg(filename), "isvid": isVid(filename)} for filename in filelist if (isImg(filename) or isVid(filename))]
    print(filelist);
    return render_template("imgvid.html", filelist=filelist);
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0');
