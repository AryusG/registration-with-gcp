import socket 

s = socket.socket()
print("Socket Successfully Created")
port = 3389
s.bind(('', port))
print(f"Socket Binded to Port {port}")
s.listen(5)
print("Socket is Listening...")

while True:
  c_socket, address = s.accept()
  print(f"Got Connection From {address}")
  message = "Thank you for connecting"
  c_socket.send(message.encode())
  c_socket.close()