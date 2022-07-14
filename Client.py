import socket 

s = socket.socket()
port = 3389
s.connect(('34.87.213.59', port))
print(s.recv(1024).decode())
s.close()