#!/usr/bin/python2.7
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC785d42931b52c8bf5c7c5064d9a60ecc'
auth_token = '57ac2662b90e184ebd7418f98524bb8c'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hello there!',
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+919502340053'
                          )

print(message.sid)
