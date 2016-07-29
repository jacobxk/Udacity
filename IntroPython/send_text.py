from twilio.rest import TwilioRestClient

account_sid = "AC5e384c975b4487f4d2c09870b94e3e2b" # Your Account SID from www.twilio.com/console
auth_token  = "2c0a76fcb3f017f72c23d283373ced78"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="+85268746013", 
    from_="+13477672288",
    body="Hello from Python!")

print message.sid
