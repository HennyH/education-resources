
#!/usr/bin/env python3

# 1. The imap message parsing code was taken from https://www.thepythoncode.com/article/reading-emails-in-python
# 2. You need to enable 'lesssecureapps' in gmail using https://www.google.com/settings/security/lesssecureapps
from getpass import getpass
import cgi
import cgitb
import os, imaplib, email, email.header

cgitb.enable()

print("Content-Type: text/html")
print()

email_address = "henry.hollingworth@ashdalesc.wa.edu.au"
mail = imaplib.IMAP4_SSL(host="imap.gmail.com", port=993)
mail.login(email_address, os.environ.get("ASHDAHLE_PW") or getpass(f"Password for {email_address}"))
mail.select()
_, data = mail.search(None, "ALL")
msgnums = data[0].split()

print("<ol>")
for msgnum in msgnums[:10]:
    _, msg = mail.fetch(msgnum, "(RFC822)")
    for response in msg:
        if not isinstance(response, tuple):
            continue
        # parse a bytes email into a message object
        msg = email.message_from_bytes(response[1])
        # decode the email subject
        subject, encoding = email.header.decode_header(msg["Subject"])[0]
        if isinstance(subject, bytes):
            # if it's a bytes, decode to str
            subject = subject.decode(encoding)
        # decode email sender
        from_h, encoding = email.header.decode_header(msg.get("From"))[0]
        if isinstance(from_h, bytes):
            from_h = from_h.decode(encoding)
        # if the email message is multipart
        if msg.is_multipart():
            # iterate over email parts
            for part in msg.walk():
                # extract content type of email
                content_type = part.get_content_type()
                content_disposition = str(part.get("Content-Disposition"))
                try:
                    # get the email body
                    body = part.get_payload(decode=True).decode()
                except:
                    pass
        else:
            # extract content type of email
            content_type = msg.get_content_type()
            # get the email body
            body = msg.get_payload(decode=True).decode()
        print(f"""
            <li>
                <h2>{subject}</h2>
                <em>{from_h}</em>
                <p>{body}</p>
            </li>
        """)
print("</ol>")