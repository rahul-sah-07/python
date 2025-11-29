# File-Transfer-App
import socket

HOST = ""   
PORT = 5001

server = socket.socket()
server.bind((HOST, PORT))
server.listen(1)
print("Waiting for sender to connect...")

conn, addr = server.accept()
print(f" Connected with: {addr}")

filename = conn.recv(1024).decode()
with open(filename, "wb") as file:
    print(f"Receiving file: {filename}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        file.write(data)

print("File received successfully!")
conn.close()
server.close()
