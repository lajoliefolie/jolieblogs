import mysql.connector
import os

# Model for database functions
class DBHandler():
    
    conn = None
    cursor = None
    
    # Example method to show differences in syntax needed for SELECT statements when using the non-flask MySQL
    # Needs to fill in the values based on dict values
    @classmethod
    def executeTest(self):
        query = "SELECT * FROM Users where email = %(email)s;"
        self.cursor.execute(query, ({"email":"admin@admin.com"}))
        print(self.cursor.fetchone())
    
    # Initiates a database connection for the instantiated DBHandler object on creation
    @classmethod
    # def __init__(self):
    def connect(self):
        # MySQL config
        # Please edit these values to fit your own MySQL database!
        _user = "lewiscb"
        _password = ""
        _database = "jolieblogs"
        _host = os.getenv("IP", "0.0.0.0")
        self.conn = mysql.connector.connect(user = _user, password = _password, host = _host, database = _database)
        self.cursor = self.conn.cursor()
    
    # Executes queries for data needs
    # Returns the query result
    @classmethod
    def executeQuery(self, query, args):
        # self.cursor = self.conn.cursor(dictionary=True)
        self.cursor.execute(query, args)
        return self.cursor
    
    # Handles alters, inserts, etc.
    @classmethod
    def executeUpdate(self, query, args):
        self.cursor.execute(query, args)
        self.conn.commit()
        
    # Resets user increment to keep userid values low
    @classmethod
    def resetUsersIncrement(self):
        self.cursor.execute("ALTER TABLE Users AUTO_INCREMENT = 1;")
        self.conn.commit()
        
        
    # Disconects; used for clean up
    @classmethod
    def disconnect(self):
        self.conn.close()
        self.cursor.close()