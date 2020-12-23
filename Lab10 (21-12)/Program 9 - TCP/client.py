import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 65432

print('\033[32m======== CLIENT ========\033[0m')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((SERVER_HOST, SERVER_PORT))
    while True:
        filename = input('Enter file name: ')

        if not filename:
            break

        sock.sendall(bytes(filename, 'utf-8'))
        print(f'Sent: {filename}')

        data = sock.recv(1024)
        contents = data.decode('utf-8')
        print(f'Received: {contents}')
        print()
