from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/proglang/<int:maxCount>")
def printProgrammingLanguages(maxCount):
    programmingLanguages = ["Python", "Java", "C", "C++", "R", "JavaScript", "Dart", "C#"]
    returnString = "<h2>Programming Languages:<h2>"
    for index in range(min(len(programmingLanguages), maxCount)):
        returnString += programmingLanguages[index] + "<br>"
    return returnString

@app.route("/notproglang/<int:maxCount>")
def printNotProgrammingLanguages(maxCount):
    notProgrammingLanguages = ["HTML xD", "CSS", "AJAX", "XML"]
    returnString = "<h2>Not Programming Languages:<h2>"
    for index in range(min(len(notProgrammingLanguages), maxCount)):
        returnString += notProgrammingLanguages[index] + "<br>"
    return returnString

@app.route("/request/<req>/<int:maxCount>")
def service(req, maxCount):
    if req == "proglang":
        return redirect(url_for("printProgrammingLanguages", maxCount = maxCount))
    else:
        return redirect(url_for("printNotProgrammingLanguages", maxCount = maxCount))

if __name__ == "__main__":
    app.run(debug =  True)

# URL: http://localhost:5000/request/proglang/6 redirected to
#      http://localhost:5000/proglang/6
# Output: https://github.com/avinash3699/flask-basics/blob/main/04.url_for/output1.jpg

# URL: http://localhost:5000/request/notproglang/3 redirected to
#      http://localhost:5000/notproglang/3
# Output: https://github.com/avinash3699/flask-basics/blob/main/04.url_for/output2.jpg
