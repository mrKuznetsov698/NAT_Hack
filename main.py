import socket
import time

master_ip = None
anybody_was_connected = False


def send_ms(address, ms: str):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(address)
    sock.send(ms.encode())


serv = socket.create_server(('0.0.0.0', 8888))
while True:
    client, address = serv.accept()
    if not anybody_was_connected:
        anybody_was_connected = True
        master_ip = address
        print(master_ip)
        client.send(f'master,{address[0]},{address[1]}'.encode())
        client.close()
        time.sleep(1)
        # client.send(b'server,ping')
        send_ms(address, 'server,ping')
    else:
        client.send(f'client,{master_ip[0]},{master_ip[1]}'.encode())
        client.shutdown(socket.SHUT_WR)
        serv.close()
        break
