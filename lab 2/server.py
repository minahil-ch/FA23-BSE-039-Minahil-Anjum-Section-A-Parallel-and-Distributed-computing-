Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import socket
... 
... server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
... server_socket.bind(('127.0.0.1', 65432))
... server_socket.listen()
... 
... print("Server is listening...")
... conn, addr = server_socket.accept()
... 
... # Receive 3-byte header
... header = conn.recv(3)
... message_length = int(header.decode())
... 
... # Receive the message according to its length
... data = conn.recv(message_length)
... 
... print("Received message:", data.decode())
... 
... conn.close()
