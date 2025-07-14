from twilio.rest import Client

account_sid = 'AC364982624e21db53386b17cb38e4f736'
auth_token = 'b6cfea7537f7575a50c8f523a4a01c9c'
twilio_phone_number = '+15186678883'
recipient_phone_number = '+918279253678'

def send_sms(message,account_sid,auth_token,twilio_phone_number,recipient_phone_number):
    client = Client(account_sid, auth_token)

    try:
        client.messages.create(
            body=message,
            from_=twilio_phone_number,
            to=recipient_phone_number
        )
        print("SMS sent successfully!")
    except Exception as e:
        print(f"SMS sending failed: {e}")


send_sms("hello",account_sid,auth_token,twilio_phone_number,recipient_phone_number)