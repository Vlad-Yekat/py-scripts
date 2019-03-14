import socket
from select import select

to_monitor = []
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('localhost', 5001))
server.listen()


def accept_server(server):
    client, addr = server.accept()
    print("Conn from", addr)
    to_monitor.append(client)


def send_message(client):
    request = client.recv(1024)
    print(request)
    if request:
        client.send("123".encode())
    else:
        client.close()


def event_loop():
    while True:
        ready_to_read, _, _ = select(to_monitor, [], [])
        for sock in ready_to_read:
            if sock is server:
                accept_server(sock)
            else:
                send_message(sock)


if __name__ == "__main__":
    to_monitor.append(server)
    event_loop()
