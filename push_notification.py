from twilio.rest import Client
import os
from dotenv import load_dotenv

# If this doesn't work, you need to create a .env file in the same directory as this file
# and add the following lines:
# TWILIO_ACCOUNT_SID=your_account_sid
# TWILIO_AUTH_TOKEN=your_auth_token
# Replace your_account_sid and your_auth_token with a valid Twilio account SID and auth token
# You can find these in your Twilio account dashboard at https://www.twilio.com/console
# We are using the whatsapp version of the Twilio API

load_dotenv()

class BurnoutNotifier:
    def __init__(self, to_phone_number,  account_sid, auth_token):
        self.to_phone_number = to_phone_number
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.client = Client(account_sid, auth_token)
    
    def send_notification(self):
        message = self.client.messages.create(
            body="Burnout detected! Please take a break and take care of yourself.",
            # We cant send messages to unverified numbers in the free tier
            to=f"whatsapp:{self.to_phone_number}".replace(' ', ''),
            from_='whatsapp:+14155238886',
        )
        
        print(f"Notification sent: {message.sid}")


if __name__ == '__main__':

    # Get twilio account_sid and auth_token .env file
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    to_phone_number = os.getenv('TWILIO_PHONE_NUMBER')

    # Send notification to the phone number
    notifier = BurnoutNotifier(to_phone_number=to_phone_number, account_sid=account_sid, auth_token=auth_token)
    notifier.send_notification()

