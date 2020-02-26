import os

import Database as db
import Server as s

INTEGER   = db.INTEGER
REAL      = db.REAL
TEXT      = db.TEXT
TIMESTAMP = db.TIMESTAMP





class Vispo():

    # Attributes
    # dictTemplate = ''
    # database = None
    # server   = None

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


    def __checkTemplate(self, dictionary):
        print("Vispo: check template")

        for key, value in dictionary.items():
            if not (value in (INTEGER, REAL, TEXT, TIMESTAMP)):
                return False
            
        return True


    def __checkRecord(self, dictionary):
        print("Vispo: check record")

        for key, value in dictionary.items():
            if not ( key in self.dictTemplate.keys() ):
                return False

        return True




    def addRecord(self, record):
        print("Vispo: adding object to DB")
        if self.__checkRecord( record ):
            self.database.addRecord( record )
        
        return 0


    def getLastRecord(self):
        print("Vispo: get last record")
        res = self.database.getLastRecord()
        return res


    def getAllRecords(self):
        print("Vispo: get last record")
        res = self.database.getAllRecords()
        return res


    def getRecords(self, start, end):
        print("Vispo: get Records from %s and %s", start, end)
        res = self.database.getRecords(start, end)
        return res




