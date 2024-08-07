from celery import shared_task
from django.utils import timezone
from .utils import custom_email_sender, custom_sms_sender
from .models import ClientAppointment
from datetime import timedelta 
from django.contrib.auth import get_user_model

User = get_user_model()


@shared_task(bind=True)
def send_email_reminder(self):
    now = timezone.now()

    current_time = now.astimezone(timezone.get_default_timezone())

    one_day_ahead = current_time + timedelta(days=1)
    one_hour_ahead = current_time + timedelta(hours=1)
    ten_minutes_ahead = current_time + timedelta(minutes=10)

    # Find out appointments one day ahead
    appointments_one_day = ClientAppointment.objects.filter(
        appointment_date=one_day_ahead.date(),
        appointment_time__hour=one_hour_ahead.time().hour,
        appointment_time__minute=one_day_ahead.time().minute
    )

    # Find out appointment 1 hour ahead
    appointments_one_hour = ClientAppointment.objects.filter(
        appointment_date=one_day_ahead.date(),
        appointment_time__hour=one_hour_ahead.time().hour,
        appointment_time__minute=one_hour_ahead.time().minute,

    )

    # Find appointments ten minutes ahead
    appointments_ten_minutes = ClientAppointment.objects.filter(
        appointment_date=ten_minutes_ahead.date(),
        appointment_time__hour=ten_minutes_ahead.time().hour,
        appointment_time__minute=ten_minutes_ahead.time().minute
    )

    # Send appoitments notification
    for appointment in appointments_one_day:
        email_subject = 'Reminder: Property inspection.'
        email_message = f"Hello {appointment.first_name}, kindly note that your appointment is coming up on {appointment.appointment_date}, location:{appointment.selected_property_address} see you there!"
        sender = 'Favour Idowu'
        email_address = appointment.email_address
        custom_email_sender(email_address, email_subject, email_message, sender)

        # Send Outbound SMS Reminder
        sms_message_content = f"Hello {appointment.first_name}, kindly note that your appointment is coming up on {appointment.appointment_date}, location:{appointment.selected_property_address} see you there!"
        custom_sms_sender("Tros Technologies", appointment.mobile_number, sms_message_content)


    for appointment in appointments_one_hour:
        email_subject = 'Reminder: Property inspection.'
        email_message = f"Hello {appointment.first_name}, kindly note that your appointment is about to start in an hour, location:{appointment.selected_property_address} see you there!"
        sender = 'Favour Idowu'
        email_address = appointment.email_address
        custom_email_sender(email_address, email_subject, email_message, sender)

        # Send outbound SMS reminder
        sms_message_content = f"Hello {appointment.first_name}, kindly note that your appointment is coming up on {appointment.appointment_date}, location:{appointment.selected_property_address} see you there!"
        custom_sms_sender("Tros Technologies", appointment.mobile_number, sms_message_content)

    for appointment in appointments_ten_minutes:
        email_subject = 'Reminder: Property inspection.'
        email_message = f"Hello {appointment.first_name}, kindly note that your appointment is about to start in 10 mins, location:{appointment.selected_property_address} see you there!"
        sender = 'Favour Idowu'
        email_address = appointment.email_address
        custom_email_sender(email_address, email_subject, email_message, sender)

        # Send outbound SMS Reminder
        sms_message_content = f"Hello {appointment.first_name}, kindly note that your appointment is about to start in 10 mins, location:{appointment.selected_property_address} see you there!"
        custom_sms_sender("Tros Technologies", appointment.mobile_number, sms_message_content)