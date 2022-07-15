
import smtplib
from email.message import EmailMessage
import ssl
from flask import escape
import functions_framework

@functions_framework.http
def send_email(request):
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'destination_email' in request_json:
        destination_email = request_json['destination_email']
    elif request_args and 'destination_email' in request_args:
        destination_email = request_args['destination_email']
    else:
        destination_email = 'World'

    my_email = "verdysworld@gmail.com"
    my_email_pass = "mascwseuajhxjenh"
    
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
    
    return 'Email sent to {}!'.format(escape(destination_email))
  
  