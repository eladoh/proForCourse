import socket
import os


host = '127.0.0.1'
port = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen()

print(f'Server listening on {host}:{port}...')

conn, addr = sock.accept()
print(f'Connected with client {addr}')

# Receive the length of the filename
filename_length = int(conn.recv(8).decode())
# Receive the filename itself
filename = conn.recv(filename_length).decode()

print(f'Received filename: {filename}')
file_basename = os.path.basename(filename)
file_path = os.path.join("C:\\Users\\user1\\Desktop\\proForCourse\\files", file_basename)

# Receive the length of the data
data_length = int(conn.recv(16).decode())
print(f'Expecting to receive {data_length} bytes')

with open(file_path, "wb") as fo:
    received_data = 0
    while received_data < data_length:
        data = conn.recv(1024)
        if not data:
            break
        fo.write(data)
        received_data += len(data)

print(f'Received {received_data} bytes')
conn.close()
sock.close()
print(f'File saved to {file_path}')
