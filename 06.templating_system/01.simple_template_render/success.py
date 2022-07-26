from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def showSuccessPage():
    return render_template("success.htm")

if __name__ == "__main__":
    app.run(debug = True)

# URL: http://localhost:5000/
# Output: 