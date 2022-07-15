# GCP/AWS/Azure
You will be required to simulate the registration process on a website] This task is composed of 3 different sub tasks: 

1. Writing a “server” script which should be automated on a Virtual Machine in GCP
2. Writing a “client” script to send a messaKe to the server script
running on the VM
3. A GCP Function which sends an email to the client’s email, triggered by the server script

## Files required to submit:
serverapy, clientapy, GCP function script.

### Client.py
Should be executed via command line: python3 clientapy *email
email is the address that the client script sends to the server. You should use a real email that you can access to ensure you are
receiving the email. This script will send the email to the VM server.

### Server.py
Event-driven that responds to an email being received It should receive the message from the client and forward it to the GCP
function. 

### GCP function script
This procedural script running on a GCP function will simply take the first argument (the client email), and utilise a python library of choice, to send an email to the client’s email.

## Restrictions/Clarifications
  - Your client script should be able to externally access the “server” running on the VM, that is from outside GCP.
  - You may need to setup a Gmail account and “Enable Third-Party Access” to programmatically send emails in the GCP Function script.
  - You should consider HTTP triggers.
