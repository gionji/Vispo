import os

import Database as db
import Server as s






class Vispo():

    # constants
    class DataType:
        INTEGER   = db.INTEGER 
        REAL      = db.REAL
        TEXT      = db.TEXT
        TIMESTAMP = db.TIMESTAMP 


    # Attributes
    dictTemplate = ''
    database = None
    server   = None

    def __init__(self, name, dictTemplate):
        self.name = name

        # check the dict template
        res = self.__checkTemplate(dictTemplate)

        if res:
            self.dictTemplate = dictTemplate

            # crete the db
            self.database = self.__createDatabase( self.name, self.dictTemplate )
            # create the server
        



    def __createServer(self, port):
        print("Vispo: Create Server")
        return 0

    def enableServer(self):
        print("Vispo: Enable server")
        return 0

    def disableServer(self):
        print("Vispo: Disable server")




    def __createDatabase(self, name, dictionary):
        print("Vispo: create database")
        ret = db.Database(name, dictionary)        
        return ret

    def __checkTemplate(self, dictTemplate):

        print("Vispo check template")
        return True



    def addRecord(self, record):
        print("Vispo: adding object to DB")
        return 0

    def getLastRecord(self):
        print("Vispo: get last record")
        return 0

    def getRecords(self, start, end):
        print("Vispo: get Records from %s and %s", start, end)
        return 0




