import socket
import threading
from PIL import ImageGrab
import io
import pyperclip



def main():
    host = "localhost"
    port = 8080

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.bind((host, port))
    sock.listen()

    while True:
        serversock, addr = sock.accept()
        print("" + str(addr[0]) + " " + str(addr[1]))

        send_bytes_thread = threading.Thread(target= send_bytes, args= (serversock,))
        send_bytes_thread.start()


def send_bytes(sock):

    request = int.from_bytes(sock.recv(1024))

    if(request == 1):
        print("sending screenshot...")
        screen = ImageGrab.grab()
        buffer = io.BytesIO() #  "temporary storage"

        screen.save(buffer, format="JPEG")
        
        screen_bytes = buffer.getvalue()

        sock.sendall(len(screen_bytes).to_bytes(4, byteorder="big"))
        sock.sendall(screen_bytes)
    if (request == 2):
        print("paste")
        for_clipboard = sock.recv(1024).decode()
        pyperclip.copy(for_clipboard)
    if request == 3:
        clipboard = pyperclip.paste()
        sock.sendall(clipboard.encode())
    
main()


