from libraries.dbhandler import DBHandler
from flask import session

# Model for posts functions
class Posts:
    
    # Creates and submits a post
    def makePost(self, request):
        db = DBHandler()
        db.connect()
        title = request.args.get('title', 0, type=str)
        text = request.args.get('text', 0, type=str)
        
        query = "INSERT INTO Posts (userid, title, text) values (%s, %s, %s);"
        db.executeUpdate(query, (session['userid'], title, text))
        db.disconnect()
        return "valid_post"
    
    # Returns all posts made by specified user
    def getUserPosts(self, userid):
        db = DBHandler()
        db.connect()
        
        query = "SELECT * FROM Posts WHERE userid = %s ORDER BY date DESC;"
        cursor = db.executeQuery(query, userid)
        tupls = cursor.fetchall()
        return tupls
    
    # Returns all posts made by all users
    def getAllPosts(self):
        db = DBHandler()
        db.connect()
        
        query = "SELECT * FROM Posts ORDER BY date DESC;"
        cursor = db.executeQuery(query, ())
        tupls = cursor.fetchall()
        return tupls