from libraries.dbhandler import DBHandler
from flask import session

# Model for posts functions
class Posts:
    
    # Creates and submits a post
    @classmethod
    def makePost(self, request):
        db = DBHandler()
        db.connect()
        title = request.args.get('title', 0, type=str)
        text = request.args.get('text', 0, type=str)
        
        # query = "INSERT INTO Posts (userid, title, text) values ({0}, '{1}', '{2}');".format(session['userid'], title, text)
        query = "INSERT INTO Posts (userid, title, text) values (%s, %s, %s);"
        print(query)
        db.executeUpdate(query, (session['userid'], title, text))
        db.disconnect()
        return "valid_post"
    
    # Returns all posts made by specified user
    @classmethod
    def getUserPosts(self, userid):
        db = DBHandler()
        db.connect()
        
        query = "SELECT * FROM Posts WHERE userid = {0} ORDER BY date DESC;".format(userid)
        cursor = db.executeQuery(query)
        tupls = cursor.fetchall()
        print(tupls)
        return tupls
    
    # Returns all posts made by all users
    @classmethod
    def getAllPosts(self):
        db = DBHandler()
        db.connect()
        
        query = "SELECT * FROM Posts ORDER BY date DESC;"
        cursor = db.executeQuery(query)
        tupls = cursor.fetchall()
        # print(tupls)
        return tupls