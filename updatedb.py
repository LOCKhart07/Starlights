import pyrebase
from collections import OrderedDict
import pickle

# Handling file
def updateDB():
    upd = open('datafile.pickle', 'wb')
    pickle.dump(od, upd)
    upd.close()

def readDB():
    rd = open('datafile.pickle', 'rb')
    temp = pickle.load(rd)
    global tempx
    tempx = temp
    rd.close()

# Initialize file
od=OrderedDict([('TimeDelay', '"0.5"'), ('autoDelay', '"15"'), ('sequenceNo', '1')])
updateDB()
readDB()
print("Initial values: ",tempx)

# Configure firebase
config = {     
  "apiKey": "AAAAgO7gceU:APA91bE5phBPPs3hHDRZTuwQXu-hbRGY8Rpm4FT-t3fku07_6zd6Qw3EHCuW75fDTNDuqQ55dUTxzOpfJjjjLZpv29eC_pfofpyNjaoL8OH2RXPFnkYIL1esHYYrt5_0mF1nGp7gb5dK",
  "authDomain": "lightsrpi.firebaseapp.com",
  "databaseURL": "https://lightsrpi-default-rtdb.firebaseio.com/",
  "storageBucket": "lightsrpi.appspot.com"
}
try:
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    print("Database Initialized")
except:
    print("Database connection failed")

# Constantly running to check for database updates
while True:
    try:
        od=db.child("kBgW").get().val()
    except:
        print("error")
    if (str(od) != str(tempx)):
        updateDB()
        readDB()
        print(tempx)