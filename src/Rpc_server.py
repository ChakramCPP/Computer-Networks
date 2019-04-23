import socket
import os

HOST = '127.0.0.1'
PORT = 5000


def get_output(data):
    if data == 'putty':
        file = os.startfile('C:\Program Files (x86)\PuTTY\putty.exe')
    else:
        file = os.startfile('C:\Program Files\RStudio\\bin\\rstudio.exe')


with socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    data, address = s.recvfrom(1024)
    print(data.decode(), 'from', address)
    while True:
        s.sendto(b'Send the query!', address)
        data, address = s.recvfrom(1024)
        get_output(data.decode())
        data, address = s.recvfrom(1024)
        get_output(data.decode())
        # s.sendto(output.encode(), address)
        # print("Output sent!!")
