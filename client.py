import socket
import time


def server_stuff(addr):
    serv = socket.create_server(addr)
    while True:
        client, _ = serv.accept()
        client.send('Hello, friend!'.encode())
        ms = client.recv(1024).decode()
        if ms == 'server,ping':
            print("Connection works!")
        else:
            print(ms)


def client_stuff(addr):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(addr)
    while True:
        ms = sock.recv(1024).decode()
        sock.send(f'You send: {ms}'.encode())
        print(ms)


proxy_ip = ('176.53.163.30', 8888)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(proxy_ip)
msg = sock.recv(1024).decode().split(',')
if msg[0] == 'master':
    sock.shutdown(socket.SHUT_WR)
    sock.close()
    del sock
    time.sleep(0.5)
    server_stuff(addr=('0.0.0.0', int(msg[2])))
elif msg[0] == 'client':
    sock.shutdown(socket.SHUT_WR)
    client_stuff(addr=(msg[1], int(msg[2])))
