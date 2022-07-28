from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.htm")

if __name__ == "__main__":
    app.run(debug = True)

# URL: http://localhost:5000/
# Output1(Alert Box): https://github.com/avinash3699/flask-basics/blob/main/08.static_files/output1.jpg
# Output2(Text): https://github.com/avinash3699/flask-basics/blob/main/08.static_files/output2.jpg