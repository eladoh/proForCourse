from tkinter import *
import os 
import sys
import time
import subprocess
#import pandas
#import numpy
import requests
from bs4 import BeautifulSoup
import json
import colorama
from time import sleep


path  = os.path.normpath(r"C:/Users/user1/Desktop/corcu")

window = Tk()
window.minsize(400,400)
new_file = Label(window, text = '')
monitor = Label(window, text = '')

search_text = Label(window, text = 'enter a path to monitor')
search_text.pack()

entry = Entry()
entry.config(font=('Ink Free', 10))
entry.pack()

def submit():
    global monitor
    search = entry.get() # get the value of what you wrote
    monitor = Label(window, text = 'monitoring the path...')
    monitor.pack()
    main("ANTI VIRUS", True, search)


button = Button(window, text="start scan", width=25, command= submit)
button.place(x=100, y=300)



def get_last_modified_list(path:str) -> dict: #  turning the path from string to dict so the os.walk can run over it
    data = os.walk(path) #  אובייקט של גנרטור שכל פעם מחזיר טאפל שיש בו שלושה נתונים: הנתיב, התיקיה והקבצים שבאותו התקייה
    return_data = [] # empty list
 
    for route, folder , files in data: # רץ על הטאפל שקיבל מדאטה ולוקח את שלושת הנתונים בו ושם אותם במשתנים
        for file in files: # רץ על כל אחד מהקבצים
            file = os.path.join(route, file) # לוקח את הנתיב הנוחכי מוסיף לקצה שלו את הקובץ האחרון ושומר את זה במשתנה 
            return_data.append(str(file))
            #return_data[file] = "Modification time: " + str(os.stat(file).st_mtime) # מוסיף למילון את נתיב הקובץ ונותן לו נתונים של מתי הוא שונה 

    formatted_result = [p.replace("\\", "/") for p in return_data]
    return formatted_result 

#print(get_last_modified_list(path))

#https://virustotal.readme.io/v2.0/reference/file-scan
def check_for_virus(file_path):
    global new_file
    # new_file.pack_forget()

    post_url = "https://www.virustotal.com/api/v3/files"

    files = { "file": ("file", open(file_path, "rb")) }
    headers = {
        "accept": "application/json",
        "x-apikey": "f205ae5df052b585445febb5df5ea7c7c41bfd13bba3eaf348cf59718022327d"
    }

    response = requests.post(post_url, files=files, headers=headers)
    response_data = response.json()

    response_id = response_data["data"]["id"]

    print(response_id)

    get_url = f"https://www.virustotal.com/api/v3/analyses/{response_id}"

    end_response = requests.get(get_url, headers=headers)

    end_responsejson = end_response.json()

    stats = end_responsejson["data"]["attributes"]["stats"]
#    print(end_response.text)
    print(stats)

    stats_to_keep = list(stats.keys())[:2] # list of the stats i want to save

    filtered_stats = {key: stats[key] for key in stats_to_keep} # creating a dict with only the stats i need

    count_bad = 0
    print(filtered_stats)

    for stat in filtered_stats:
        count_bad += filtered_stats[stat]
    if(filtered_stats[stat] > 0):
        new_file = Label(window, text = 'new file has been added it contain malicious content')
        new_file.pack()
        window.after(5000, lambda: new_file.pack_forget())
        print(f"this file contain malicious content {count_bad}")
    else:
        new_file = Label(window, text = 'new file has been added it does not contain any malicious content')
        new_file.pack()
        window.after(5000, lambda: new_file.pack_forget())
        print("this file has no viruses")




#check_for_virus("C:/Users/user1/Desktop/corcu/New Text Document (4).txt")

def main(name: str, run: bool, watchdir: str):
    print("PROGRAM IS LIVE")
    print(f"Program: {name}")
    first_run = True
    current_data = get_last_modified_list(watchdir)

    def check_files():
        nonlocal first_run, current_data
        new_data = get_last_modified_list(watchdir)
        if first_run:
            current_data = new_data
            first_run = False
        if new_data != current_data:
            added_file = list(set(new_data) - set(current_data))
            current_data = new_data
            print(f"File Changed/added {added_file[0]}")
            check_for_virus(added_file[0])
        if run:
            window.after(50, check_files)  # Schedule next check

    check_files()

#main("Anti Virus", True)

mainloop()
















