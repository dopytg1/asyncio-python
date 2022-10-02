import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("localhost", 5000))
server_socket.listen()


while True:
    print("before accept")
    client_socket, address = server_socket.accept()
    print(f"{address} has connected")
    while True:
        print("before .recv()")
        request = client_socket.recv(4096)
        if not request:
            break
        else:
            response = "hello world\n".encode()
            client_socket.send(response)

    print("outside")
    client_socket.close()


