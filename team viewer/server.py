import socket
# Work with Image
from PIL import ImageGrab
import io 
from random import randint
import pyautogui
import threading 
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QPushButton, QAction, QMessageBox, QLineEdit
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QRect, Qt
import time
from pyautogui import moveTo

def capture_screen():
    screen = ImageGrab.grab() # take a screenshot
    buffer = io.BytesIO() # save image as bytes 
    screen.save(buffer, format='JPEG') # save the screenshot to a file
    return buffer.getvalue() # return image in bytes

def handle_client(server_sock):
    while True:
        try:
            screen_data = capture_screen()
            server_sock.sendall(len(screen_data).to_bytes(4, byteorder='big'))
            server_sock.sendall(screen_data)

            cords = server_sock.recv(8)
            if not cords:
                break

            x = int.from_bytes(cords[:4])
            y = int.from_bytes(cords[4:])

            moveTo(x,y)
            print(f"x = {x} , y = {y}")

        except Exception as e:
            print(f"connection lost: {e}")
            break

def main():
    host = '0.0.0.0'
    port = 8080

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen()
    print(f'Server listening on {host}:{port}...')
    while True:
        server_sock, addr = sock.accept()
        print(f'Connected with client {addr}')

        client_thread = threading.Thread(target=handle_client, args=(server_sock,))
        client_thread.start()

main()