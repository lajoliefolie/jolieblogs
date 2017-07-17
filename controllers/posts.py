from flask import Blueprint, render_template, request, redirect, flash, url_for, jsonify
from flask import session
from libraries.posts import Posts
from libraries.user import User
from jinja2 import Template

# controller for posts url prefix
posts = Blueprint("posts",__name__,template_folder='templates')

# Loads the post making HTML
@posts.route("/make_post",methods=["GET"])
def make_post():
    return render_template("posts/makepost.html")
    
# Route which handles the actual posting of the blog post
@posts.route("/post_post",methods=["GET"])
def submit_post():
    title = request.args.get('title', 0, type=str)
    text = request.args.get('text', 0, type=str)
    userPost = Posts()
    userPost = userPost.makePost(request)
    return jsonify(userPost)

# Handles retrieving the posts of a particular user, according to the 'uid' parameter
# Currently used for viewing profiles
@posts.route("/get_user_posts",methods=["GET"])
def get_user_posts():
    userPosts = Posts()
    userPosts = userPosts.getUserPosts(request.args.get('uid'));
    user = User()
    postsArray = []
    for post in userPosts:
        tmp = []
        for element in post:
            tmp.append(element)
        tmp.append(user.generate_pic_hash(user.get_user_data(post[0])[1]))
        postsArray.append(tmp)
        
    return render_template("posts/userposts.html", posts=postsArray)
    
# Returns all posts
# Currently used for the main page view
@posts.route("/get_all_posts",methods=["GET"])
def get_all_posts():
    userPosts = Posts()
    userPosts = userPosts.getAllPosts()
    user = User()
    postsArray = []
    for post in userPosts:
        tmp = []
        for element in post:
            tmp.append(element)
        tmp.append(user.generate_pic_hash(user.get_user_data(post[0])[1]))
        postsArray.append(tmp)
        
    return render_template("posts/userposts.html", posts=postsArray)