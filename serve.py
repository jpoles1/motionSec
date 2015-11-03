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
def getFileList(pos, stride):
    if(pos<0): pos = 0;
    filelist = os.listdir("static/caps/");
    filelist = sorted(filelist, reverse=True)[pos:pos+stride]
    filelist = [{"filename": filename, "isimg": isImg(filename), "isvid": isVid(filename)} for filename in filelist if (isImg(filename) or isVid(filename))]
    return filelist;
@app.route("/")
@app.route("/<int:pos>")
@app.route("/<int:pos>/<int:stride>")
def getGallery(pos=0, stride=20):
    return render_template("imgvid.html", groupid=0, filelist=getFileList(pos,stride), pos=pos, stride=stride);
@app.route("/ajax/<string:groupid>/<string:pos>/<string:stride>")
def getMediaGroup(groupid, pos, stride):
    return render_template("mediagroup.html", groupid=groupid, filelist=getFileList(int(pos),int(stride)), pos=int(pos), stride=int(stride));
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0');
