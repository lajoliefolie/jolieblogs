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
        # print("AM I BEING CALLED TWICE????")
        if(isadmin):
            query = "DELETE FROM Permissions WHERE userid = %s and permission = 'admin';"
        else:
            query = "INSERT INTO Permissions (userid, permission) VALUES (%s, 'admin');"
        
        # print(query)
        db.executeUpdate(query, (str(userid)))
        db.disconnect()
        return True
        
    # Deletes users from the database; used by admin
    @classmethod
    def delete_user(self, userid):
        db = DBHandler()
        db.connect()
        # print("AM I (DELETE) BEING CALLED TWICE????")
        query = "DELETE FROM Users WHERE userid = %s;"
        db.executeUpdate(query, (userid))
        # print(query)
        db.disconnect()
        if(str(userid) == str(session['userid'])):
            return "deleted_logout"
        return "deleted"