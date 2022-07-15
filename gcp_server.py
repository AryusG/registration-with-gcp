import socket 

def send_to_gcp_function(destination_email: str):
  gcp_fn_url = f"https://australia-southeast1-cybernetic-muse-356101.cloudfunctions.net/send-email?destination_email={destination_email}"
  

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
    send_to_gcp_function(destination_email=destination_email) 
    c_socket.send("Email has been sent.".encode())

  c_socket.send("Thank you for connecting!".encode())
  c_socket.close()
  
  