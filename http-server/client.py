import socket

def main():
    host = '127.0.0.1'
    port = 8080

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP socket
    sock.connect((host, port))  # Connect to the server

    upload_or_download = str(input("do you want to upload or download files?:  "))

    upload_or_download_bytes = upload_or_download.encode('utf-8')
    
    sock.sendall(upload_or_download_bytes)
    
#    sock.close()

    if upload_or_download == "upload":
        while True:
            filename = input(r'Input filename you want to send: ')
            try:
                with open(filename, "rb") as fi:
                    data = fi.read()
                    if not data:
                        print('File is empty')
                        break

                    sock.send(str(len(filename)).zfill(8).encode())
                    sock.send(filename.encode())

                    total_sent = 0
                    while total_sent < len(data):
                        sent = sock.send(data[total_sent:])
                        total_sent += sent
                        print(f'Sent {sent} bytes to server')

                print(f'File {filename} sent successfully!')

            except IOError:
                print('You entered an invalid filename! Please enter a valid name')
                continue
            break  # Exit the loop after sending one file

        sock.close()  # Close the socket connection
    if upload_or_download == "download":

        pass

if __name__ == '__main__':
    main()
