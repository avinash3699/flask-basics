from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<name>/<int:age>/<int:mark>")
def showSuccessPage(name, age, mark):
    return render_template("success.htm", data = {"Name": name, "Age": age, "Mark": mark})

if __name__ == "__main__":
    app.run(debug = True)

# URL: http://localhost:5000/Avinash/20/99
# Output: 

# URL: http://localhost:5000/Avinash/20/9
# Output: 