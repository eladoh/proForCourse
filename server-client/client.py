import socket
import pickle


client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('127.0.0.1', 8080)

client_sock.connect(server_address)

print(f'Connected to server at {server_address}')

filename = input("Enter the file path of your file: ")

upload_or_download = str(input("do you want to upload or download the file? "))

client_sock.sendall(upload_or_download.encode('utf-8'))

if upload_or_download == "upload":
    with open(filename, "rb") as fi:
        data = fi.read()
        if not data:
            print('File is empty')
            client_sock.close()
            exit(1)

        # Send the length of the filename
        client_sock.send(str(len(filename)).zfill(8).encode())
        # Send the filename
        client_sock.send(filename.encode())

        # Send the length of the data
        client_sock.send(str(len(data)).zfill(16).encode())

        # Send the file data in chunks
        total_sent = 0
        while total_sent < len(data):
            sent = client_sock.send(data[total_sent:])
            if sent == 0:
                raise RuntimeError("Socket connection broken")
            total_sent += sent

    client_sock.close()
if upload_or_download == "download":
    destination_path = str(input("where do you want to store your file?"))

    client_sock.sendall(destination_path.encode('utf-8'))

    print("\nthose are the files:")
    received_data = b''
    while True:
        chunk = client_sock.recv(4096)
        if not chunk:
            break
        received_data += chunk
    deserialized_data = pickle.loads(received_data)
    print(deserialized_data)

