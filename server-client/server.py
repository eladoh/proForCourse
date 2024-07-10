import socket
import os
import threading


def handle_client(conn, addr, upload_or_download):
    if upload_or_download == "upload":

        filename_length = int(conn.recv(8).decode())
        filename = conn.recv(filename_length).decode()

        print(f'Received filename: {filename}')
        file_basename = os.path.basename(filename)
        file_path = os.path.join("C:\\Users\\user1\\Desktop\\proForCourse\\files", file_basename)

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
        #sock.close()
        print(f'File saved to {file_path}')
        if upload_or_download == "download":
            path = r"C:\Users\user1\Desktop\proForCourse\files"
            obj = os.scandir(path)
            print(obj)
            # list_of_files = []
            # pick_file = str(input(f"which file do you want to download? {list_of_files}"))




def main():

    host = '127.0.0.1'
    port = 8080

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen()
    print(f'Server listening on {host}:{port}...')

    while True:
        conn, addr = sock.accept()
        print(f'Connected with client {addr}')

        upload_or_download = conn.recv(1024).decode()

        if(upload_or_download == "upload"):
            print("upload")
        if upload_or_download == "download":
            print("download")

        client_thread = threading.Thread(target=handle_client, args=(conn, addr, upload_or_download))
        client_thread.start()

# # Receive the length of the filename
# filename_length = int(conn.recv(8).decode())
# # Receive the filename itself
# filename = conn.recv(filename_length).decode()

# print(f'Received filename: {filename}')
# file_basename = os.path.basename(filename)
# file_path = os.path.join("C:\\Users\\user1\\Desktop\\proForCourse\\files", file_basename)

# # Receive the length of the data
# data_length = int(conn.recv(16).decode())
# print(f'Expecting to receive {data_length} bytes')

# with open(file_path, "wb") as fo:
#     received_data = 0
#     while received_data < data_length:
#         data = conn.recv(1024)
#         if not data:
#             break
#         fo.write(data)
#         received_data += len(data)

# print(f'Received {received_data} bytes')
# conn.close()
# sock.close()
# print(f'File saved to {file_path}')

main()