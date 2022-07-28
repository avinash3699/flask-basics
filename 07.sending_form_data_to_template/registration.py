from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/confirm", methods = ['POST', 'GET'])
def confirmation():
    if request.method == "POST":
        form = request.form
        return render_template("print_details.htm", details = form)

if __name__ == "__main__":
    app.run(debug = True)

# Step 1: Open form.htm in the browser. The below page opens up
# Output: https://github.com/avinash3699/flask-basics/blob/main/07.sending_form_data_to_template/output1.jpg

# Step 2: Type the details and click the "Register Button"
# Output: https://github.com/avinash3699/flask-basics/blob/main/07.sending_form_data_to_template/output2.jpg

# Step 3: The entered form details will be displayed. The form is displayed thorugh the request object
# Output: https://github.com/avinash3699/flask-basics/blob/main/07.sending_form_data_to_template/output3.jpg