d#Python Script that sends an email
import smtplib
from openpyxl import load_workbook
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Send email function
def sendemail(toemail):
    #My email and password
    my_email = "gliscor2214@gmail.com"
    password = input()

    msg = MIMEMultipart()
    msg['From'] = my_email
    msg['To'] = toemail
    msg['Subject'] = "python email"

    body = "This is an email sent by a python script"
    msg.attach(MIMEText(body, 'plain'))

    #connect to gmail server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    server.login(my_email, password)

    text = msg.as_string()

    server.sendmail(my_email, toemail, text)

    server.quit()

#grabbing emails from a file will be added here
#wb = load_workbook(filename = 'email_list.xlsx')

sendemail("danieleberhart14@gmail.com")
