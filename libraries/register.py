from libraries.dbhandler import DBHandler
from flask import session
from os import urandom
import hashlib
from libraries.permissions import CheckPermissions
from libraries.user import User

# Model for register functions
class RegisterLib:
    
    # Handles registration of user
    @classmethod
    def check(self, request):
        db = DBHandler()
        db.connect()
        
        email = request.args.get('returnEmail', 0, type=str)
        pw1 = request.args.get('returnPassword', 0, type=str)
        pw2 = request.args.get('confirmPassword', 0, type=str)
        query = ("SELECT email, password FROM Users " + \
                "WHERE email = '%s';")
        cursor = db.executeQuery(query, (email))

        tupl = cursor.fetchone()
        if (tupl != None) and (tupl[0] == email):
            db.disconnect()
            return "email_registered"
        elif not pw1 == pw2:
            db.disconnect()
            return "pw_match"
        else:
            salt = hashlib.sha256(urandom(256)).hexdigest()
            pw = hashlib.sha256(pw1 + salt).hexdigest()
            query = "INSERT INTO Users (email, password, salt) values(%s, %s, %s);"
            db.resetUsersIncrement()
            db.executeUpdate(query, (email, pw, salt))
            query = "SELECT userid, email, signup_date FROM Users WHERE email = '%s';"
            cursor = db.executeQuery(query, (email))
            tupl = cursor.fetchone()
            
            userid = tupl[0]
            email = tupl[1]
            signupdate = tupl[2]
            
            perms = CheckPermissions()
            isadmin = perms.check_permissions("admin", userid)
            
            user = User()
            user.create_user(userid, email, isadmin, signupdate)
            session['userid'] = user.get_userid()
            session['email'] = user.get_email()
            session['signupdate'] = user.get_signupdate()
            
            return "valid_register"