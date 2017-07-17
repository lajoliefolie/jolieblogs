from flaskext.mysql import MySQL
# import MySQLdb as MySQL
import os

# Model for database functions
class DBHandler():
    
    conn = None
    cursor = None
    
    # Executes queries for data needs
    # Returns the query result
    @classmethod
    def executeQuery(self, query, args):
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
        
    # Initiates a database connection for the instantiated DBHandler object
    @classmethod
    def connect(self):
        from app import app
        mysql = MySQL(app)

        # MySQL config
        # Please edit these values to fit your own MySQL database!
        app.config['MYSQL_DATABASE_USER'] = "lewiscb"
        app.config['MYSQL_DATABASE_PASSWORD'] = ""
        app.config['MYSQL_DATABASE_DB'] = "jolieblogs"
        app.config['MYSQL_DATABASE_HOST'] = os.getenv("IP", "0.0.0.0")
        self.conn = mysql.connect()
        self.cursor = self.conn.cursor()
        
    # Disconects; used for clean up
    @classmethod
    def disconnect(self):
        self.conn.close()
        self.cursor.close()