from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from rest_framework import generics
from .models import ( ClientAppointment, CradenMooreClients, EnishBookings, LaundryClinicCustomerQuery,
                     LaundryClinicEnglishSpeakingCustomerQuery, LaundryClinicSpanishSpeakingCustomerQuery,
                     LaundryClinicVoiceCall,
                     CeraCerni, ImageAds)
from .serializers import ( ClientAppointmentSerializer, CradenMooreClientsSerializer, 
                          EnishBookingsSerializer, LaundryClinicCustomerQuerySerializer,
                          LaundryClinicEnglishSpeakingCustomerQuerySerializer,
                          LaundryClinicSpanishSpeakingCustomerQuerySerializer,
                          LaundryClinicVoiceCallSerializer,
                          CercerniSerializer, ImageAdsSerializer)
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import custom_email_sender, custom_sms_sender, send_email_with_html_template
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
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






## Laundry Clinic View logic

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
            


class CreateLaundryClinicVoiceCall(generics.CreateAPIView):
    queryset = LaundryClinicVoiceCall.objects.all()
    serializer_class = LaundryClinicVoiceCallSerializer



class CreateEnglishSpeakingCustomersQuery(generics.CreateAPIView):
    queryset = LaundryClinicEnglishSpeakingCustomerQuery.objects.all()
    serializer_class = LaundryClinicEnglishSpeakingCustomerQuerySerializer



class CreateSpanishSpeakingCustomersQuery(generics.CreateAPIView):
    queryset = LaundryClinicSpanishSpeakingCustomerQuery.objects.all()
    serializer_class = LaundryClinicSpanishSpeakingCustomerQuerySerializer


class UpdateSpanishSpeakingcustomersQuery(generics.RetrieveUpdateAPIView):
    queryset = LaundryClinicSpanishSpeakingCustomerQuery.objects.all()
    serializer_class = LaundryClinicSpanishSpeakingCustomerQuerySerializer
    lookup_field = 'spreadsheet_row'


def list_english_customers(request):
    customers = LaundryClinicEnglishSpeakingCustomerQuery.objects.all()

    context = {'customers': customers}
    return render(request, 'reminder/english-customer.html', context)


def list_spanish_customers(request):
    customers = LaundryClinicSpanishSpeakingCustomerQuery.objects.all()

    context = {'customers': customers}
    return render(request, 'reminder/spanish-customer.html', context)


@login_required(login_url='login-user')
def laundry_clinic_dashboard_test(request):
    spanish_customers = LaundryClinicSpanishSpeakingCustomerQuery.objects.all().order_by(
        '-timestamp', 'status'
    ).values(
        'id',
        'first_name',
        'last_name',
        'email_address',
        'phone_number',
        'customer_query_message_english',
        'location',
        'status',
        'timestamp',
    )

    english_customers = LaundryClinicEnglishSpeakingCustomerQuery.objects.all().order_by(
        '-timestamp', 'status'
    ).values(
        'id',
        'first_name',
        'last_name',
        'email_address',
        'phone_number',
        'customer_query_message',
        'location',
        'status',
        'timestamp',
    )

    customer_objs = list(english_customers) + list(spanish_customers)


    paginator = Paginator(customer_objs, 10)
    page_number = request.GET.get('page')
    customers = paginator.get_page(page_number)

    context = {'customers': customers, 'spanish_customers': spanish_customers}

    return render(request, 'reminder/laundry-index.html', context)


@login_required(login_url='login-user')
def get_detail_laundry_clinic_record(request, type, id):
    if type == 'spanish':
        customer = get_object_or_404(LaundryClinicSpanishSpeakingCustomerQuery, id=id)
    elif type == 'english':
        customer = get_object_or_404(LaundryClinicEnglishSpeakingCustomerQuery, id=id)
    else:
        return HttpResponse("Not Found")

    context = {'customer': customer, 'type': type}
    return render(request, 'reminder/record-detail.html', context)


