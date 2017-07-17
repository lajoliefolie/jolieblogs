# JolieBlogs

Easy to use blog site with a front page and profile views. Built with flask with a flask-MySQL backend! Can also work with a classic MySQL backend.


## Prerequisites & Libraries

* JolieBlogs requires <a href="http://flask.pocoo.org/">Flask</a>, a useful Python web framework.

* Pip install the following: flask, flask-mysql


## Instructions

* Now that the above are installed, start flask-mysqldb with 'mysql-ctl start' from the command line.

* Either use 'phpmyadmin-ctl install' to load phpmyadmin, or use 'mysql-ctl cli' to load the MySQL command line interface.

* With the CLI, you can copy and paste the contents of the jolieblogs.sql script to run the commands; make sure the last one runs, too!

* When running the jolieblogs.sql script to set up your tables, a default user will be created with admin privileges and the following credentials:


Email: admin [at] admin [dot] com


Password: admin

This will allow you to create your own account, then sign into the default account to provide your new account with administrator privileges.

* Edit your dbhandler.py to connect to your database configuration, as well as your host and port information in app.py.

*Run app.py!

## Authors:

* Christine Lewis