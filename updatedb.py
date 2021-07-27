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
  "apiKey": "",
  "authDomain": "lightsrpi.firebaseapp.com",
  "databaseURL": "",
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