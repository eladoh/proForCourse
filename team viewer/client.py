import socket
from PIL import Image
import io
from random import randint
import pyautogui
import threading
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import sys
import keyboard

class RemoteControlClient(QMainWindow):
    def __init__(self, host='localhost', port=8080):
        super().__init__()
        self.setWindowTitle('Remote Control Client')
        self.setGeometry(100, 100, 1000, 600)
        
        self.label = QLabel(self)
        self.label.setGeometry(0, 0, 800, 600)
        self.pixmap = QPixmap()
        self.label.setMouseTracking(True)
        self.setMouseTracking(True)

        self.min_interval = 0.01 
        self.last_x = -1
        self.last_y = -1
        
        self.move_count = 0
        self.limit = 15
        
        self.current_width = 800
        self.current_height = 600  

        self.hotkey_state = False

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        self.client_socket.connect((host, port))



        # Start screen receiving in a separate thread
        self.receive_thread = threading.Thread(target=self.receive_screen, daemon=True)
        self.receive_thread.start()
        
        # Start keyboard event handling in a separate thread
        self.keyboard_input_thread = threading.Thread(target=self.start_keyboard_hook, daemon=True)
        self.keyboard_input_thread.start()
        
    def start_keyboard_hook(self):
        keyboard.hook(self.handle_keyboard_event)
        keyboard.wait("esc")  # Keep the thread running until 'esc' is pressed

    def receive_screen(self):
        while True:
            try:
                data_size = int.from_bytes(self.client_socket.recv(4), byteorder='big')
                screen_data = b''
                while len(screen_data) < data_size:
                    packet = self.client_socket.recv(data_size - len(screen_data))
                    if not packet:
                        break
                    screen_data += packet
                self.pixmap.loadFromData(screen_data)
                self.label.setScaledContents(True)
                self.label.resize(self.width(), self.height())
                self.label.setPixmap(self.pixmap)

            except Exception as e:
                print(f"Connection failed: {e}")
                break

    def resizeEvent(self, event):
        self.current_width = self.width()
        self.current_height = self.height()
        super().resizeEvent(event)
    def mouseMoveEvent(self, event): # event
        # x = self.mapFromGlobal(QCursor.pos()).x()
        # y = self.mapFromGlobal(QCursor.pos()).y()
        x = event.x() / self.current_width
        y = event.y() / self.current_height
        x = int(x * 1000) + 100
        y = int(y * 1000) + 50
        #text = f"Mouse coordinates: ( {x} : {y} )"
        
        if ((x != self.last_x or y != self.last_y) and (self.move_count >= self.limit)):
            self.last_x = x
            self.last_y = y
            x_bytes = x.to_bytes(4, byteorder="big")
            y_bytes = y.to_bytes(4, byteorder="big")
            #self.send_coordinates(x, y)
            message_type = 3 # 3 = mouse move event
            self.send_sockets(3, x_bytes + y_bytes)
            print(f'x: {x}, y: {y}')
            self.move_count = 0 
        else:
            self.move_count += 1
            
        # cords_thread = 
   
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.pressPos = event.pos()
            x = event.x()
            y = event.y() 
            x = int(x / self.current_width * 1000) + 280
            y = int(y / self.current_height * 1000) 
            print(f"x: {x}, y: {y}")
            #self.send_coordinates(x, y)
            message_type = 1
            x_bytes = x.to_bytes(4, byteorder='big')
            y_bytes = y.to_bytes(4, byteorder='big')
            #print(x_bytes + y_bytes)

            self.send_sockets(message_type, x_bytes + y_bytes)

    def hot_keys(self):
        hotkeys = []
        letters = 'abcdefghijklmnopqrstuvwxyz'

        for i in range(2):
            for letter in range(26):
                if i == 0:
                    hotkeys.append(f"ctrl+{letters[letter]}")
                else:
                    hotkeys.append(f"alt+{letters[letter]}")

        return hotkeys

    def handle_keyboard_event(self, event):
        hotkeys = self.hot_keys()

        if event.event_type == keyboard.KEY_DOWN:
            for hotkey in hotkeys:
                if keyboard.is_pressed(hotkey):
                    self.hotkey_state = True
                    key_pressed = hotkey
                    print(key_pressed)
                    key_pressed_bytes = key_pressed.encode('utf-8')
                    message_type = 2

                    self.send_sockets(message_type, key_pressed_bytes)
                    break
            else:
                self.hotkey_state = False

        if event.event_type == keyboard.KEY_UP and not self.hotkey_state:
            key_pressed = event.name
            key_pressed_bytes = key_pressed.encode('utf-8')
            message_type = 2
            self.send_sockets(message_type, key_pressed_bytes)
            print(key_pressed)
        
    def send_sockets(self, message_type, data): # send mouse and keyboard
        try:
            header = message_type.to_bytes(1, "big") # 1 = mouse, 2 = keyboard
            data_len = len(data).to_bytes(4, "big") 

            self.client_socket.sendall(header + data_len + data) 

        except Exception as e:
            print(f"failed to send socket {e}")
            

    # def send_coordinates(self, x, y):
    #     try:
    #         x_bytes = x.to_bytes(4, byteorder='big')
    #         y_bytes = y.to_bytes(4, byteorder='big')
    #         self.client_socket.sendall(x_bytes + y_bytes)
    #         #print(f"Sent coordinates: ({x}, {y})")
    #     except Exception as e:
    #         print(f"Failed to send coordinates: {e}")

app = QApplication(sys.argv)
client = RemoteControlClient(host='localhost', port=8080)
client.show()
sys.exit(app.exec_())
