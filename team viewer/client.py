import socket
from os import getlogin
from PIL import Image
import io
from random import randint
import pyautogui
import threading
# PyQt5
import sys

from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtGui import QPixmap, QImage,QCursor
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QMouseEvent
import time


class RemoteControlClient(QMainWindow):
    def __init__(self, host='10.100.102.6', port=8080):
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
        
        self.current_width = 800
        self.current_height = 600  


        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, port))
        #self.setMouseTracking(True)


        self.receive_thread = threading.Thread(target=self.receive_screen, daemon=True)
        self.receive_thread.start()
        

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
                print(f"connection failed {e}")
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
        
        if (x != self.last_x or y != self.last_y):
            self.last_x = x
            self.last_y = y
            self.send_coordinates(x, y)
            
        # cords_thread = threading.Thread(target=self.send_coordinates,args=(x,y), daemon=True)
        # cords_thread.start()
        #self.send_coordinates(x, y)

    def send_coordinates(self, x, y):
        try:
            x_bytes = x.to_bytes(4)
            y_bytes = y.to_bytes(4)
            self.client_socket.sendall(x_bytes + y_bytes)
            #print(f"Sent coordinates: ({x}, {y})")
        except Exception as e:
            print(f"Failed to send coordinates: {e}")
    
app = QApplication(sys.argv)
client = RemoteControlClient(host='10.100.102.6', port=8080)
client.show()
sys.exit(app.exec_())
