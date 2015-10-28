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
def getImg():
    filelist = os.listdir("static/caps/");
    print(filelist);
    filelist = [{"filename": filename, "isimg": isImg(filename), "isvid": isVid(filename)} for filename in filelist if (isImg(filename) or isVid(filename))]
    sorted(filelist)
    print(filelist);
    return render_template("imgvid.html", filelist=filelist);
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0');
