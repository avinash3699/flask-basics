from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def showSuccessPage():
    return render_template("success.htm")

if __name__ == "__main__":
    app.run(debug = True)

# URL: http://localhost:5000/
# Output: https://github.com/avinash3699/flask-basics/blob/main/06.templating_system/01.simple_template_render/output.jpg
