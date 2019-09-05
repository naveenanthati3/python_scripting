#!/usr/bin/python2.7
# Python code to illustrate Sending mail from  
# your Gmail account  
import smtplib 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login("naveen3ba@gmail.com", "naveen@333") 
  
# message to be sent 
message = "Message_you_need_to_send"
  
# sending the mail 
s.sendmail("naveen3ba@gmail.com", "naveen3ba@gmail.com", message) 
  
# terminating the session 
s.quit() 