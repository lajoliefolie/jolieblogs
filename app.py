from flask import Flask
import os

app = Flask(__name__)

# Importing controllers
from controllers.main import main
from controllers.login import login
from controllers.register import register
from controllers.admin import admin
from controllers.profile import profile
from controllers.posts import posts
app.register_blueprint(main, url_prefix='/')
app.register_blueprint(login, url_prefix='/login')
app.register_blueprint(register, url_prefix='/register')
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(profile, url_prefix='/profile')
app.register_blueprint(posts, url_prefix='/posts')


if __name__ == "__main__":
    # Starting with these values due to c9.io
    host = os.getenv("IP", "0.0.0.0")
    port = os.getenv("PORT", 8080)
    app.secret_key='teststring' # Oh, hush
    app.run(host, port)