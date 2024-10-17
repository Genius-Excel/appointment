from django.shortcuts import render
from datetime import datetime
from rest_framework import generics
from .models import ClientAppointment, CradenMooreClients, EnishBookings, LaundryClinicCustomerQuery
from .serializers import ClientAppointmentSerializer, CradenMooreClientsSerializer, EnishBookingsSerializer, LaundryClinicCustomerQuerySerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import custom_email_sender, custom_sms_sender
from django.conf import settings
import stripe 
import json


stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.

class CreateClientAppointment(generics.CreateAPIView):
    queryset = ClientAppointment.objects.all()
    serializer_class = ClientAppointmentSerializer


class CreateCradenMooreClient(generics.CreateAPIView):
    queryset = CradenMooreClients.objects.all()
    serializer_class = CradenMooreClientsSerializer

    def perform_create(self, serializer):
        user = serializer.save()

        SMS_sender = "Craden Moore Solicitors"
        SMS_meesage = f"Hello {user.first_name}, we recently spoke few minutes ago. Kindly book an appointment with this link:{user.meeting_link}."
        SMS_recipient = user.mobile_number

        custom_sms_sender(SMS_sender, SMS_recipient, SMS_meesage)


class CreateEnishBooking(generics.CreateAPIView):
    queryset = EnishBookings.objects.all()
    serializer_class = EnishBookingsSerializer

    def perform_create(self, serializer):
        user = serializer.save()

        SMS_sender = "Enish"
        SMS_message = f"Hello {user.first_name},\n\n" \
                      f"Your table reservation at {user.restaurant_location} for {user.number_of_guests} guests is confirmed for {user.appointment_date}\n" \
                      f"We look forward to welcoming you!."
        
        SMS_recipient = user.mobile_number
        custom_sms_sender(SMS_sender, SMS_recipient, SMS_message)
        # custom_email_sender(settings.TEST_EMAIL, "Enish Testing", SMS_message, "Enish Restaurant")


## API View for sending Apology Email to customer for Laundry Clinic
class CreateLaundryClinicEmailApology(generics.CreateAPIView):
    queryset = LaundryClinicCustomerQuery.objects.all()
    serializer_class = LaundryClinicCustomerQuerySerializer

    def perform_create(self, serializer):
        customer = serializer.save()

        email_sender = 'Laundry Clinic'
        email_subject = 'Follow up on service complaints.'
        email_message = customer.ai_email_response
        email_recipient = customer.email_address

        custom_email_sender(email_recipient, email_subject, email_message, email_sender)

        # determine cusomer language for SMS:
        if customer.language_mode == "English":
            english_sms_message = f"Dear {customer.first_name}, your complaint has been passed to one of our team members to deal with and an email acknowledgement has also been sent to you. We will contact you shortly with a resolution. Thank you for choosing Laundry Clinic."
            custom_sms_sender('Laundry Clinic', customer.phone_number, english_sms_message)
        else:
            spanish_sms_message = f"Estimado {customer.first_name}, su queja se pasó a uno de los miembros de nuestro equipo para que la trate y también se le envió un acuse de recibo por correo electrónico. Nos comunicaremos con usted en breve con una resolución. Gracias por elegir Laundry Clinic."
            custom_sms_sender('Laundry Clinic', customer.phone_number, spanish_sms_message)
            


# IMPLEMENT STRIPE PAYMENT FOR ENISH
@csrf_exempt
def create_checkout_session(request, amount):
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'gbp',
                    'product_data': {
                        'name': 'Enish Table Reservation Deposit',
                    },
                    'unit_amount': amount,  # 50.00 pounds
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='https://oawosile.pythonanywhere.com/',
            cancel_url='https://oawosile.pythonanywhere.com/',
        )


        return JsonResponse({'sessionid': session.id, 'url': session.url})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
    

@csrf_exempt
def confirm_payment(request, stripe_session_id):
    try:
        session_status = None
        session = stripe.checkout.Session.retrieve(stripe_session_id)
        payment_intent_id = session.payment_intent
        session_payment_status = session.payment_status

        print(payment_intent_id)
        print(session_payment_status)

        return JsonResponse({'payment_status': session_payment_status, 'payment_intent_id': payment_intent_id, 'session': session})
    except Exception as e:
        return JsonResponse({"Erro": str(e)})

   
def sample(request):
    session_id = request.GET.get('session_id')
    return render(request, 'reminder/sample.html')

def payment_success(request):
    session_id = request.GET.get('session_id')
    # You can verify the session and perform actions like updating your database here
    return render(request, 'reminder/payment-success.html')

def payment_cancelled(request):
    return render(request, 'reminder/payment-success.html')

       
    
def home(request):
    return render(request, 'reminder/home.html')


