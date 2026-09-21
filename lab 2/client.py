import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 65432))

message = "Hello Server, this is a long message."

# Create 3-byte header
header = str(len(message)).zfill(3)

# Send header followed by message
client_socket.send(header.encode())
client_socket.send(message.encode())

client_socket.close()
