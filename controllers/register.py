from flask import Blueprint, render_template, request, redirect, flash, url_for, session, jsonify
from libraries.register import RegisterLib

# controller for register url prefix
register = Blueprint("register",__name__,template_folder='templates')

# Loads register form page
@register.route("/")
def register_view():
    return render_template("login/register.html")
    
# jQuery called method to check validity of register form values, and finish otherwise
@register.route("/check", methods = ["POST", "GET"])
def check():
    # print("Here!")
    reg = RegisterLib()
    code = reg.check(request)
    # print(code)
    return jsonify(code)
        