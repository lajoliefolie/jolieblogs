from libraries.dbhandler import DBHandler
from flask import session
import hashlib
from libraries.permissions import CheckPermissions

# Model for profile functions
class Profile:
    
    # Handles updating email for users
    def update_email(self, request):
        db = DBHandler()
        db.connect()
        
        email1 = request.args.get('returnEmail', 0, type=str)
        email2 = request.args.get('returnConfEmail', 0, type=str)
        pw = request.args.get('returnPassword', 0, type=str)
        query = ("SELECT password, salt FROM Users " + \
                "WHERE email = %s;")
        cursor = db.executeQuery(query, session['email'])

        tupl = cursor.fetchone()
        pw_retr = tupl[0]
        salt = tupl[1]
        pw = hashlib.sha256(pw + salt).hexdigest()
        
        query = ("SELECT email FROM Users " + \
                "WHERE email = %s;")
        cursor = db.executeQuery(query, email1)
        tupl = cursor.fetchone()

        if email1 != email2:
            db.disconnect()
            return "email_nomatch"
        elif pw != pw_retr:
            db.disconnect()
            return "password_fail"
        elif tupl != None:
            db.disconnect()
            return "email_used"
        else:
            query = "UPDATE Users SET email=%s WHERE email=%s;"
            db.executeUpdate(query, (email1, session['email']))
            session['email'] = email1
            db.disconnect()
            return "valid_update"
        
    # Handles updating password for users
    def update_password(self, request):
        db = DBHandler()
        db.connect()
        
        pw1 = request.args.get('pw1', 0, type=str)
        pw2 = request.args.get('pw2', 0, type=str)
        pwConf = request.args.get('returnPassword', 0, type=str)
        query = ("SELECT password, salt FROM Users " + \
                "WHERE email = %s")
        cursor = db.executeQuery(query, (session['email']))

        tupl = cursor.fetchone()
        pw_retr = tupl[0]
        salt = tupl[1]
        pwConf = hashlib.sha256(pwConf + salt).hexdigest()
        if pw1 != pw2:
            db.disconnect()
            return "password_nomatch"
        elif pwConf != pw_retr:
            db.disconnect()
            return "password_fail"
        else:
            query = "UPDATE Users SET password=%s WHERE email=%s;"
            db.executeUpdate(query, (hashlib.sha256(pw1 + salt).hexdigest(), session['email']))
            db.disconnect()
            return "valid_update"
            
    # Handles deleing profile for users
    def delete_user(self, userid):
        db = DBHandler()
        db.connect()
        query = "DELETE FROM Users WHERE userid = %s;"
        db.executeUpdate(query, (str(userid)))
        db.disconnect()
        if(str(userid) == str(session['userid'])):
            return "deleted_logout"
        return "deleted"