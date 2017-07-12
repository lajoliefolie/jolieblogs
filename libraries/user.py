from dbhandler import DBHandler
import md5

# Initially planned to be implemented as a user object
# The get_user_data() method is still used
class User:
    
    userid = None;
    email = None;
    isadmin = None;
    signupdate = None;
    
    # Gets some user data
    @classmethod
    def get_user_data(self, userid):
        db = DBHandler()
        db.connect()
        query = "SELECT email, signup_date FROM Users where userid = {0};".format(str(userid))
        cursor = db.executeQuery(query)
        tupl = cursor.fetchone()
        return tupl
    
    # Generates hash for Jdenticon
    @classmethod
    def generate_pic_hash(self, signup_date):
        pic_hash = md5.new(str(signup_date)).hexdigest()
        # print(pic_hash)
        return pic_hash
    
    # Would-be function to set user variables on creation
    @classmethod
    def create_user(self, userid_tmp, email_tmp, isadmin_tmp, signupdate_tmp):
        self.userid = userid_tmp
        self.email = email_tmp
        self.isadmin = isadmin_tmp
        self.signupdate = signupdate_tmp
        
    # Getter methods
    @classmethod
    def get_userid(self):
        return self.userid
        
    @classmethod
    def get_email(self):
        return self.email
        
    @classmethod
    def get_isadmin(self):
        return self.isadmin
        
    @classmethod
    def get_signupdate(self):
        return self.signupdate
    
    # Setter methods
    @classmethod
    def set_userid(self, userid_tmp):
        self.userid = userid_tmp
        
    @classmethod
    def set_email(self, email_tmp):
        self.email = email_tmp
        
    @classmethod
    def set_isadmin(self, isadmin_tmp):
        self.isadmin = isadmin_tmp
        
    @classmethod
    def set_signupdate(self, signupdate_tmp):
        self.signupdate = signupdate_tmp