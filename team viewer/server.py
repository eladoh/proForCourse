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
from pyautogui import moveTo, click
import keyboard

def capture_screen():
    screen = ImageGrab.grab() # take a screenshot
    buffer = io.BytesIO() # save image as bytes 
    screen.save(buffer, format='JPEG', quality=25) # save the screenshot to a file
    return buffer.getvalue() # return image in bytes

def send(server_sock):
    width = pyautogui.size().width.to_bytes(4, byteorder="big")
    height = pyautogui.size().height.to_bytes(4, byteorder="big")
    server_sock.sendall(width)
    server_sock.sendall(height)
    while True:
        try:
            screen_data = capture_screen()
            server_sock.sendall(len(screen_data).to_bytes(4, byteorder='big'))
            server_sock.sendall(screen_data)
        except Exception as e:
            print(f"connection lost: {e}")
            break

def receive_input(server_sock):
    while True:
        try:
            message_type = int.from_bytes(server_sock.recv(1), byteorder="big") # 1 = mouse, 2 = keyboard
            data_len = int.from_bytes(server_sock.recv(4), byteorder="big")
            data = server_sock.recv(data_len)
            
            if (not message_type) or (not data_len) or (not data):
                break

            if message_type == 1:# mouse 
                x = int.from_bytes(data[:4], byteorder="big")
                y = int.from_bytes(data[4:], byteorder="big")  
                moveTo(x,y)
                click(x,y)
                print(f"x: {x}, y:{y}")
            elif message_type == 2:# keyboard
                key_pressed = data.decode("utf-8")
                keyboard.press(key_pressed)
                keyboard.release(key_pressed)
                print(key_pressed)
            elif message_type == 3:
                x = int.from_bytes(data[:4], byteorder="big")
                y = int.from_bytes(data[4:], byteorder="big")
                print(f"x: {x}, y:{y}")
                #moveTo(x , y)
        except Exception as e:
            print(f"input reciving error: {e}")
            break
def main():
    host = 'localhost'
    port = 8080

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen()
    print(f'Server listening on {host}:{port}...')
    while True:
        server_sock, addr = sock.accept()
        print(f'Connected with client {addr}')

        client_thread = threading.Thread(target=send, args=(server_sock,))
        client_thread.start()
        receive_thread = threading.Thread(target=receive_input, args=(server_sock,)) 
        receive_thread.start()

main()