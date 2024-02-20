import socket


sock = socket.socket()
sock.connect(('localhost', 7774))
sock.send(b"Hello Word")

data = sock.recv(1024)
sock.close()

print(data)

