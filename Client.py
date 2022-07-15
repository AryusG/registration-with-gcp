import socket 
import sys

cmd_line_input = False

if len(sys.argv[:]) > 1:
  cmd_line_email = sys.argv[1:][0]
  cmd_line_input = True

s = socket.socket()
port = 3389
gcp_vm_ip = '34.87.213.59'
# personal_ip = '127.0.0.1'
s.connect((gcp_vm_ip, port))

if cmd_line_input:
  s.send(cmd_line_email.encode())

print(s.recv(1024).decode())
s.close()