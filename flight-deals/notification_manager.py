from twilio.rest import Client
import smtplib

TWILIO_SID = "use twilio sid"
TWILIO_AUTH_TOKEN = "use twilio auth token"
TWILIO_VIRTUAL_NUMBER = "use twilio provided num"
TWILIO_VERIFIED_NUMBER = "use the verified num that u used to login"
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "munugotisairuthvik@gmail.com"
MY_PASSWORD = "use app password"

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
        
    def send_emails(self, emails, message):
        with smtplib.SMTP_SSL(MAIL_PROVIDER_SMTP_ADDRESS,port=465) as connection:
            # connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8'))