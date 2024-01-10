import sqlite3, os


class Database:

    def __init__(self, database):
        self.dbName = str(database)
        self.conn = None
        self.__createDatabase()


    def __createDatabase(self):
        self.db_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "{}.db".format(self.dbName))
        self.__connectToDataBase()
        self.conn.executescript("""CREATE TABLE IF NOT EXISTS projects (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                    color TEXT NOT NULL,
                                    title TEXT NOT NULL ,
                                    text TEXT NOT NULL,
                                    url TEXT
                                )""")
        self.conn.executescript("""CREATE TABLE IF NOT EXISTS blogPost (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                    color TEXT NOT NULL,
                                    title TEXT NOT NULL,
                                    text TEXT NOT NULL,
                                    image BLOB NOT NULL,
                                    imagePath TEXT NOT NULL,
                                    imageText TEXT NOT NULL
                                )""")
        
        self.__disconnectToDatabase()
        
    
    def __connectToDataBase(self):
        self.conn = sqlite3.connect(self.db_path)
    
    def __disconnectToDatabase(self):
        self.conn.commit()
        self.conn.close()
    
    def insertProject(self, table, color, title, text, url = None):
        self.__connectToDataBase()
        if (self.__doesObjectExist(table, title) == False):
            self.conn.execute("INSERT INTO {} (color, title, text, url) VALUES ('{}', '{}', '{}', '{}')".format(table, color, title, text, url))
        self.__disconnectToDatabase()
    
    
    def insertBlogPost(self, table, title, text, imagePath, imageText, color = ""):
        self.__connectToDataBase()

        if (self.__doesObjectExist(table, title) == False):
            with open(imagePath, 'rb') as file:
                self.conn.execute("INSERT INTO {} (color, title, text, image, imagePath, imageText) VALUES (?, ?, ?, ?, ?, ?)".format(table), (color, title, text, file.read(), imagePath, imageText))

        self.__disconnectToDatabase()
    
    def fetchObjets(self, table):
        self.__connectToDataBase()

        if (table == "blogPost"):
            # Need to add another table for images to that when getting info, all binary data wont load into memory
            data = self.conn.cursor().execute("SELECT * FROM {} ORDER BY id DESC".format(table)).fetchall()
            for post in data:
                with open(post[5], 'wb') as file:
                    file.write(post[4])

        elif (table == "projects"):
            data = self.conn.cursor().execute("SELECT * FROM {}".format(table)).fetchall()

        self.__disconnectToDatabase()
        return data

    def __doesObjectExist(self, table, title):
        data = self.conn.cursor().execute("SELECT * FROM {}".format(table)).fetchall()
        for project in data:
            if (project[2] == title):
                return True
        return False
    
    def deleteObjets(self, table, id):
        self.__connectToDataBase()
        self.conn.execute("DELETE FROM {} WHERE id='{}'".format(table, id))
        self.__disconnectToDatabase()
    
    def deleteAllFromTable(self, table):
        self.__connectToDataBase()
        self.conn.execute("DELETE FROM {}".format(table))
    
        
