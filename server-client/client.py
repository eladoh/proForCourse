import socket

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('127.0.0.1', 8080)

client_sock.connect(server_address)

print(f'Connected to server at {server_address}')

filename = input("Enter the file path of your file: ")

#upload_or_download = str(input("do you want to upload or download the file? "))

#client_sock.sendall(upload_or_download.encode('utf-8'))

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
