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
# Output: Hello friemds. Cheems here

# URL: http://localhost:5000/printNum/99
# Output: Number is 99

# URL: http://localhost:5000/printNum/nine
# Output: ERROR

# URL: http://localhost:5000/printFloat/369.963
# Output: Floating Number is 369.963

# URL: http://localhost:5000/printFloat/threepointnine
# Output: ERROR