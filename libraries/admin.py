from libraries.dbhandler import DBHandler
from flask import session

# Model for admin functions
class AdminPage():
    
    # Selects user information
    @classmethod
    def retrieve_user_data(self):
        db = DBHandler()
        db.connect()
        query = "SELECT userid, email, signup_date, permissions FROM GetPermissions"
        cursor = db.executeQuery(query)
        tupls = cursor.fetchall()
        # print(tupls)
        # print(tupls[0])
        # print(tupls[1])
        return tupls
        
    # Updates administrator privileges
    @classmethod
    def update_admin(self, userid, isadmin):
        db = DBHandler()
        db.connect()
        query = "";
        isadmin = isadmin=="admin"
        if(isadmin):
            query = "DELETE FROM Permissions WHERE userid = {0} and permission = 'admin';".format(str(userid))
        else:
            query = "INSERT INTO Permissions (userid, permission) VALUES ({0}, 'admin');".format(str(userid))
        
        # print(query)
        db.executeUpdate(query)
        db.disconnect()
        return True
        
    # Deletes users from the database; used by admin
    @classmethod
    def delete_user(self, userid):
        db = DBHandler()
        db.connect()
        query = "DELETE FROM Users WHERE userid = {0};".format(str(userid))
        db.executeUpdate(query)
        print(query)
        db.disconnect()
        if(str(userid) == str(session['userid'])):
            return "deleted_logout"
        return "deleted"