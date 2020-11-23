import imaplib
import email

host = 'imap.gmail.com'
username = 'ragnarknight99@gmail.com'
password = 'Ragnar@99'

mail = imaplib.IMAP4_SSL(host)
mail.login(username, password)
mail.select("inbox")

_, search_data = mail.search(None, 'UNSEEN')

for num in search_data[0].split():
    # print(num)
    _, data = mail.fetch(num, '(RFC822)')
    # print(data)
    _, b = data[0]
    email_message = email.message_from_bytes(b)
    for part in email_message.walk():
        if part.get_content_type() == "text/plain" or part.get_content_type() == "text/html":
            body = part.get_payload(decode=True)
            print(body)
