# Send SMS message to phone when script has crashed/finished.
# Currently scripted for gmail and at&t phone number. Change line 6 (if not gmail) and line 9 (if not at&t).

import smtplib

server = smtplib.SMTP( "smtp.gmail.com", 587 )
server.starttls()
server.login( '<gmail_address>', '<gmail_password>' )
server.sendmail( '<author>', '<number>@txt.att.net', '<message here>' )

'''
You might need to change the SMS gateway for your cell provider, one link
is http://sms411.net/how-to-send-email-to-a-phone/ or Google
<cell provider> SMS email gateway and test it. 
'''

print ("text message sent")
