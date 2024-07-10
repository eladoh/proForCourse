
# import socket
# import os


# def handle_client:



# def main():

#    # upload_or_download = str(input("do you want to upload or download files?:  "))

#     host = '127.0.0.1'  # Local IP
#     port = 8080  # Port
#     clients = int(input('Enter number of clients: '))

#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sock.bind((host, port)) 
#     sock.listen(clients)  

#     connection, addr = sock.accept()  

#     command_bytes = connection.recv(1024)  
#     command_received = command_bytes.decode('utf-8')
    
#     print("Received command:", command_received)
# #    connection.close()
#     #sock.close()

#     if command_received == "upload" or command_received == "Upload":
#         print("iam here")
#         target_directory = r'C:\Users\user1\Desktop\proForCourse\files'

#         connections = []  

#         for i in range(clients):
#             conn, addr = sock.accept()  
#             connections.append(conn)  
#             print('Connected with client', i + 1)

#         for conn in connections:
#             try:
#                 filename_length = int(conn.recv(8).decode()) # האורך של השם
#                 filename = conn.recv(filename_length).decode() # השם עצמו

#                 #filepath = os.path.join(target_directory, filename)
#                 file_basename = os.path.basename(filename)

#                 filepath = os.path.join(target_directory, file_basename)

#                 with open(filepath, "wb") as fo: 
#                     while True:
#                         data = conn.recv(1024)  
#                         if not data:
#                             break
#                         fo.write(data)

#                 print(f'Receiving file from client: {filename}')
#                 print('Received successfully! Filename is:', filename)

#             except Exception as e:
#                 print(f'Error handling client data: {e}')
#             finally:
#                 conn.close() # סוגרים את החיבור 

#         sock.close() 
#     if command_received == "download" or command_received == "Download":
#         sock.send("download")

#         path = r"C:\Users\user1\Desktop\proForCourse\files"
        
#         searched_file = str(input("which file do you want to get?"))

        

        


# if __name__ == '__main__':
#     main()






import socket
import os
import threading

def handle_client(conn, address, command):
    try:
        if command == "upload" or command == "Upload":
            print(f"Client {address} wants to upload files.")
            target_directory = r'C:\Users\user1\Desktop\proForCourse\files'

            filename_length = int(conn.recv(8).decode()) # Length of the file name
            filename = conn.recv(filename_length).decode() # The file name itself

            file_basename = os.path.basename(filename)
            filepath = os.path.join(target_directory, file_basename)

            with open(filepath, "wb") as fo:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    fo.write(data)

            print(f'Receiving file from client {address}: {filename}')
            print('Received successfully! Filename is:', filename)

        elif command == "download" or command == "Download":
            print(f"Client {address} wants to download files.")
            # Implement download logic here
            # Example: conn.sendall(b"File contents")

        else:
            print(f"Unknown command '{command}' received from client {address}")

    except Exception as e:
        print(f'Error handling client {address} data: {e}')
    finally:
        conn.close()

def main():
    host = '127.0.0.1'  # Local IP
    port = 8080  # Port

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port)) 
    sock.listen()  

    print(f'Server listening on {host}:{port}...')

    while True:
        conn, addr = sock.accept()  
        print(f'Connected with client {addr}')

        command_bytes = conn.recv(1024)  
        command_received = command_bytes.decode('utf-8')

        # Create a thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(conn, addr, command_received))
        client_thread.start()

if __name__ == '__main__':
    main()
















