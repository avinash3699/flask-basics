from flask import Flask

app = Flask(__name__)

# @app.route("/hello")
def hello_world():
    return "Hello World using add_url_rule"

app.add_url_rule("/hello", "hello", hello_world)

if __name__ == "__main__":
    app.run()

# URL: http://localhost:5000/hello
# Output: https://github.com/avinash3699/flask-basics/blob/main/02.add_url_rule/output.jpg
