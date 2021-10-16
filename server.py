import socket
from Utils.logs import *


def server_program():
    print(info('Starting server...'))
    host = socket.gethostname()
    port = 5000
    server_socket = socket.socket()
    server_socket.bind((host, port))
    print(info(f"Server start on port: {c.white.bold(port)}"))
    server_socket.listen(2)
    conn, address = server_socket.accept()
    print(warn(f'Client connected to address: {address[0]}'))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print(warn(f'Message received from user: {address[0]}, content: {c.white.underline(str(data))}'))
        data = input(info('Your message response: '))
        conn.send(data.encode())
        print(info('Message send !'))
    conn.close()
    print(warn('Server disable !'))


server_program()
