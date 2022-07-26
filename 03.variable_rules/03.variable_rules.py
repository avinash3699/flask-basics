from flask import Flask

app = Flask(__name__)

@app.route("/print/<text>")
def printText(text):
    return text

@app.route("/printNum/<int:num>")
def printNum(num):
    return f"Number is {num}"

@app.route("/printFloat/<float:num>")
def printFloat(num):
    return f"Floating Number is {num}"

if __name__ == "__main__":
    app.run()

# URL: http://localhost:5000/print/Hello%20friemds.%20Cheems%20here
# Output: https://github.com/avinash3699/flask-basics/blob/main/03.variable_rules/output1.jpg

# URL: http://localhost:5000/printNum/99
# Output: https://github.com/avinash3699/flask-basics/blob/main/03.variable_rules/output2.jpg

# URL: http://localhost:5000/printNum/nine
# Output: https://github.com/avinash3699/flask-basics/blob/main/03.variable_rules/output3.jpg

# URL: http://localhost:5000/printFloat/369.963
# Output: https://github.com/avinash3699/flask-basics/blob/main/03.variable_rules/output4.jpg

# URL: http://localhost:5000/printFloat/threepointnine
# Output: https://github.com/avinash3699/flask-basics/blob/main/03.variable_rules/output5.jpg
