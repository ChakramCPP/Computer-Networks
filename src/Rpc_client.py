import socket

HOST = '127.0.0.1'
PORT = 5000
address = (HOST, PORT)

with socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) as s:
    s.sendto(b'Hii Need help!', address)
    print('Message sent')
    data = s.recv(1024)
    print('Response:', data.decode())
    data = 'rstudio'
    s.sendto(data.encode(), address)
    print('Waiting for the remote server...')
    # output = s.recv(1024)
    # print('Output: ', output.decode())