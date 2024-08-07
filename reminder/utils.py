import mailtrap as mt
from django.conf import settings
from decouple import config 
import vonage

# Send email custom function.
def custom_email_sender(email_address, subject, message, sender_name):
    mail = mt.Mail(
                    sender=mt.Address(email='noreply@easyappz.com', name=sender_name),
                    to=[mt.Address(email=email_address)],
                    subject=subject,
                    text=message,
                    html=None,
                )

    client = mt.MailtrapClient(token=settings.SMTP_API_TOKEN)
    client.send(mail)



VONAGE_API_KEY=config("VONAGE_API_KEY")
VONAGE_API_SECRET=config("VONAGE_API_SECRET")

def custom_sms_sender(sms_sender, sms_recipient, sms_message):
    client = vonage.Client(key=VONAGE_API_KEY, secret=VONAGE_API_SECRET)

    print("Sending SMS")
    try:
        response_data = client.sms.send_message({
            "from": sms_sender,
            "to": sms_recipient,
            "text": sms_message,
        })

        print("SMS Sent success")
        print(response_data)
    except Exception as e:
        print(f"Not sending because: {e}")