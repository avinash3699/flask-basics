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
    
# Step 1: Open form.htm in the browser. The below page opens up
# Output: 

# Step 2: Type something in the first input area and click the 'submit - get req'
# Output: 

# Step 3: Go to previous page. Type something in the second input area and click the 'submit - post req'
# Output: 
