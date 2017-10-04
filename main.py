from flask import Flask, request, redirect, render_template
from cgi import escape


app = Flask(__name__)
app.config['DEBUG'] = True






@app.route("/", methods=[post])
def sign_up():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username = escape(username)
    password = escape(password)
    verify = escape(verify)
    email = escape(email)
    
    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    if username == "" or " " in username or len(username) < 3 or len(username) > 20:
        username_error = "Invalid Password"
    if password == "" or " " in password or len(password) < 3 or len(password) > 20:
        password_error = "Invalid Password"
    if verify == "" or very != password:
        verify_error = "Invalid Email"
    if email_error == "" and username_error == "" and verify_error == "" and password_error == "":
        return render_template("welcome.html"), username = username)
    else:
        return render_template("index.html" , username_error = username_error
                                                                , password_error = password_error
                                                                ,verify_error = verify_error
                                                                , email_error = email_error
                                                                , username = username
                                                                , email = email)


@app.route("/")
def index():
    return render_template("index.html")

app.run()











@app.route("/")