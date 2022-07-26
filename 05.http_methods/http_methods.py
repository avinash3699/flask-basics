from flask import Flask, redirect, request, url_for

app = Flask(__name__)

@app.route("/displayName/<name>/<reqType>")
def displayName(name, reqType):
    return f"Welcome {name} to the website. You got here through {reqType} request"

@app.route("/http_methods", methods = ["GET", "POST"])
def handleRequest():
    
    if request.method == "POST":
        name = request.form['name']
        reqType = "POST"

    else:
        name = request.args.get("name")
        reqType = "GET"

    return redirect(url_for("displayName", name = name, reqType = reqType))

if __name__ == "__main__":
    app.run(debug = True)    