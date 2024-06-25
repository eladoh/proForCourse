from tkinter import *
import os 
import sys
import time
import subprocess
import pandas
import requests
from bs4 import BeautifulSoup
import json
import colorama
from time import sleep


path  = os.path.normpath(r"C:/Users/user1/Desktop/corcu")

def get_last_modified_dict(path:str) -> dict: #  turning the path from string to dict so the os.walk can run over it
    data = os.walk(path) #  אובייקט של גנרטור שכל פעם מחזיר טאפל שיש בו שלושה נתונים: הנתיב, התיקיה והקבצים שבאותו התקייה
    return_data = dict() # empty dict
    # for item in data:
    #     print("item: " + str(item))
    # for route, folder , files in data:
    #     print("route " + str(route))
    #     print("folder "+ str(folder))
    #     print("files " + str(files))
    
    for route, folder , files in data: # רץ על הטאפל שקיבל מדאטה ולוקח את שלושת הנתונים בו ושם אותם במשתנים
        for file in files: # רץ על כל אחד מהקבצים
            file = os.path.join(route, file) # לוקח את הנתיב הנוחכי מוסיף לקצה שלו את הקובץ האחרון ושומר את זה במשתנה 
            return_data[file] = "Modification time: " + str(os.stat(file).st_mtime) # מוסיף למילון את נתיב הקובץ ונותן לו נתונים של מתי הוא שונה 
    return return_data 

#print(get_last_modified_dict(path))

colorama.init()

def type(words: str):
    for char in words:
        sleep(0.015)
        sys.stdout.write(char)
        sys.stdout.flush()
    print()

#https://virustotal.readme.io/v2.0/reference/file-scan
def check_for_virus():

    url = 'https://www.virustotal.com/vtapi/v2/file/scan'

    params = {'apikey': 'https://www.virustotal.com/vtapi/v2/file/scan/upload_url'}

    files = {'file': ('myfile.exe', open('C:/Users/user1/Desktop/corcu/secret_message.jpg', 'rb'))}

    response = requests.post(url, files=files, params=params)

    print(response.json())

    # url = "https://www.virustotal.com/vtapi/v2/file/scan/upload_url"

    # params = {'apikey':'f205ae5df052b585445febb5df5ea7c7c41bfd13bba3eaf348cf59718022327d'}

    # response = requests.get(url, params=params)

    # print(response.json())
    # upload_url_json = response.json()
    # upload_url = upload_url_json['upload_url']

    # file_to_scan= r"C:/Users/user1/Desktop/corcu/secret_message.jpg"
    # files = {'file': (file_to_scan, open(file_to_scan, 'rb'))}
    # response = requests.post(upload_url, files=files)

    # print(response.text)




check_for_virus()



def main(commend:str, watchdir:dir= path):
    print("PROGRAM IS LIVE")
    print(f"program: {commend}")
    first_run = True
    
    current_data = str(get_last_modified_dict(watchdir)) # takes current file data(filePath, modificaition time, )
    while True:
        new_data = get_last_modified_dict(watchdir) # getting new data
        if first_run:
            current_data = new_data
            first_run = False
        if new_data != current_data and not first_run : # אם המידע השתנה אז צריך להחליף את המידע הישן בחדש
            added_file = set(new_data) - set(current_data) # בודק מה הקובץ החדש
            current_data = new_data
            print(f"File Changed/added {added_file}") 
            check_for_virus(added_file)
            




        time.sleep(0.05) 

#main("Anti Virus")
























# route = Tk()

# route.minsize(400,400)

# m = Label(route, text="ANTI VIRUS")
# m.pack()
# button = Button(route, text="Folder To Start Checking from", width=25, command= route.destroy)
# button.place(x=100, y=300)

# m.mainloop()
