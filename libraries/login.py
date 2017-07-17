from libraries.dbhandler import DBHandler
from flask import session
import hashlib
from libraries.permissions import CheckPermissions
from libraries.user import User
from json import JSONEncoder
import time

# Model for login functions
class LoginLib:
    
    # Login function used with jQuery implementation
    @classmethod
    def login_js(self, request):
        formEmail = request.args.get('returnEmail', 0, type=str)
        formPassword = request.args.get('returnPassword', 0, type=str)
        password = ""
        
        # try:
        #     if (session['login_attempts'][0]):

        db = DBHandler()
        db.connect()
        query = ("SELECT userid, email, password, salt, signup_date FROM Users WHERE email = %s;")
        cursor = db.executeQuery(query, (formEmail))
        
        
        tupl = cursor.fetchone()
        db.disconnect()

        if not (tupl == None):
            userid = tupl[0]
            email = tupl[1]
            password = tupl[2]
            salt = tupl[3]
            signupdate = tupl[4]
            
            formPassword = hashlib.sha256(formPassword + salt).hexdigest()
            
            if (password == formPassword):
                perms = CheckPermissions()
                isadmin = perms.check_permissions("admin", userid)
                
                user = User()
                user.create_user(userid, email, isadmin, signupdate)
                session['userid'] = user.get_userid()
                session['email'] = user.get_email()
                session['signupdate'] = user.get_signupdate()
                
                return True
            else:
                time.sleep(0.4)
                return False
        return False
            
    
        # for(Userid, Email, Password) in cursor:
        #     userid = Userid
        #     password = Password
        
    
    # Deprecated pre-jQuery login function
    # @classmethod
    # def login(self, request):
    #     # print("LOGIN HIT!")
    #     db = DBHandler()
    #     db.connect()
    #     email = request.form["returnEmail"]
    #     password = request.form["returnPassword"]
    #     passwordRetrieved = ""
    #     # print(email)
    #     # print(password)
    #     query = ("SELECT email, password FROM Users " + \
    #             "WHERE email = '"+email+"' AND password = '"+password+"'")
    #     cursor = db.executeQuery(query)
    #     db.disconnect()
    
    #     for(Email, Password) in cursor:
    #         emailRetrieved = Email
    #         passwordRetrieved = Password
    #         # print("Email: {}. PW: {}".format(Email, Password))
        
    #     print("Got here")
    #     if request.method == 'POST' and \
    #     (passwordRetrieved == password):
    #         # print("POST!")
    #         # print("Email: " + email)
    #         # print("PW: " + password)
    #         session['email'] = email
    #         return True
    #     else:
    #         # print("Retour au login...")
    #         return False