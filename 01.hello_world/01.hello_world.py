from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!!"

if __name__ == '__main__':
    # app.run(debug = True)
    app.run()

# URL: http://localhost:5000/
# Output: Hello World!!