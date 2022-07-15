import socket 
import smtplib
from email.message import EmailMessage
import ssl
from dotenv import load_dotenv
import os

load_dotenv()

def send_email(destination_email: str):
  my_email = os.environ.get('EMAIL_NAME')
  my_email_pass = os.environ.get('EMAIL_PASS')
  print(my_email)
  print(my_email_pass)
  subject = "Test Email"
  body = '''This is a test email'''
  em = EmailMessage()
  em['From'] = my_email
  em['To'] = destination_email
  em['Subject'] = subject
  em.set_content(body)

  ssl_context = ssl.create_default_context()

  with smtplib.SMTP_SSL('smtp.gmail.com', context=ssl_context) as smtp:
    smtp.login(my_email, my_email_pass)
    try:
      smtp.sendmail(my_email, destination_email, em.as_string())
      print(f"Email has been sent from {my_email} to {destination_email}")
    except smtplib.SMTPResponseException as e:
      print(f"Error with: {e}")

  
s = socket.socket()
print("Socket Successfully Created")
port = 3391
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
    send_email(destination_email)
    c_socket.send("Email has been sent.".encode())

  c_socket.send("Thank you for connectin!".encode())
  c_socket.close()