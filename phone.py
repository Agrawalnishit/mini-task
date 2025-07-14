from twilio.rest import    Client

# Your Twilio credentials
account_sid = 'AC364982624e21db53386b17cb38e4f736'
auth_token = 'b6cfea7537f7575a50c8f523a4a01c9c'
twilio_phone_number = '+15186678883'
recipient_phone_number = '+918279253678'
   # The number you want to call (must be verified on trial)

# Initialize the client
client = Client(account_sid, auth_token)

# Make the call
call = client.calls.create(
    to=+918279253678,
    from_=+15186678883,
    url='http://demo.twilio.com/docs/voice.xml'  # This URL defines what the call will say
)

print(f"Call initiated with SID: {call.sid}")
