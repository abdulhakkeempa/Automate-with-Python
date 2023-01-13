import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
import pandas as pd;
from dotenv import load_dotenv
import os

#list to hold the details of failed communications
failed = []

#email body
body = """Respected sir , 

Thank you for attending the Pre University Capacity Building Workshop on Artificial Intelligence .  Here is your Participation Certificate.

With Regards
Organiser
Pre University Capacity Building Workshop
"""

#email subject
subject = "Certificate of Participation - IEEE Pre - University Capacity Building Workshop"


#function to send email
def send_mail(send_from, send_to, subject, text, files=None):
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = send_to
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

    #catching the exception incase of invalid email id
    try:
      smtp.sendmail(send_from, send_to, msg.as_string())
    except:
      failed.append(send_to)

#loading env variables
load_dotenv()

#smtp email configuration
smtp = smtplib.SMTP()
smtp._host = os.getenv('SMTP_SERVER')
smtp.connect(os.getenv('SMTP_SERVER'), os.getenv('SMTP_PORT'))
smtp.starttls()
smtp.login(os.getenv('FROM_EMAIL'), os.getenv('PASSWORD'))

#reading the dataset
df = pd.read_csv("assets/data/data.csv")

#iterating and sending the mail
for index,col in df.iterrows():
  print(col['Name']+":"+col['Email'])
  #attachment file
  file = "assets/"+col['Name'].rstrip()+".pdf"
  send_mail(os.getenv('FROM_EMAIL'),col['Email'].rstrip(),subject,body,file)


print("Failed Mails:"+failed)