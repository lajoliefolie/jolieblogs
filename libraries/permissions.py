from libraries.dbhandler import DBHandler
from flask import render_template, session
import logging
from functools import wraps
    
# Model for permissions checking functions
class CheckPermissions:
    
    # Checks permissions based on required permissions as an array, and userid
    def check_permissions(self, permission_reqs, userid):
            
        db = DBHandler()
        db.connect()
        
        query = "SELECT userid, permission FROM Permissions WHERE userid = %s;"
        cursor = db.executeQuery(query, (str(userid)))
        tupls = cursor.fetchall()
        match = False
        for (userid, permission) in tupls:
            if permission in permission_reqs:
                match = True
        db.disconnect()
        return match