import socket 
import smtplib
from email.message import EmailMessage
import ssl
from dotenv import load_dotenv
import os
import requests
from requests.structures import CaseInsensitiveDict
  
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

  data = c_socket.recv(1024)
  if len(data) > 0:
    destination_email = data.decode()
    url = "https://australia-southeast1-cybernetic-muse-356101.cloudfunctions.net/send-email"
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    payload = '{"destination_email": "verdyg24@gmail.com"}'
    response = requests.post(url, headers=headers, data=payload)

    c_socket.send("Email has been sent.".encode())

  c_socket.send("Thank you for connecting!".encode())
  c_socket.close()