import pymysql

# Defines the database connector class
class DBConnector:
    
    # Initializes the connection
    def __init__(self, host='localhost', database='library_db', user='root', password=''):
        self.conn = pymysql.connect(host=host, user=user, password=password, database=database)
        self.cursor = self.conn.cursor()

    # Gets the data from a query
    def get_data(self, query):
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    # Executes a query
    def execute(self, query):
         self.cursor.execute(query)
         self.conn.commit()

    # Closes the connection
    def close(self):
        self.conn.close()