import mailtrap as mt
from django.conf import settings

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
