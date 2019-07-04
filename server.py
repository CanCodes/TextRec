from flask import Flask , render_template,request
from main import textRecog
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)
ALLOWED_EXTENSIONS = set(["png", "jpeg", "jpg"])
UPLOAD_FOLDER = '/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowedFile(file):
    return "." in file and file.rsplit(".")[1] in ALLOWED_EXTENSIONS


@app.route("/", methods=["POST", "GET"])
def homepage():
    if request.method == "POST":
        if "img" not in request.files:
            return render_template("index.html", msg= "File not uploaded.")
        file = request.files["img"]
        if file.filename == "":
            return render_template("index.html", msg="File not uploaded.")
        if file and allowedFile(file.filename):
            text = textRecog(file)
            return render_template("index.html", msg="Success", res=text, img= '/uploads/' + secure_filename(file.filename))
    elif request.method == "GET":
        return render_template('index.html')


if __name__ == '__main__':
    app.run()
