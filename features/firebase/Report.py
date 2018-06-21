import firebase_admin
from firebase_admin import (
    credentials, db
)


def extractReportKey(key):
    parts = key.split('-')
    uid = parts[1]
    dateStr = "%s-%s-%s %s:%s:%s"%(parts[2],parts[3],parts[4],parts[5],parts[6],parts[7])
    return (uid,dateStr)
    
def listReports():
    ref = db.reference('/')
    i = 0
    reportList = []
    for c in ref.get():
        print(i,c)
        if c.startswith('report-'):
            print(c)
            (uid,dateStr) = extractReportKey(c)
            print('\tuid:',uid,'\n\ttime:',dateStr)
            output = (uid,dateStr)
            reportList.append(output)
        i += 1
    return reportList

def viewReport(key):
    print('Key:',key)
    ref = db.reference(key)
    (uid,dateStr) = extractReportKey(key)
    print("Report by %s on %s"%(uid,dateStr))
    
    s = ""
    for c in ref.get():
        msg = ref.child(c)
        print(msg.child('message').child('text').get())
        s += msg.child('message').child('text').get()
        s += '\n'
    return s

if __name__ == '__main__':

    cred = credentials.Certificate('../../study-room-firebase-service-account.json')
    default_app = firebase_admin.initialize_app(cred,
    {
        'databaseURL': 'https://stellar-utility-840.firebaseio.com/'
    })

    # print('Default App:',default_app.name)

    listReports()
    viewReport('report-U53199750dbac026a2bd87a094472ddf1-2018-06-21-12-02-37')