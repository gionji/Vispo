import Vispo as vp
import datetime

a = {"nome" : vp.TEXT ,
        "cognome" : vp.TEXT,
        "eta" : vp.REAL }

leee = vp.Vispo('cane', a)


b = {"nome" : 'rex',
     "cognome" : 'hunde',
     "eta" : 23.0 }


leee.addRecord(b)


allData = leee.getAllRecords()


start = datetime.datetime(2020, 2, 26, 16, 40, 4, 993087)
end = datetime.datetime(2020, 2, 26, 16, 50, 4, 993087)

someData = leee.getRecords('2020-02-26 16:40:50','2020-02-26 16:50:50')

for r in someData:
    print( dict(r) )



someData = leee.getRecords(start, end)

for r in someData:
    print( dict(r) )


