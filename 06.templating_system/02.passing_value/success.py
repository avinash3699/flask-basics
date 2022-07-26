from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<name>/<age>")
def showSuccessPage(name, age):
    return render_template("success.htm", name = name, age = age)

if __name__ == "__main__":
    app.run(debug = True)

# URL: http://localhost:5000/Avinash/20
# Output: https://github.com/avinash3699/flask-basics/blob/main/06.templating_system/02.passing_value/output1.jpg

# URL: http://localhost:5000/Cheems/9
# Output: https://github.com/avinash3699/flask-basics/blob/main/06.templating_system/02.passing_value/output2.jpg
