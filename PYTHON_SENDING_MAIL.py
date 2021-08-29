import smtplib

import stdiomask
password1 = stdiomask.getpass()
print(password1)
sender_email = "gallabhargav2001@gmail.com"
receiver_email = "bhargavgalla2731@gmail.com"
message = "PRAISE THE LORD"

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(sender_email,password1)
print("login success")
server.sendmail(sender_email,receiver_email,message)
print("email has been sent to ",receiver_email)
