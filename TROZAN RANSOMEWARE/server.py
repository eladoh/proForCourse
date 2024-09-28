import socket
import sqlite3
from cryptography.fernet import Fernet
import secrets

# generate secret key
def generate_secret():
    secret = secrets.token_bytes(16)  # Returns a bytes object of the specified length
    print(secret)
    with open("encryption_key.txt", "wb") as file:
        file.write(secret)
    return secret
def read_current_key():
    with open(r"C:\Users\user1\Desktop\proForCourse\encryption_key.txt", "rb") as key:
        key = key.read()
        print(key)
        return key

def main():
    host = "127.0.0.1"
    secret = read_current_key()#read_current_key() generate_secret()
    
    # with open("encryption_key.txt", "w") as file:
    #     file.write(secret.hex())
    port = 8080
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen()
    
    print(f'Server listening on {host}:{port}...')

    server_sock, addr = sock.accept()
    print(f'Connected with client {addr}')

    server_sock.sendall(secret)    

main()