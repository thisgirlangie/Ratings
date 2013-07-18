from flask import Flask, render_template, redirect, request
from model import User, session
import model
app = Flask(__name__)

@app.route("/")
def index():
    user_list = session.query(User).limit(15).all()
    return render_template("user_list.html", users=user_list)

# ADD USER
@app.route("/add_user")
def display_add_user_form():
    html = render_template("add_user.html")
    return html

@app.route("/add_user_create")
def add_user_create():
    age = request.args.get("age")
    email = request.args.get("email")
    password = request.args.get("password")
    zipcode = request.args.get("zipcode")
    u = User(age=age, email=email, password=password, zipcode=zipcode)
    session.add(u)
    session.commit()
    return "Succesfully added user!"

@app.route("/view_users")
def view_users():
    user_list = session.query(User).limit(5).all() # wrong
    print user_list #wrong


if __name__ == "__main__":
    app.run(debug = True)