from flask import Blueprint, render_template, request, redirect, flash, url_for, jsonify
from flask import session
from libraries.admin import AdminPage
from libraries.permissions import CheckPermissions
from libraries.posts import Posts
from jinja2 import Template
from libraries.user import User

# controller for admin url prefix
admin = Blueprint("admin",__name__,template_folder='templates')

# Base admin route
# Checks permissions of the user, and if admin permissions are not found, denies access
@admin.route("/")
def admin_check():
    perms = CheckPermissions()
    user = User()
    user = user.get_user_data(session['userid'])
    if(perms.check_permissions(["admin"], session["userid"])):
        return render_template("user_control/admin_panel.html")
    else:
        return render_template("denied.html")

# Loading user data for admin controls
@admin.route("/load_user_data", methods=["GET", "POST"])
def load_user_data():
    admin = AdminPage()
    tupls = admin.retrieve_user_data()
    return jsonify(tupls)

# Updates admin privileges of selected user
@admin.route("/update_admin", methods=["GET", "POST"])
def update_admin():
    admin = AdminPage()
    userid = request.args.get('userid', 0, type=str)
    isadmin = request.args.get('isadmin', 0, type=str)
    tupls = admin.update_admin(userid, isadmin)
    return jsonify(tupls)

# Deletes the selected user, and all their posts
# Post deleting happens with a MySQL trigger
@admin.route("/delete_user", methods=["GET", "POST"])
def delete_user():
    admin = AdminPage()
    userid = request.args.get('userid', 0, type=str)
    tupls = admin.delete_user(userid)
    return jsonify(tupls)