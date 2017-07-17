from flask import Blueprint, render_template, request, redirect, flash, url_for, jsonify
from flask import session
from libraries.login import LoginLib
from libraries.posts import Posts
from jinja2 import Template

# controller for login url prefix
login = Blueprint("login",__name__,template_folder='templates')

# Loads base login view
@login.route("/")
def login_view():
    return render_template("login/login_js.html")
	
# Login has been submitted; will it be valid or not????
@login.route("/completed_js", methods = ["GET", "POST"])
def completed_js():
    loggerin = LoginLib()
    if loggerin.login_js(request):
        return jsonify("valid_login")
    else:
        return jsonify("invalid_login")
        
# Logout function that pops session variables and redirects.
@login.route("/logout")
def logout():
    session.pop('userid', None)
    session.pop('isadmin', None)
    session.pop('email', None)
    session.pop('signupdate', None)
    return redirect(url_for('main.main_view'))