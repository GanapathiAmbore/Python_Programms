# Python code to illustrate Sending mail from
# your Gmail account
import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("ganapathi.ambore@techo2.com", "8801091595")

# message to be sent
message = "Message_you_need_to_send"

# sending the mail
s.sendmail("ganapathi.ambore@techo2.com", "ganapathiambore@gmail.com", message)

# terminating the session
s.quit()
