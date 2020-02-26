import sqlite3
import datetime


INTEGER = 'integer'
REAL = 'real'
TIMESTAMP = 'timestamp'
TEXT = 'text'

class Database:
    tableName = None
    structDict = None
    dbname = None

    def __init__(self, name, tempDict):
        print('Database: init()')
        self.tableName = name
        self.dbName = self.tableName + ".sqlite" 
        self.structDict = tempDict

        self.__createTable(self.tableName, self.structDict)


    def __create_connection(self, db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)
 
        return conn





    def __createTable(self, name, dictionary):
        
        sql_query = "CREATE TABLE IF NOT EXISTS " + name + "( " 
        sql_query = sql_query + str("id integer PRIMARY KEY AUTOINCREMENT ")
        sql_query = sql_query + ", timestamp timestamp NOT NULL"                    

        for key, value in dictionary.items():
            sql_query = sql_query + ", " + str( key ) + " " +str(value) 

        sql_query = sql_query + ");"

        print("Database: creating table\nQuery: "+ str(sql_query))
        
        
        try:
            conn = self.__create_connection( self.dbName )
            c = conn.cursor()
            c.execute( sql_query )
        except Exception as e:
            print(e)



    def addRecord(self, recordDict):
        print("Database: add record")

        self.__checkRecord(recordDict)

        timestamp = (datetime.datetime.now(), )

        recordTuple = ( timestamp )

        sql = 'INSERT INTO ' + str( self.tableName ) + "("
        sql = sql + "timestamp"

        for key, value in recordDict.items():
            sql = sql + ", " + str(key)
            recordTuple = recordTuple + (value, )

        sql = sql + ") VALUES ( ? "
        
        for i in range(0, len(recordDict)):
            sql = sql + ", ?"

        sql = sql + ")"

        print("Database: Query = " + str(sql) )
        print("Database: Tupla = " + str(recordTuple) )

        try:
            conn = self.__create_connection( self.dbName )
            c = conn.cursor()
            c.execute( sql , recordTuple )
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)


        return 0


    def getLastRecord(self):
        print("Database: get Last record")
        result = None

        try:
            conn = self.__create_connection( self.dbName )

            cursor = conn.cursor()
    
            cursor.execute("SELECT * FROM " + str(self.tableName)  + " ORDER BY id DESC LIMIT 1")
            result = cursor.fetchone()

            conn.close()
        except Exception as e:
            print(e)

        return result


    def getAllRecords(self):
        print("Database: get all record")
        result = None

        try:
            conn = self.__create_connection( self.dbName )

            conn.row_factory = sqlite3.Row

            cursor = conn.cursor()

            cursor.execute("SELECT * FROM " + str(self.tableName))
            result = cursor.fetchall()

            conn.close()
        except Exception as e:
            print(e)

        return result




    def getRecords(self, start, end):
        print("Database: get records between %s and %s", str(start), str(end))
        
        result = None

        try:
            conn = self.__create_connection( self.dbName )

            conn.row_factory = sqlite3.Row

            cursor = conn.cursor()

            cursor.execute("SELECT * FROM " + str(self.tableName) + " WHERE timestamp >= ? AND timestamp  <= ?", (start, end))
            result = cursor.fetchall()

            conn.close()
        except Exception as e:
            print(e)

        return result

    

    def __checkRecord(self, dictionary):
        print("Database: check record before to add")
        #check if keywords are correct
        return True
