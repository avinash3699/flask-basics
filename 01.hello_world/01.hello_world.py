from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!!"

if __name__ == '__main__':
    # app.run(debug = True)
    app.run()

# URL: http://localhost:5000/
# Output: https://github.com/avinash3699/flask-basics/blob/main/01.hello_world/output.jpg
