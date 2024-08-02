import socket
import pickle
import os

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 8080)

client_sock.connect(server_address)

print(f'Connected to server at {server_address}')

upload_or_download = str(input("do you want to upload or download the file? "))

#filename = input("Enter the file path of your file: ")


client_sock.sendall(upload_or_download.encode('utf-8'))

if upload_or_download == "upload":
    filename = input("Enter the file path of your file: ")
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

  #  list_length = int(client_sock.recv(1024).decode())

    list_of_files = client_sock.recv(4096)

    list_of_files = list_of_files.decode('utf-8')

    list_of_files = eval(list_of_files)

    print("\npick a file to download ")
    for file in list_of_files:
        print(file)

    picked_file = input("")
    while True:
        if picked_file in list_of_files:
            print("executing...")
            client_sock.send(picked_file.encode())

            break
        else:
            print("file does not exist...")
            picked_file = input("")

    storing_path = input("where do you want to store the file? ")

    filename_length = int(client_sock.recv(8).decode())
    filename = client_sock.recv(filename_length).decode()

    print(f'Received filename: {filename}')
    file_basename = os.path.basename(filename)
    file_path = os.path.join(storing_path, file_basename)
    print(file_path)

    data_length = int(client_sock.recv(16).decode())
    print(f'Expecting to receive {data_length} bytes')

    with open(file_path, "wb") as fo:
        received_data = 0
        while received_data < data_length:
            data = client_sock.recv(1024)
            if not data:
                break
            fo.write(data)
            received_data += len(data)

    # print(f'Received {received_data} bytes')
    # conn.close()
    # #sock.close()
    # print(f'File saved to {file_path}')



    #print(pickle.loads(list_of_files))


    # for i in range(list_length):
    #     file = client_sock.recv(1024).decode()
    #     print(file)



    # destination_path = str(input("where do you want to store your file?"))

    # client_sock.sendall(destination_path.encode('utf-8'))

    # print("\nthose are the files:")
    # received_data = b''
    # while True:
    #     chunk = client_sock.recv(4096)
    #     if not chunk:
    #         break
    #     received_data += chunk
    # deserialized_data = pickle.loads(received_data)
    
    # print(deserialized_data)

