from flask import Blueprint, render_template, request, redirect, flash, url_for, jsonify
from flask import session
from libraries.profile import Profile
from jinja2 import Template
from libraries.user import User
import md5

# controller for profile url prefix
profile = Blueprint("profile",__name__,template_folder='templates')

# Profile base route that handles uid parameter specification
# Also handles if no uid is specified; load with uid instead
@profile.route("/")
def load_profile():
    user = User()
    tupl = None
    if (request.args.get('uid') != None):
        tupl = user.get_user_data(request.args.get('uid'))
        if(tupl != None):
            return render_template("user_control/profile.html", email = tupl[0], signupdate = tupl[1], pic_hash = user.generate_pic_hash(str(tupl[1])))
        else:
            return redirect(url_for("main.main_view"))
    else:
        tupl = user.get_user_data(session['userid'])
        return redirect(url_for("profile.load_profile")+"?uid="+str(session['userid']))
    
# Loads update email form upon click
@profile.route("/update_email")
def update_email():
    return render_template("user_control/update_email.html")
    
# Called via jQuery to update email information, and check validity of form values
@profile.route("/update_email_check", methods = ["POST", "GET"])
def email_check():
    profile = Profile()
    update_code = profile.update_email(request)
    print(update_code)
    return jsonify(update_code)
    
# Loads update password form upon click
@profile.route("/update_password")
def update_password():
    return render_template("user_control/update_password.html")
    
# Called via jQuery to update password information, and check validity of form values
@profile.route("/update_password_check", methods = ["POST", "GET"])
def password_check():
    profile = Profile()
    update_code = profile.update_password(request)
    print(update_code)
    return jsonify(update_code)

# Deletes the user from the database
@profile.route("/delete_user", methods = ["POST", "GET"])
def delete_user():
    profile = Profile()
    userid = request.args.get("uid", 0, type=str)
    print(userid)
    tupls = profile.delete_user(userid)
    return redirect(url_for("login.logout"))