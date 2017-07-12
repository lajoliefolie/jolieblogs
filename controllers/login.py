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
    # print("COMPLETED HIT")
    if loggerin.login_js(request):
        # print("logged! JSJS")
        # print(session['userid'])
        return jsonify("valid_login")
    else:
        return jsonify("invalid_login")
        
# Deprecated login completed function; this was before jQuery implementation.
# @login.route("/completed", methods = ["GET", "POST"])
# def completed():
#     loggerin = LoginLib()
#     # print("COMPLETED HIT")
#     if loggerin.login(request):
#         return redirect(url_for('main.main_view',))
#     else:
#         return redirect(url_for('login.login_view'))
        
# Logout function that pops session variables and redirects.
@login.route("/logout")
def logout():
    # print(session['userid'])
    session.pop('userid', None)
    session.pop('isadmin', None)
    session.pop('email', None)
    session.pop('signupdate', None)
    return redirect(url_for('main.main_view'))