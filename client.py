import socket
from Utils.logs import *


def client_program():
    host = socket.gethostname()
    port = 5000
    print(info('Connecting to server...'))
    client_socket = socket.socket()
    client_socket.connect((host, port))
    print(info('Connexion success !'))
    message = input(warn('Your message: '))

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print(warn(f'Message from user {c.white(host)}: {data}'))
        message = input(info('Your message response: '))

    client_socket.close()


try:
    client_program()
except ConnectionRefusedError:
    print(critical('Connexion refused !'))
