import smtplib


def send_mail(to, content):
    username = 'ragnarknight99@gmail.com'
    password = 'Ragnar@99'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()  # make conversation with gmail
    server.starttls()  # it start session for us
    server.login(username, password)  # authentication
    server.sendmail(username, to, content)
    server.close()


to = input("Enter the email address of recipent: ")
content = input("Enter the content for email: \n")

send_mail(to, content)
