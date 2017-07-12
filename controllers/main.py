from flask import Blueprint, render_template, session
import logging

# controller for default / url prefix
main = Blueprint("main",__name__,template_folder="templates")

# Main view that shows index.html
@main.route("/",methods=["GET"])
def main_view():
	return render_template("index.html")