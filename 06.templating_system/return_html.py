from flask import Flask

app = Flask(__name__)

@app.route("/")
def return_html():
    return "<html> \
                <head> \
                    <title> HTML returned by python flask </title> \
                </head> \
                <body> \
                    <h1> HTML returned by Python! </h1> \
                </body> \
            </html>\
           "

if __name__ == "__main__":
    app.run(debug = True) 