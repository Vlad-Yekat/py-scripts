import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('localhost', 5001))
server.listen()

while True:
    client, addr = server.accept()
    print("Conn from", addr)
    while True:
        request = client.recv(1024)
        print(request)
        if not request:
            break
        else:
            client.send("123".encode())
