# -*- coding: utf-8 -*-

from flask import redirect, session
from functools import wraps
from libraries.permissions import CheckPermissions



def reqRolesSendTo(destination_str, *roles):
    
    def wrapper(f):
        
        @wraps(f)
        def wrapped(*args, **kwargs):
            if not CheckPermissions().check_permissions(roles, session['userid']):
                return redirect(destination_str)
                
            return f(*args, **kwargs)
            
        return wrapped
        
    return wrapper