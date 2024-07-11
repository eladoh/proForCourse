import socket
import os
import threading
import pickle


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

        #destination_path_ = conn.recv(1024).decode('utf-8')

        file_location_path = r"C:\Users\user1\Desktop\proForCourse\files"
        list_of_files = []
        dir = os.scandir(file_location_path)

       # print("\nthose are the files:")
        for file in dir:
            if file.is_file():
                list_of_files.append(file.name)
            #print(file.name)
        
        list_of_files = str(list_of_files)
        print(list_of_files)
        list_of_files = list_of_files.encode()

        conn.send(list_of_files)

        picked_file_path = conn.recv(1024).decode() #fr"{file_location_path}\{ conn.recv(1024).decode()}"
        print("picked file path: ", picked_file_path)
       # print(str(len(picked_file_path)))

        #picked_file_data_len = os.path.getsize(picked_file_path)

    with open(picked_file_path, "rb") as fi:
        data = fi.read()
        if not data:
            print('File is empty')
          #  client_sock.close()
            exit(1)

        # Send the length of the filename
        conn.send(str(len(picked_file_path)).zfill(8).encode())
        # Send the filename
        conn.send(picked_file_path.encode())

        # Send the length of the data
        conn.send(str(len(data)).zfill(16).encode())

        # Send the file data in chunks
        total_sent = 0
        while total_sent < len(data):
            sent = conn.send(data[total_sent:])
            if sent == 0:
                raise RuntimeError("Socket connection failed")
            total_sent += sent
            print(total_sent)


        #picked_file = str(input(f"which file do you want to download?"))

       # file_size = os.path.getsize(picked_file)
        #print(file_size)

        
       # conn.send(picked_file.encode())
        




def main():

    host = '10.100.102.11'
    port = 8080

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen()
    print(f'Server listening on {host}:{port}...')

    while True:
        conn, addr = sock.accept()
        print(f'Connected with client {addr}')

        upload_or_download = conn.recv(1024).decode()

        # if(upload_or_download == "upload"):
        #     print("upload")
        # if upload_or_download == "download":
        #     print("download")

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