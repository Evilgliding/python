import socket
from time import sleep
import sys


HOST = (socket.gethostname(), 7774)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind(HOST)

server.listen()
print('---start---')

def index():
    with open('11.html','rb',encoding='uts-8') as f:
        res= f.read()

    return res.encode('utf-8')

def get_users():
    res="""
    <h1> USERS </h1>
    <p>user 1</p>
    <p>user 2</p>

"""
    return res.encode('utf-8')
OK = b'HTTP/1.1 200 OK\n\n'
ERR_404 = b'HTTP/1.1 404 Hso ti vvel????\n\n'

while 1:
    print('--listen---')
    client, addr = server.accept()  
    data = client.recv(1024).decode('utf-8').split('\n')
    method, addr, ver = data[0].split()

    if addr=='/':
        print(index)
        client.send(OK)
        client.send(index())
    elif addr=='/users':
        client.send(OK)
        client.send(get_users())
    else:
        client.send(ERR_404)

    print('--polucheno--')
    print(data)
    
    client.close()



