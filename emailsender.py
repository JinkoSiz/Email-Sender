import  smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'email here'
email['to'] = 'email here'
email['subject'] = 'You are millionaire!'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.host here.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('email here', 'password here')
    # Just some mischiefs
    for _ in range(10):
        smtp.send_message(email)

print('All done!')
