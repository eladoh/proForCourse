import socket 
import time

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # add my ipv4 ip, type of socket, sock_stream = tcp
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((SERVER_HOST, SERVER_PORT)) # adding ip and port

server_socket.listen(5) # how many connections can be in the queue

print(f"listning on port {SERVER_PORT} ... ")

while(True):
    clinet_socket, clinet_address = server_socket.accept()
    request = clinet_socket.recv(15000).decode() # how much data we can handle in bytes
    print(request)
    headers = request.split('\n')
    first_header_componentes = headers[0].split()


    http_methods = first_header_componentes[0]
    path = first_header_componentes[1]

    if path == '/' and http_methods == 'GET':
        fin = open(r"C:\Users\user1\Desktop\proForCourse\http-server\index.html")
        content = fin.read()
        fin.close()

        response = 'HTTP/1.1 200 OK \n\n' + content
    else:
        response = 'http/1.1 405 method not allowed\n\n'
    clinet_socket.sendall(response.encode())
    clinet_socket.close()
        

# import socket


# def server_program():
#     # get the hostname
#     host = socket.gethostname()
#     port = 5000  # initiate port no above 1024

#     server_socket = socket.socket()  # get instance
#     # look closely. The bind() function takes tuple as argument
#     server_socket.bind((host, port))  # bind host address and port together

#     # configure how many client the server can listen simultaneously
#     server_socket.listen(2)
#     conn, address = server_socket.accept()  # accept new connection
#     print("Connection from: " + str(address))
#     while True:
#         # receive data stream. it won't accept data packet greater than 1024 bytes
#         data = conn.recv(1024).decode()
#         if not data:
#             # if data is not received break
#             break
#         print("from connected user: " + str(data))
#         data = input(' -> ')
#         conn.send(data.encode())  # send data to the client

#     conn.close()  # close the connection
# def client_program():
#     host = socket.gethostname()  # as both code is running on same pc
#     port = 5000  # socket server port number

#     client_socket = socket.socket()  # instantiate
#     client_socket.connect((host, port))  # connect to the server

#     message = input(" -> ")  # take input

#     while message.lower().strip() != 'bye':
#         client_socket.send(message.encode())  # send message
#         data = client_socket.recv(1024).decode()  # receive response

#         print('Received from server: ' + data)  # show in terminal

#         message = input(" -> ")  # again take input

#     client_socket.close()  # close the connection


# if __name__ == '__main__':
#     server_program()



# import socket
# import threading
# import time

# HEADER = 64 # 64 bytes first message to the server this checks the next connection size

# PORT = 8080
# SERVER = socket.gethostbyname(socket.gethostname()) # gets your ip address
# ADDR = (SERVER,PORT)
# FORMAT = 'utf-8'
# DISCONNECT_MESSAGE = "dissconnect"

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(ADDR)


# def handle_client(conn, addr):
#     print(f"new connection: {addr} connected.")

#     connected = True
#     while connected:

#         msg_length = conn.recv(HEADER).decode(FORMAT)
#         headers = msg_length.split('\n')
#         first_header_componentes = headers[0].split()
#         if first_header_componentes == "GET":
#             print("get request")
#         elif msg_length:
#             print(f"Received message length: {msg_length}")  # Debugging line
#             msg_length = int(msg_length)
#             msg = conn.recv(msg_length).decode(FORMAT)
#             if msg == DISCONNECT_MESSAGE:
#                 connected = False

#             print(f"{addr}, {msg}")
#     conn.close()
    

# def start():
#     server.listen(5)
#     print(f"server is listeing on {SERVER}")
#     while True:
#         conn, addr = server.accept()
#         thred = threading.Thread(target=handle_client , args=(conn,addr))
#         thred.start()
#         print(f"active connection: {threading.active_count() - 1}")

# print("server is running")
# start()














