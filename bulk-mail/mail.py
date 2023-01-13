import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
import pandas as pd;
from dotenv import load_dotenv
import os

#function to send email
def send_mail(send_from, send_to, subject, text, files=None,server="127.0.0.1"):
    assert isinstance(send_to, list)

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    with open(files, "rb") as fil:
      part = MIMEApplication(
              fil.read(),
              Name=basename(files)
      )
    # After the file is closed
    part['Content-Disposition'] = 'attachment; filename="%s"' % basename(files)
    msg.attach(part)


    smtp = smtplib.SMTP(server)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()


load_dotenv()

#smtp email configuration
smtp = smtplib.SMTP(os.getenv('SMTP_SERVER'), os.getenv('SMTP_PORT'))
smtp.starttls()
smtp.login(os.getenv('FROM_EMAIL'), os.getenv('PASSWORD'))

df = pd.read_csv("assets/data/data.csv")

for index,col in df.iterrows():
  print(col['Name']+":"+col['Email'])



subject = """Respected sir , 

Thank you for attending the Pre University Capacity Building Workshop on Artificial Intelligence .  Here is your Participation Certificate.

With Regards
Organiser
Pre University Capacity Building Workshop
"""

