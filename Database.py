import sqlite3


INTEGER = 'integer'
REAL = 'real'
TIMESTAMP = 'timestamp'
TEXT = 'text'

class Database:
    tableName = None
    structDict = None

    def __init__(self, name, tempDict):
        print('Database: init()')
        self.tableName = name
        self.structDict = tempDict

        self.__createTable(self.tableName, self.structDict)



    def __createTable(self, name, dictionary):
        
        sql_query = "CREATE TABLE IF NOT EXISTS " + name + "( " 
        sql_query = sql_query + str("id integer PRIMARY KEY AUTOINCREMENT ")
                            

        for key, value in dictionary.items():
            sql_query = sql_query + ", " + str( key ) + " " +str(value) 

        sql_query = sql_query + ");"

        print("Database: creating table\nQuery: "+ str(sql_query))


    def addRecord(self, recordDict):
        print("Database: add record")
        self.__checkRecord(recordDict)

        return 0


    def getLastRecord(self):
        print("Database: get Last record")
        return 0


    def getRecord(self, start, end):
        print("Database: get records between %s and %s", str(start), str(end))
        return 0
    

    def __checkRecord(self, dictionary):
        print("Database: check record before to add")
        #check if keywords are correct
        return True
