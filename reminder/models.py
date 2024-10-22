from django.db import models

# Create your models here.
class ClientAppointment(models.Model):
    first_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length=150, null=True)
    mobile_number = models.CharField(max_length=50)
    email_address = models.CharField(max_length=150, null=True)
    selected_property = models.TextField(null=True)
    selected_property_address = models.TextField()
    appointment_date = models.DateField()
    appointment_time = models.DateTimeField()

    def __str__(self):
        return f"{self.first_name} --- {self.appointment_date}"



class CradenMooreClients(models.Model):
    first_name = models.CharField(max_length=250)
    mobile_number = models.CharField(max_length=100)
    meeting_link = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.first_name} - {self.mobile_number} {self.meeting_link[:5]}"

    
class EnishBookings(models.Model):
    """
        This model class is defined for Enish
        Restaurant with Vapi AI Voice Assistants.
        All fields to be sent to this API endpoint
        are all string values (Reason for using CharField in all cases.)
    """


    first_name = models.CharField(max_length=250)
    mobile_number = models.CharField(max_length=100)
    restaurant_location = models.CharField(max_length=250)
    number_of_guests = models.CharField(max_length=150)
    appointment_date = models.CharField(max_length=150)


    def __str__(self):
        return f"{self.first_name} -- Location:{self.restaurant_location[:6]} -- {self.number_of_guests}"



language_options = (
    ("English", "English"),
    ("Spanish", "Spanish"),
)

class LaundryClinicCustomerQuery(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    customer_query_message = models.TextField()
    ai_email_response = models.TextField()
    phone_number = models.CharField(max_length=50, null=True)
    email_address = models.EmailField()
    language_mode = models.CharField(max_length=50, choices=language_options, default="English", null=True)


class LaundryClinicEnglishSpeakingCustomerQuery(models.Model):
    """This is the model class of Laundry Clinic English Speakers
    """

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()
    customer_query_message = models.TextField()
    customer_comments = models.TextField()
    ai_assistant_response = models.TextField()
    laundry_event_details = models.TextField()
    location = models.CharField(max_length=150)
    timestamp = models.DateTimeField()
    ai_email_response = models.TextField()
    phone_number = models.CharField(max_length=50)





class LaundryClinicSpanishSpeakingCustomerQuery(models.Model):
    """This is the model class of Laundry Clinic Spanish Speakers
    """
    spreadsheet_row = models.IntegerField(null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()
    phone_number = models.CharField(max_length=50, null=True)
    customer_query_message_english = models.TextField(null=True)
    customer_query_message_spanish = models.TextField(null=True)
    customer_comments_english = models.TextField(null=True)
    customer_comments_spanish = models.TextField(null=True)
    ai_assistant_response_english = models.TextField(null=True)
    ai_assistant_response_spanish = models.TextField(null=True)
    laundry_event_details_english = models.TextField(null=True)
    laundry_event_details_spanish = models.TextField(null=True)
    location = models.CharField(max_length=150, null=True)
    timestamp = models.DateTimeField()
    ai_email_response_spanish = models.TextField()
