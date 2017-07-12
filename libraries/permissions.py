from libraries.dbhandler import DBHandler
from flask import render_template, session
import logging
from functools import wraps
    
# Model for permissions checking functions
class CheckPermissions:
    
    # Checks permissions based on required permissions as an array, and userid
    @classmethod
    def check_permissions(self, permission_reqs, userid):
        # print("GOT TO PERMISSION!!")
            
        db = DBHandler()
        db.connect()
        
        query = "SELECT userid, permission FROM Permissions WHERE userid = '{0}';".format(str(userid))
        cursor = db.executeQuery(query)
                
        match = False
        for (userid, permission) in cursor:
            if permission in permission_reqs:
                match = True
        db.disconnect()
        # print(match)
        return match