import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 12345))
server_socket.listen(1)
server_socket.settimeout(10)  # Timeout after 10 seconds of inactivity
print("Server is listening...")

try:
    while True:
        try:
            conn, addr = server_socket.accept()
            print(f"Connection from {addr}")
            data = conn.recv(1024)
            print(f"Received: {data.decode('utf-8')}")
            conn.sendall(b"Hello, Client!")
            conn.close()
        except socket.timeout:
            print("No activity, server shutting down...")
            break
finally:
    server_socket.close()
