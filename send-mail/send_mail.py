import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

username = 'ragnarknight99@gmail.com'
password = 'Ragnar@99'


def send_mail(text="Surprise Motherfucker!!", subject="HelLo FuCkeRs",
              from_email='Ragnar Lodbrok <ragnarknight99@gmail.com>', to_emails=None, html=None):

    assert isinstance(to_emails, list)

    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ", ".join(to_emails)
    msg['Subject'] = subject

    text_part = MIMEText(text, 'plain')
    msg.attach(text_part)

    if html != None:
        html_part = MIMEText(html, 'html')
        msg.attach(html_part)

    msg_str = msg.as_string()

    """ LOGIN TO SMTP SERVER """
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()

    server.login(username, password)
    server.sendmail(from_email, to_emails, msg_str)

    server.quit()
    # with smtplib.SMTP() as server:
    #     server.login()


send_mail(to_emails=['ragnarknight99@gmail.com'])