@login_required(login_url='login-user')
def update_query_status(request, type, id, action_type):
    if type == 'spanish':
        customer = get_object_or_404(LaundryClinicSpanishSpeakingCustomerQuery, id=id)
    elif type == 'english':
        customer = get_object_or_404(LaundryClinicEnglishSpeakingCustomerQuery, id=id)
    else:
        return HttpResponse("Not Found")
    
    if action_type == 'do':
            customer.status = "Resolved"
    elif action_type == 'undo':
            customer.status = "Open"
    else:
         return HttpResponse("Error: invalid action type")

    customer.save()

    return redirect('laundry-index')

@login_required(login_url='login-user')
def get_all_laundry_clinic_calls(request):
    customer_objs =  LaundryClinicVoiceCall.objects.all()

    paginator = Paginator(customer_objs, 10)
    page_number = request.GET.get('page')
    customer_calls = paginator.get_page(page_number)

    context = {
        'customer_calls': customer_calls,
    }

    return render(request, 'reminder/laundry-clinic-calls.html', context)

@login_required(login_url='login-user')
def get_laundry_clinic_ai_call_detail(request, id):
    customer_call = get_object_or_404(LaundryClinicVoiceCall, id=id)

    context = {
        'customer_call': customer_call,
    }

    return render(request, 'reminder/ai-call-record-detail.html', context)


def login_user(request):
    if request.method == "POST":
        password = request.POST.get('password')
        username = request.POST.get('username')
        
        username_attempt = None
        # Query database to check if username exists
        try:
            username_attempt = User.objects.get(username=username)
        except ObjectDoesNotExist:
            messages.error(request, "Invalid Username entered")
            # return redirect(reverse(login_user))

        user = authenticate(request, password=password, username=username)
        if user is not None:
            login(request, user)
            return redirect('laundry-index')
        else:
            messages.error(request, "Incorrect password")
            return redirect('login-user')
    
    context = {'title': 'Login user'}
    return render(request, 'reminder/login.html', context)


@login_required(login_url='login-user')
def logout_user(request):
    logout(request)
    messages.info(request, "You have been logged out successfully!")
    return redirect('login-user')
## End Laundry Clinic View Logic






## Ceracerni

class CreateCeraniEmail(generics.CreateAPIView):
    queryset = CeraCerni.objects.all()
    serializer_class = CercerniSerializer

    def perform_create(self, serializer):
        user_response = serializer.save()
        # booking_id = user_response.booking_id
        # booking_name = user_response.booking_name
        selected_image = user_response.selected_image
        image_url = user_response.image_url
        email_address = settings.CERACERNI_EMAIL
        booking_email = user_response.booking_email
        email_subject = 'Booking Notification With Selected Image'
        email_sender = 'Tros Technologies'

        # Template details
        template_file = 'templates/reminder/ceracerni-email-notification.html'
        context = {
            'email_type': 'admin',
            'booking_email': booking_email,
            'selected_image': selected_image,
            'image_url': image_url,
        }

        send_email_with_html_template(template_file, context, email_address, email_subject, email_sender)

        customer_email_subject = 'Booking Confirmation With Selected Image'
        email_sender = "Ceracerni Art Hub"
        context['email_type'] = 'customer'

        send_email_with_html_template(
            template_file, context, booking_email, 
            customer_email_subject, email_sender
        )



## End Ceracerni




# IMPLEMENT STRIPE PAYMENT FOR ENISH
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
    

def payment_success(request):
    session_id = request.GET.get('session_id')
    # You can verify the session and perform actions like updating your database here
    return render(request, 'reminder/payment-success.html')

def payment_cancelled(request):
    return render(request, 'reminder/payment-success.html')

       
    
def home(request):
    return render(request, 'reminder/home.html')


class CreateImageAds(generics.CreateAPIView):
    queryset = ImageAds.objects.all()
    serializer_class = ImageAdsSerializer