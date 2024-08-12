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