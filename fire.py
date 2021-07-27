import pyrebase
import re
from collections import OrderedDict

config = {     
  "apiKey": "AAAAgO7gceU:APA91bE5phBPPs3hHDRZTuwQXu-hbRGY8Rpm4FT-t3fku07_6zd6Qw3EHCuW75fDTNDuqQ55dUTxzOpfJjjjLZpv29eC_pfofpyNjaoL8OH2RXPFnkYIL1esHYYrt5_0mF1nGp7gb5dK",
  "authDomain": "lightsrpi.firebaseapp.com",
  "databaseURL": "https://lightsrpi-default-rtdb.firebaseio.com/",
  "storageBucket": "lightsrpi.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()



od=db.child("kBgW").get().val()
print(od)

# for key, value in od.items(): 
#     print(key, value)

print(od['TimeDelay'])
print("\n\n\n")

temp=od['TimeDelay']
timeTemp = re.findall(r"[-+]?\d*\.\d+|\d+", str(temp))
print(timeTemp[0])