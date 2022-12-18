import smtplib
import ssl
from email.message import EmailMessage
email_sender = 'shangil2711@gmail.com'

email_password = 'dedbqucutxfwjyux'

email_recevier = ''
subject = 'check out my mail'

body = """ 
hii how are you??
mail sended using Python!!!!!
"""

em = EmailMessage()

em['From'] = email_sender
em['To'] = email_recevier
em['subject'] = subject
em.set_content(body)

filename = ['shantanu.txt']
for file in filename:
    with open(file,'rb') as f:
        file_data = f.read()
        file_name=f.name

    em.add_attachment(file_data,maintype='application',subtype='octet-stream',filename=file)


context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.send_message(em)


