#!/usr/bin/python2.7
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'twilio_ac_id'
auth_token = 'twilio_access_token'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hello there!',
                              from_='whatsapp:twilio_whatsapp_number',
                              to='whatsapp:receiver_number'
                          )

print(message.sid)
