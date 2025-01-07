import socket
import threading
import pyperclip

host = "localhost"
port = 8080

def main():
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    send_requests_thread = threading.Thread(target=send_requests,args=(client_socket, ))
    send_requests_thread.start()


def send_requests(client_socket):
    print("request action: 1. screenshot 2. paste")
    request = int(input())

    if(request == 1): # screenshot
        bytes = request.to_bytes(16, byteorder="big")
        print("screenshot was chosen")
        client_socket.sendall(bytes)
        image_len = int.from_bytes(client_socket.recv(4), byteorder="big")
        print(image_len)

        image_bytes = b""

        while image_len > len(image_bytes):
            image_bytes += client_socket.recv(image_len - len(image_bytes))

        print(image_bytes)
        with open("image.jpg", "wb") as f:
            f.write(image_bytes)
    if (request == 2): # paste
        print("enter what you want to send: ")
        bytes = request.to_bytes(16, byteorder="big")
        client_socket.sendall(bytes)
        to_send = input()

        client_socket.sendall(to_send.encode())
    if request == 3:
        print("coping")
        bytes = request.to_bytes(16, byteorder="big")
        client_socket.sendall(bytes)

        clipboard = client_socket.recv(1024).decode()
        pyperclip.copy(clipboard)        
        

main()